from django.apps import apps
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

from djangocrud.core.models import *


class Command(BaseCommand):
    help = 'Configures the permissions for models'

    def handle(self, *args, **options):
        for m in apps.get_app_config('core').get_models():
            content_type = ContentType.objects.get_for_model(m)
            Permission.objects.get_or_create(
                codename='view_{0}'.format(m.__name__.lower()),
                name='Can view {0}'.format(m.__name__.lower()),
                content_type=content_type
                )

        self.stdout.write(self.style.SUCCESS('Successfully configured permissions'))
