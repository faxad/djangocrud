from django.db.models import (
    Model,
    CharField,
    DateTimeField,
    TextField)

from djangocrud.core.mixins import BaseEntityMixin
from djangocrud.core.validators import *


class AbstractEntity(Model):
    creation_date = DateTimeField('creation date', auto_now_add=True)
    last_updated = DateTimeField('last updated', auto_now=True)

    class Meta:
        abstract = True


class Supplier(AbstractEntity, BaseEntityMixin):
    name = CharField(max_length=200, validators=[validate_name])
    category = CharField(max_length=10, choices=(
        ('PB', 'Public'), ('PR', 'Private')))
    remarks = TextField(blank=True, null=True)

    def __unicode__(self):
        return self.name

    def clean(self):
        """Custom validation logic should go here"""
        pass
