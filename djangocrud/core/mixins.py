from django.contrib.auth.mixins import PermissionRequiredMixin

from djangocrud.core.constants import CRUD_OPERATIONS


class BaseEntityMixin(object):
    """Properties and methods that apply to all
    models defined under core
    """
    @property
    def title(self):
        return self.__class__.__name__


class AuthMixin(PermissionRequiredMixin):
    def get_permission_required(self):
        return ['core.{0}_{1}'.format(
            CRUD_OPERATIONS[self.__class__.__name__.strip('Entity').lower()],
            self.request.path.split('/')[1].lower())]
