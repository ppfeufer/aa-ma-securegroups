"""
The models
"""

# Standard Library
import datetime
from collections import defaultdict

# Third Party
import humanize

# Django
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.db.models import F, OuterRef, Q, Subquery
from django.utils.formats import localize
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _
from django.utils.translation import ngettext

# Alliance Auth
from allianceauth.eveonline.models import EveCharacter, EveCorporationInfo

# Member Audit
from memberaudit.app_settings import MEMBERAUDIT_APP_NAME
from memberaudit.models import (
    Character,
    CharacterAsset,
    CharacterCorporationHistory,
    CharacterRole,
    CharacterSkillSetCheck,
    CharacterTitle,
    General,
    SkillSet,
)

# Alliance Auth (External Libs)
from eveuniverse.models import EveType


def _get_threshold_date(timedelta_in_days: int) -> datetime.datetime:
    """
    Get the threshold date

    :param timedelta_in_days: The timedelta in days
    :type timedelta_in_days: int
    :return: The threshold date
    :rtype: datetime.datetime
    """

    return datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(
        days=timedelta_in_days
    )


class BaseFilter(models.Model):
    """
    BaseFilter
    """

    description = models.CharField(
        max_length=500,
        help_text=_("The filter description that is shown to end users."),
    )  # this is what is shown to the user

    class Meta:
        """
        Model meta definitions
        """

        abstract = True

    def __str__(self) -> str:
        """
        Model string representation

        :return: The model string representation
        :rtype: str
        """

        return f"{self.name}: {self.description}"

    def process_filter(self, user: User) -> bool:
        """
        Process the filter

        :param user: The user
        :type user: User
        :return: Return True when filter applies to the user, else False.
        :rtype: bool
        """

        raise NotImplementedError(_("Please create a filter!"))

    def audit_filter(self, users: models.QuerySet[User]) -> dict:
        """
        Return information for each given user weather they pass the filter,
        and a help message shown in the audit feature.

        :param users: The users
        :type users: models.QuerySet[User]
        :return: The audit information
        :rtype: dict
        """

        raise NotImplementedError(_("Please create an audit function!"))


class ActivityFilter(BaseFilter):
    """
    ActivityFilter
    """

    inactivity_threshold = models.PositiveIntegerField(
        help_text=_("Maximum allowable inactivity, in <strong>days</strong>.")
    )

    class Meta:
        """
        Model meta definitions
        """

        verbose_name = _("Smart Filter: Activity")
        verbose_name_plural = verbose_name

    @property
    def name(self) -> str:
        """
        Filter name

        :return: The filter name
        :rtype: str
        """

        inactivity_threshold = ngettext(
            singular=f"{self.inactivity_threshold:d} day",
            plural=f"{self.inactivity_threshold:d} days",
            number=self.inactivity_threshold,
        )

        return _(f"Activity [Last {inactivity_threshold}]")

    def process_filter(self, user: User) -> bool:
        """
        Process the filter

        :param user: The user
        :type user: User
        :return: Return True when filter applies to the user, else False.
        :rtype: bool
        """

        threshold_date = _get_threshold_date(
            timedelta_in_days=self.inactivity_threshold
        )

        return (
            Character.objects.owned_by_user(user=user)
            .filter(
                Q(online_status__last_login__gt=threshold_date)
                | Q(online_status__last_logout__gt=threshold_date),
            )
            .count()
            > 0
        )

    def audit_filter(self, users) -> dict:
        """
        Audit Filter

        :param users: The users
        :type users: models.QuerySet[User]
        :return: The audit information
        :rtype: dict
        """

        threshold_date = _get_threshold_date(
            timedelta_in_days=self.inactivity_threshold
        )

        output = defaultdict(lambda: {"message": "", "check": False})

        for user in users:
            characters = Character.objects.owned_by_user(user=user).filter(
                Q(online_status__last_login__gt=threshold_date)
                | Q(online_status__last_logout__gt=threshold_date),
            )

            if characters.count() > 0:
                chars = defaultdict(list)

                for char in characters:
                    chars[char.user.pk].append(char.eve_character.character_name)

                for char_user, char_list in chars.items():
                    message = ngettext(
                        singular="Active character: ",
                        plural="Active characters: ",
                        number=len(char_list),
                    )

                    output[char_user] = {
                        "message": message + ", ".join(sorted(char_list)),
                        "check": True,
                    }

        return output


