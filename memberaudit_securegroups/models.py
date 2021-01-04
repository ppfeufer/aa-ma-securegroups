from django.contrib.auth.models import User
from django.core.cache import cache
from django.db import models

from allianceauth.authentication.models import CharacterOwnership


class SingletonModel(models.Model):
    class Meta:
        abstract = True

    def delete(self, *args, **kwargs):
        pass

    def set_cache(self):
        cache.set(self.__class__.__name__, self)

    def save(self, *args, **kwargs):
        self.pk = 1
        super(SingletonModel, self).save(*args, **kwargs)

        self.set_cache()

    @classmethod
    def load(cls):
        if cache.get(cls.__name__) is None:
            obj, created = cls.objects.get_or_create(pk=1)
            if not created:
                obj.set_cache()
        return cache.get(cls.__name__)


class BaseFilter(models.Model):

    description = models.CharField(max_length=500)  # this is what is shown to the user

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.name}: {self.description}"

    @property
    def name(self):
        return "Member Audit Compliance"

    def process_filter(
        self, user: User
    ):  # this is the check run against a users characters
        raise NotImplementedError("Please Create a filter!")


class MemberAuditComplianceFilter(BaseFilter, SingletonModel):
    def process_filter(self, user: User):
        return (
            CharacterOwnership.objects.filter(
                user=user, memberaudit_character=None
            ).count()
            == 0
        )
