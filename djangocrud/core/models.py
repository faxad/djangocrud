"""Model definition for CRUD operations"""

from django.db.models import (
    Model,
    CharField,
    DateTimeField,
    TextField)

from djangocrud.core.mixins import BaseEntityMixin
from djangocrud.core.validators import validate_name


class AbstractEntity(Model):
    """Common properties for all models"""
    creation_date = DateTimeField('Creation Date', auto_now_add=True)
    last_updated = DateTimeField('Last Updated', auto_now=True)

    @property
    def class_meta(self):
        """Returns class meta"""
        return self._meta

    def __unicode__(self):
        """Returns ID"""
        return self.id

    class Meta:
        abstract = True


class Supplier(AbstractEntity, BaseEntityMixin):
    """Sample representation of Supplier"""
    name = CharField("Name", max_length=200, validators=[validate_name])
    category = CharField(verbose_name="Category/Type", max_length=10, choices=(
        ('PB', 'Public'), ('PR', 'Private')))
    remarks = TextField("Remarks", blank=True)

    def clean(self):
        """Custom validation logic should go here"""
        pass
