"""
Admin pages
"""

# Standard Library
from typing import Any

# Third Party
import humanize

# Django
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http.request import HttpRequest
from django.utils.translation import gettext_lazy as _
from django.utils.translation import ngettext

# Member Audit
from memberaudit.models import CharacterRole

# Memberaudit Securegroups
from memberaudit_securegroups.models import (
    ActivityFilter,
    AgeFilter,
    AssetFilter,
    ComplianceFilter,
    CorporationRoleFilter,
    CorporationTitleFilter,
    SkillPointFilter,
    SkillSetFilter,
    TimeInCorporationFilter,
)


@admin.register(ActivityFilter)
class ActivityFilterAdmin(admin.ModelAdmin):
    """
    ActivityFilterAdmin
    """

    list_display = ("description", "_inactivity_threshold")

    def _inactivity_threshold(self, obj) -> str:
        """
        Get the inactivity threshold

        :param obj: The object
        :type obj: ActivityFilter
        :return: The inactivity threshold
        :rtype: str
        """

        inactivity_threshold = obj.inactivity_threshold

        return_value = ngettext(
            singular=f"{inactivity_threshold:d} day",
            plural=f"{inactivity_threshold:d} days",
            number=inactivity_threshold,
        )

        return return_value


@admin.register(AgeFilter)
class AgeFilterAdmin(admin.ModelAdmin):
    """
    AgeFilterAdmin
    """

    list_display = ("description", "_age_threshold")

    def _age_threshold(self, obj) -> str:
        """
        Get the age threshold

        :param obj: The object
        :type obj: AgeFilter
        :return: The age threshold
        :rtype: str
        """

        return f"{obj.age_threshold:d} days"


@admin.register(AssetFilter)
class AssetFilterAdmin(admin.ModelAdmin):
    """
    AssetFilterAdmin
    """

    list_display = ("description", "_assets")
    autocomplete_fields = ["assets"]

    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        """
        Get the queryset

        :param request: The request
        :type request: HttpRequest
        :return: The queryset
        :rtype: QuerySet
        """

        qs = super().get_queryset(request)

        return qs.prefetch_related("assets")

    @admin.display()
    def _assets(self, obj) -> str:
        """
        Get assets

        :param obj: The object
        :type obj: AssetFilter
        :return: The assets
        :rtype: str
        """

        objs = obj.assets.all()

        return ", ".join(sorted([obj.name for obj in objs]))


@admin.register(ComplianceFilter)
class ComplianceFilterAdmin(admin.ModelAdmin):
    """
    ComplianceFilterAdmin
    """

    list_display = ("description", "reversed_logic")


class CorporationRoleListFilter(admin.SimpleListFilter):
    """
    CorporationRoleListFilter
    """

    title = _("corporation role")
    parameter_name = "corporation_role"

    def lookups(self, request, model_admin) -> list:
        """
        Return lookups with used roles only.

        :param request: The request
        :type request: HttpRequest
        :param model_admin: The model admin
        :type model_admin: admin.ModelAdmin
        :return: The lookups
        :rtype: list
        """

        roles = set(model_admin.get_queryset(request).values_list("role", flat=True))
        result = [(role, CharacterRole.Role(role).label) for role in roles]

        return sorted(result, key=lambda o: o[1])

    def queryset(
        self, request, queryset  # pylint: disable=unused-argument
    ) -> QuerySet | None:
        """
        Return queryset for a selected role.

        :param request: The request
        :type request: HttpRequest
        :param queryset: The queryset
        :type queryset: QuerySet
        :return: The queryset
        :rtype: QuerySet
        """

        if value := self.value():
            return queryset.filter(role=value)

        return None


@admin.register(CorporationRoleFilter)
class CorporationRoleFilterAdmin(admin.ModelAdmin):
    """
    CorporationRoleFilterAdmin
    """

    list_display = ("description", "role", "_corporations")
    list_filter = (CorporationRoleListFilter,)
    filter_horizontal = ("corporations",)
    fields = ("description", "role", "corporations", "include_alts")

    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        """
        Get the queryset

        :param request: The request
        :type request: HttpRequest
        :return: The queryset
        :rtype: QuerySet
        """

        qs = super().get_queryset(request)

        return qs.prefetch_related("corporations")

    @admin.display()
    def _corporations(self, obj) -> str:
        """
        Get corporations

        :param obj: The object
        :type obj: CorporationRoleFilter
        :return: The corporations
        :rtype: str
        """

        objs = obj.corporations.all()

        return ", ".join(sorted([obj.corporation_name for obj in objs]))


@admin.register(CorporationTitleFilter)
class CorporationTitleFilterAdmin(admin.ModelAdmin):
    """
    CorporationTitleFilterAdmin
    """

    list_display = ("description", "title", "_corporations")
    filter_horizontal = ("corporations",)
    fields = ("description", "title", "corporations", "include_alts")

    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        """
        Get the queryset

        :param request: The request
        :type request: HttpRequest
        :return: The queryset
        :rtype: QuerySet
        """

        qs = super().get_queryset(request)

        return qs.prefetch_related("corporations")

    @admin.display()
    def _corporations(self, obj) -> str:
        """
        Get corporations

        :param obj: The object
        :type obj: CorporationTitleFilter
        :return: The corporations
        :rtype: str
        """

        objs = obj.corporations.all()

        return ", ".join(sorted([obj.corporation_name for obj in objs]))


@admin.register(SkillPointFilter)
class SkillPointFilterAdmin(admin.ModelAdmin):
    """
    SkillPointFilterAdmin
    """

    list_display = ("description", "_skill_point_threshold")

    def _skill_point_threshold(self, obj) -> str:
        """
        Get the skill point threshold

        :param obj: The object
        :type obj: SkillPointFilter
        :return: The skill point threshold
        :rtype:
        """

        skillpoints = humanize.intword(obj.skill_point_threshold)

        return f"{skillpoints} skill points"


@admin.register(SkillSetFilter)
class SkillSetFilterAdmin(admin.ModelAdmin):
    """
    SkillSetFilterAdmin
    """

    list_display = ("description", "_skill_sets", "character_type")
    filter_horizontal = ("skill_sets",)

    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        """
        Get the queryset

        :param request: The request
        :type request: HttpRequest
        :return: The queryset
        :rtype: QuerySet
        """

        qs = super().get_queryset(request)

        return qs.prefetch_related("skill_sets")

    @admin.display()
    def _skill_sets(self, obj) -> str:
        """
        Get skill sets

        :param obj: The object
        :type obj: SkillSetFilter
        :return: The skill sets
        :rtype: str
        """

        objs = obj.skill_sets.all()

        return ", ".join(sorted([obj.name for obj in objs]))


@admin.register(TimeInCorporationFilter)
class TimeInCorporationFilterAdmin(admin.ModelAdmin):
    """
    TimeInCorporationFilterAdmin
    """

    list_display = ("description", "minimum_days")
