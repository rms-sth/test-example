from django.db import models
from django.utils.translation import gettext_lazy as _


class TimeStamp(models.Model):
    """General Abstract model that can inherited by other model which requires timestamp"""

    created_at = models.DateTimeField(
        _("Created Date"),
        auto_now_add=True,
        help_text=_("Eg. 2021-09-28T19:40:02.785988+05:45"),
    )
    updated_at = models.DateTimeField(
        _("Updated Date"),
        auto_now=True,
        help_text=_("Eg. 2021-09-28T19:40:02.785988+05:45"),
    )

    class Meta:
        abstract = True


class Position(TimeStamp):
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=100, unique=True)

    def __str__(self) -> str:
        return self.name


class Company(TimeStamp):
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=100, unique=True)
    address = models.TextField()

    def __str__(self) -> str:
        return self.name


class Person(TimeStamp):
    first_name = models.CharField(
        max_length=100,
        blank=True,
    )
    middle_name = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )
    last_name = models.CharField(
        max_length=150,
        blank=True,
    )
    dob = models.DateField(
        help_text=_("Eg. 2022-10-29"),
        null=True,
        blank=True,
    )
    positions = models.ManyToManyField(
        "PersonPositionInCompanyRelationship",
        related_name="persons",
    )
    # positions = models.ManyToManyField("PersonPosition")
    def __str__(self) -> str:
        return self.first_name


class PersonPositionInCompanyRelationship(TimeStamp):
    person = models.ForeignKey(
        "Person",
        related_name="person_positions",
        on_delete=models.CASCADE,
    )
    position = models.ForeignKey(
        "Position",
        related_name="person_positions",
        on_delete=models.CASCADE,
    )
    company = models.ForeignKey(
        "Company",
        related_name="person_positions",
        on_delete=models.CASCADE,
    )