class AgeFilter(BaseFilter):
    """
    AgeFilter
    """

    age_threshold = models.PositiveIntegerField(
        help_text=_("Minimum allowable age, in <strong>days</strong>.")
    )

    class Meta:
        """
        Model meta definitions
        """

        verbose_name = _("Smart Filter: Character Age")
        verbose_name_plural = verbose_name

    @property
    def name(self) -> str:
        """
        Filter name

        :return: The filter name
        :rtype: str
        """

        age_threshold = ngettext(
            f"{self.age_threshold:d} day",
            f"{self.age_threshold:d} days",
            self.age_threshold,
        )

        return _(f"Character age [{age_threshold}]")

    def process_filter(self, user: User) -> bool:
        """
        Process the filter

        :param user: The user
        :type user: User
        :return: Return True when filter applies to the user, else False.
        :rtype: bool
        """

        threshold_date = _get_threshold_date(timedelta_in_days=self.age_threshold)

        return (
            Character.objects.owned_by_user(user=user)
            .filter(details__birthday__lt=threshold_date)
            .count()
            > 0
        )

    def audit_filter(self, users) -> dict:
        """
        Audit Filter

        :param users: The users
        :type users: models.QuerySet[User]
        :return: The audit information
        :rtype: dict
        """

        threshold_date = _get_threshold_date(timedelta_in_days=self.age_threshold)

        output = defaultdict(lambda: {"message": "", "check": False})

        for user in users:
            characters = Character.objects.owned_by_user(user=user).filter(
                details__birthday__lt=threshold_date
            )

            if characters.count() > 0:
                chars = defaultdict(list)

                for char in characters:
                    chars[char.user.pk].append(char.eve_character.character_name)

                for char_user, char_list in chars.items():
                    output[char_user] = {
                        "message": ", ".join(sorted(char_list)),
                        "check": True,
                    }

        return output


class AssetFilter(BaseFilter):
    """
    AssetFilter
    """

    assets = models.ManyToManyField(
        to=EveType,
        help_text=_("User must possess <strong>one</strong> of the selected assets."),
    )

    class Meta:
        """
        Model meta definitions
        """

        verbose_name = _("Smart Filter: Asset")
        verbose_name_plural = verbose_name

    @property
    def name(self) -> str:
        """
        Filter name

        :return: The filter name
        :rtype: str
        """

        return _("Member Audit Asset")

    def process_filter(self, user: User) -> bool:
        """
        Process the filter

        :param user: The user
        :type user: User
        :return: Return True when filter applies to the user, else False.
        :rtype: bool
        """

        return CharacterAsset.objects.filter(
            character__eve_character__character_ownership__user=user,
            eve_type__in=self.assets.all(),
        ).exists()

    def audit_filter(self, users: models.QuerySet[User]) -> dict:
        """
        Audit Filter

        :param users: The users
        :type users: models.QuerySet[User]
        :return: The audit information
        :rtype: dict
        """

        matching_assets = CharacterAsset.objects.filter(
            character=OuterRef("pk"), eve_type__in=list(self.assets.all())
        )
        characters = (
            Character.objects.filter(
                eve_character__character_ownership__user__in=list(users)
            )
            .annotate(asset_name=Subquery(matching_assets.values("eve_type__name")[:1]))
            .values(
                "asset_name",
                user_id=F("eve_character__character_ownership__user_id"),
                character_name=F("eve_character__character_name"),
            )
        )

        output_users = {}
        for character in characters:
            user_id = character["user_id"]
            if user_id not in output_users:
                output_users[user_id] = []

            asset_name = character["asset_name"]
            if asset_name:
                character_name = character["character_name"]
                output_users[character["user_id"]].append(
                    f"{character_name} ({asset_name})"
                )

        output = {}
        for user_id, matches in output_users.items():
            if matches:
                message = ", ".join(sorted(matches))
                check = True
            else:
                message = _("No matching assets found")
                check = False

            output[user_id] = {"message": message, "check": check}

        user_ids = set(users.values_list("id", flat=True))
        missing_user_ids = user_ids - set(output.keys())
        for user_id in missing_user_ids:
            output[user_id] = {
                "message": _("No audit information found"),
                "check": False,
            }

        return output


