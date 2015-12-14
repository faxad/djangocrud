from django.contrib.auth.mixins import PermissionRequiredMixin


class BaseEntityMixin(object):
    """Properties and methods that apply to all
    models defined under core
    """
    @property
    def title(self):
        return self.__class__.__name__


class AuthMixin(PermissionRequiredMixin):
    def get_permission_required(self):
        print self
        return ['core.change_{0}'.format(
            self.request.path.split('/')[1].lower())]
