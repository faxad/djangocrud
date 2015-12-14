from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    PermissionRequiredMixin)

from djangocrud.core.constants import CRUD_OPERATIONS
from djangocrud.core.helpers import get_model_name


class BaseEntityMixin(object):
    """Properties and methods that apply to all
    models defined under core
    """
    @property
    def title(self):
        return self.__class__.__name__


class AuthMixin(LoginRequiredMixin, PermissionRequiredMixin):
    def get_permission_required(self):
        return ['core.{0}_{1}'.format(
            CRUD_OPERATIONS[self.__class__.__name__.replace(
                'Entity', '').lower()],
            get_model_name(request=self.request).lower())]