class ComplianceFilter(BaseFilter):
    """
    ComplianceFilter
    """

    reversed_logic = models.BooleanField(
        default=False,
        help_text=_("If set all members WITHOUT compliance will pass this check."),
    )

    class Meta:
        """
        Model meta definitions
        """

        verbose_name = _("Smart Filter: Compliance")
        verbose_name_plural = verbose_name

    @property
    def name(self) -> str:
        """
        Return name of this filter.

        :return: The filter name
        :rtype: str
        """

        return _("Compliance")

    def process_filter(self, user: User) -> bool:
        """
        Process the filter

        :param user: The user
        :type user: User
        :return: Return True when filter applies to the user, else False.
        :rtype: bool
        """

        unregistered_characters = EveCharacter.objects.filter(
            character_ownership__user=user, memberaudit_character__isnull=True
        )

        if self.reversed_logic:
            return unregistered_characters.exists()

        return not unregistered_characters.exists()

    def audit_filter(self, users) -> dict:
        """
        Audit Filter

        :param users: The users
        :type users: models.QuerySet[User]
        :return: The audit information
        :rtype: dict
        """

        unregistered_characters = EveCharacter.objects.filter(
            character_ownership__user__in=list(users),
            memberaudit_character__isnull=True,
        ).values("character_name", user_id=F("character_ownership__user_id"))

        user_with_unregistered_characters = defaultdict(list)

        for obj in unregistered_characters:
            character_name = obj["character_name"]
            user_with_unregistered_characters[obj["user_id"]].append(
                f"{character_name}"
            )

        all_memberaudit_users_ids = General.users_with_basic_access().values_list(
            "id", flat=True
        )

        output = {}
        all_characters_message = _(
            f"All characters have been added to {MEMBERAUDIT_APP_NAME}"
        )

        for user_id in all_memberaudit_users_ids:
            unregistered_chars = user_with_unregistered_characters.get(user_id)

            if unregistered_chars:
                missing_characters_message = ngettext(
                    singular="Missing character: ",
                    plural="Missing characters: ",
                    number=len(unregistered_chars),
                )
                message = missing_characters_message + ", ".join(
                    sorted(unregistered_chars)
                )
                check = self.reversed_logic
            else:
                message = all_characters_message
                check = not self.reversed_logic

            output[user_id] = {"message": message, "check": check}

        return output


class CorporationRoleFilter(BaseFilter):
    """
    Filter for corporation roles.
    """

    corporations = models.ManyToManyField(
        to=EveCorporationInfo,
        related_name="+",
        help_text=_(
            "The character with the role must be in one of these corporations."
        ),
    )
    role = models.CharField(
        max_length=3,
        choices=CharacterRole.Role.choices,
        db_index=True,
        help_text=_("User must have a character with this role."),
    )
    include_alts = models.BooleanField(
        default=False,
        help_text=_(
            "When checked, the filter will also include the users alt-characters."
        ),
    )

    class Meta:
        """
        Model meta definitions
        """

        verbose_name = _("Smart Filter: Corporation Role")
        verbose_name_plural = verbose_name

    @property
    def name(self) -> str:
        """
        Return name of this filter.

        :return: The filter name
        :rtype: str
        """

        return _("Member Audit Corporation Role")

    def process_filter(self, user: User) -> bool:
        """
        Process the filter

        :param user: The user
        :type user: User
        :return: Return True when filter applies to the user, else False.
        :rtype: bool
        """

        qs = CharacterRole.objects.filter(
            character__eve_character__character_ownership__user=user,
            character__eve_character__corporation_id__in=self._corporation_ids(),
            role=self.role,
            location=CharacterRole.Location.UNIVERSAL,
        )

        if not self.include_alts:
            qs = qs.filter(character__eve_character__userprofile__isnull=False)

        return qs.exists()

    def audit_filter(self, users) -> dict:
        """
        Audit Filter

        :param users: The users
        :type users: models.QuerySet[User]
        :return: The audit information
        :rtype: dict
        """

        qs = Character.objects.filter(
            eve_character__character_ownership__user__in=list(users),
            eve_character__corporation_id__in=self._corporation_ids(),
            roles__role=self.role,
            roles__location=(CharacterRole.Location.UNIVERSAL),
        )

        if not self.include_alts:
            qs = qs.filter(eve_character__userprofile__isnull=False)

        matching_characters = qs.values(
            user_id=F("eve_character__character_ownership__user_id"),
            character_name=F("eve_character__character_name"),
        )

        user_with_characters = defaultdict(list)
        for user_id in matching_characters:
            character_name = user_id["character_name"]
            user_with_characters[user_id["user_id"]].append(f"{character_name}")

        output = {
            user_id: {"message": _("No matching character found"), "check": False}
            for user_id in users.values_list("id", flat=True)
        }

        for user_id, character_names in user_with_characters.items():
            output[user_id] = {
                "message": ", ".join(sorted(character_names)),
                "check": True,
            }

        return output

    def _corporation_ids(self) -> list[int]:
        """
        Return Eve IDs of corporations in this filter.

        :return: The Eve IDs of corporations in this filter
        :rtype: list[int]
        """

        return list(self.corporations.values_list("corporation_id", flat=True))


