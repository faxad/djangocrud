from django.db.models import (
    Q,
    Model,
    CharField,
    BooleanField,
    DateField,
    DateTimeField,
    TextField,
    IntegerField,
    EmailField,
    ForeignKey)


class Supplier(Model):
    name = CharField(max_length=200)
    creation_date = DateTimeField('joining date', auto_now_add=True)
    last_updated = DateTimeField('last updated', auto_now=True)
    remarks = TextField(blank=True, null=True)

    def __unicode__(self):
        return self.name

    @property
    def title(self):
        return self.__class__.__name__
