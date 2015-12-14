from django.apps import apps
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'Configures the permissions for models'

    def handle(self, *args, **options):
        for model in apps.get_app_config('core').get_models():
            content_type = ContentType.objects.get_for_model(model)
            model_name = model.__name__.lower()
            Permission.objects.get_or_create(
                codename='view_{0}'.format(model_name),
                name='Can view {0}'.format(model_name),
                content_type=content_type)

        self.stdout.write(
            self.style.SUCCESS('Successfully configured permissions'))