class CorporationTitleFilter(BaseFilter):
    """
    Filter for corporation titles.
    """

    corporations = models.ManyToManyField(
        to=EveCorporationInfo,
        related_name="+",
        help_text=_(
            "The character with the title must be in one of these corporations."
        ),
    )
    title = models.CharField(
        max_length=100,
        db_index=True,
        help_text=_("User must have a character with this title."),
    )
    include_alts = models.BooleanField(
        default=False,
        help_text=_(
            "When True, the filter will also include the users alt-characters."
        ),
    )

    class Meta:
        """
        Model meta definitions
        """

        verbose_name = _("Smart Filter: Corporation Title")
        verbose_name_plural = verbose_name

    @property
    def name(self) -> str:
        """
        Return name of this filter.

        :return: The filter name
        :rtype: str
        """

        return _("Member Audit Corporation Title")

    def process_filter(self, user: User) -> bool:
        """
        Process the filter

        :param user: The user
        :type user: User
        :return: Return True when filter applies to the user, else False.
        :rtype: bool
        """

        qs = CharacterTitle.objects.filter(
            character__eve_character__character_ownership__user=user,
            character__eve_character__corporation_id__in=self._corporation_ids(),
            name=self.title,
        )

        if not self.include_alts:
            qs = qs.filter(character__eve_character__userprofile__isnull=False)

        return qs.exists()

    def audit_filter(self, users) -> dict:
        """
        Audit Filter

        :param users: The users
        :type users: models.QuerySet[User]
        :return: The audit information
        :rtype: dict
        """

        qs = Character.objects.filter(
            eve_character__character_ownership__user__in=list(users),
            eve_character__corporation_id__in=self._corporation_ids(),
            titles__name=self.title,
        )

        if not self.include_alts:
            qs = qs.filter(eve_character__userprofile__isnull=False)

        matching_characters = qs.values(
            user_id=F("eve_character__character_ownership__user_id"),
            character_name=F("eve_character__character_name"),
        )

        user_with_characters = defaultdict(list)
        for user_id in matching_characters:
            character_name = user_id["character_name"]
            user_with_characters[user_id["user_id"]].append(f"{character_name}")

        output = {
            user_id: {"message": _("No matching character found"), "check": False}
            for user_id in users.values_list("id", flat=True)
        }

        for user_id, character_names in user_with_characters.items():
            output[user_id] = {
                "message": ", ".join(sorted(character_names)),
                "check": True,
            }

        return output

    def _corporation_ids(self) -> list[int]:
        """
        Return Eve IDs of corporations in this filter.

        :return: The Eve IDs of corporations in this filter
        :rtype: list[int]
        """

        return list(self.corporations.values_list("corporation_id", flat=True))


