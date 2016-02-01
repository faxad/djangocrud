"""Command to create view permission for all models"""

from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.core.management.base import BaseCommand

from djangocrud.core.helpers import get_all_models


class Command(BaseCommand):
    """Command to configure permission"""
    help = 'Configures the permissions for models'

    def handle(self, *args, **options):
        """Creates view_<model_name> permission"""
        for model in get_all_models():
            content_type = ContentType.objects.get_for_model(model)
            model_name = model.__name__.lower()
            Permission.objects.get_or_create(
                codename='view_{0}'.format(model_name),
                name='Can view {0}'.format(model_name),
                content_type=content_type)

        self.stdout.write(
            self.style.SUCCESS('Successfully configured permissions'))