class SkillPointFilter(BaseFilter):
    """
    SkillPointFilter
    """

    skill_point_threshold = models.PositiveBigIntegerField(
        help_text=_("Minimum allowable skill points.")
    )

    class Meta:
        """
        Model meta definitions
        """

        verbose_name = _("Smart Filter: Skill Points")
        verbose_name_plural = verbose_name

    @property
    def name(self) -> str:
        """
        Filter name

        :return: The filter name
        :rtype: str
        """

        sp_threshold = humanize.intword(self.skill_point_threshold)

        skill_point_threshold = ngettext(
            singular=f"{sp_threshold} skill point",
            plural=f"{sp_threshold} skill points",
            number=self.skill_point_threshold,
        )

        return _(f"Member Audit Skill Points [{skill_point_threshold}]")

    def process_filter(self, user: User) -> bool:
        """
        Process the filter

        :param user: The user
        :type user: User
        :return: Return True when filter applies to the user, else False.
        :rtype: bool
        """

        return (
            Character.objects.owned_by_user(user=user)
            .filter(skillpoints__total__gt=self.skill_point_threshold)
            .count()
            > 0
        )

    def audit_filter(self, users) -> dict:
        """
        Audit Filter

        :param users: The users
        :type users: models.QuerySet[User]
        :return: The audit information
        :rtype: dict
        """

        output = defaultdict(lambda: {"message": "", "check": False})

        for user in users:
            characters = Character.objects.owned_by_user(user=user).filter(
                skillpoints__total__gt=self.skill_point_threshold
            )

            if characters.count() > 0:
                chars = defaultdict(list)

                for char in characters:
                    chars[char.user.pk].append(char.eve_character.character_name)

                for char_user, char_list in chars.items():
                    output[char_user] = {
                        "message": ", ".join(sorted(char_list)),
                        "check": True,
                    }

        return output


class SkillSetFilter(BaseFilter):
    """
    SkillSetFilter
    """

    class CharacterType(models.TextChoices):
        """
        A character type.
        """

        ANY = "AN", _("Any")
        MAINS_ONLY = "MO", _("Mains only")
        ALTS_ONLY = "AO", _("Alts only")

    skill_sets = models.ManyToManyField(
        to=SkillSet,
        help_text=_(
            "Users must have a character who possess all of the skills in "
            "<strong>one</strong> of the selected skill sets."
        ),
    )
    character_type = models.CharField(
        max_length=2,
        choices=CharacterType.choices,
        default=CharacterType.ANY,
        blank=True,
        help_text=_("Specify the type of character that needs to have the skill set."),
    )

    class Meta:
        """
        Model meta definitions
        """

        verbose_name = _("Smart Filter: Skill Set")
        verbose_name_plural = verbose_name

    def save(
        self,
        force_insert=False,  # pylint: disable=unused-argument
        force_update=False,  # pylint: disable=unused-argument
        using=None,  # pylint: disable=unused-argument
        update_fields=None,  # pylint: disable=unused-argument
    ):
        """
        Save the model instance.

        :param force_insert: Force insert
        :type force_insert: bool
        :param force_update: Force update
        :type force_update: bool
        :param using: Using
        :type using: str
        :param update_fields: Update fields
        :type update_fields: list
        :return: None
        :rtype: None
        """

        # Make sure a character_type is set
        if self.character_type == "":
            self.character_type = self.CharacterType.ANY

        super().save()

    @property
    def name(self) -> str:
        """
        Return name of this filter.

        :return: The filter name
        :rtype: str
        """

        return _("Member Audit Skill Set")

    def process_filter(self, user: User) -> bool:
        """
        Process the filter

        :param user: The user
        :type user: User
        :return: Return True when filter applies to the user, else False.
        :rtype: bool
        """

        qs = CharacterSkillSetCheck.objects.filter(
            character__eve_character__character_ownership__user=user,
            skill_set__in=list(self.skill_sets.all()),
            failed_required_skills__isnull=True,
        )

        if self.character_type == self.CharacterType.MAINS_ONLY:
            qs = qs.filter(character__eve_character__userprofile__isnull=False)
        elif self.character_type == self.CharacterType.ALTS_ONLY:
            qs = qs.filter(character__eve_character__userprofile__isnull=True)

        return qs.exists()

    def audit_filter(self, users) -> dict:
        """
        Audit Filter

        :param users: The users
        :type users: models.QuerySet[User]
        :return: The audit information
        :rtype: dict
        """

        qs = Character.objects.filter(
            skill_set_checks__skill_set__in=list(self.skill_sets.all()),
            skill_set_checks__failed_required_skills__isnull=True,
        )

        if self.character_type == self.CharacterType.MAINS_ONLY:
            qs = qs.filter(eve_character__userprofile__isnull=False)
        elif self.character_type == self.CharacterType.ALTS_ONLY:
            qs = qs.filter(eve_character__userprofile__isnull=True)

        matching_characters = qs.values(
            user_id=F("eve_character__character_ownership__user_id"),
            character_name=F("eve_character__character_name"),
        )

        user_with_characters = defaultdict(list)

        for user_id in matching_characters:
            character_name = user_id["character_name"]
            user_with_characters[user_id["user_id"]].append(f"{character_name}")

        output = {
            user_id: {"message": _("No matching character found"), "check": False}
            for user_id in users.values_list("id", flat=True)
        }

        for user_id, character_names in user_with_characters.items():
            output[user_id] = {
                "message": ", ".join(sorted(character_names)),
                "check": True,
            }

        return output


class TimeInCorporationFilter(BaseFilter):
    """
    Filter for time in a corporation.
    """

    minimum_days = models.PositiveIntegerField(
        default=30,
        help_text=_(
            "Minimum number of days a main character needs to be member "
            "of his/her current corporation."
        ),
    )

    reversed_logic = models.BooleanField(
        default=False,
        help_text=_(
            "If set, all members with LESS than the minimum days will pass this check."
        ),
    )

    class Meta:
        """
        Model meta definitions
        """

        verbose_name = _("Smart Filter: Time in Corporation")
        verbose_name_plural = verbose_name

    @property
    def name(self) -> str:
        """
        Return name of this filter.

        :return: The filter name
        :rtype: str
        """

        return _("Member Audit Time in Corporation Filter")

    def process_filter(self, user: User) -> bool:
        """
        Process the filter

        :param user: The user
        :type user: User
        :return: Return True when filter applies to the user, else False.
        :rtype: bool
        """

        try:
            character = user.profile.main_character.memberaudit_character
        except (ObjectDoesNotExist, AttributeError):
            return False

        history = (
            character.corporation_history.exclude(is_deleted=True)
            .order_by("-record_id")
            .first()
        )

        if not history:
            return False

        passes = (
            (now() - history.start_date).days < self.minimum_days
            if self.reversed_logic
            else (now() - history.start_date).days >= self.minimum_days
        )

        return passes

    def audit_filter(self, users) -> dict:
        """
        Audit Filter

        :param users: The users
        :type users: models.QuerySet[User]
        :return: The audit information
        :rtype: dict
        """

        current_membership = (
            CharacterCorporationHistory.objects.filter(
                character=OuterRef("profile__main_character__memberaudit_character__pk")
            )
            .exclude(is_deleted=True)
            .order_by("-record_id")
        )
        users_days_in_corporation = users.annotate(
            start_date=Subquery(current_membership.values("start_date")[:1])
        )

        output = defaultdict(lambda: {"message": "", "check": False})

        for user in users_days_in_corporation:
            if not user.start_date:
                check = False
                msg = _("No audit information found")
            else:
                days_in_corporation = (now() - user.start_date).days
                check = (
                    days_in_corporation < self.minimum_days
                    if self.reversed_logic
                    else days_in_corporation >= self.minimum_days
                )
                end_date = localize(
                    (
                        user.start_date + datetime.timedelta(days=self.minimum_days)
                    ).date()
                )
                msg = (
                    ngettext(
                        singular=f"{days_in_corporation:d} day",
                        plural=f"{days_in_corporation:d} days",
                        number=days_in_corporation,
                    )
                    if not self.reversed_logic
                    else ngettext(
                        singular=f"{days_in_corporation:d} day (End date: {end_date})",
                        plural=f"{days_in_corporation:d} days (End date: {end_date})",
                        number=days_in_corporation,
                    )
                )

            output[user.id] = {"message": msg, "check": check}

        return output
