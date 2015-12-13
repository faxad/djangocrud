from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import redirect


class BaseEntityMixin(object):
    """Properties and methods that apply to all
    models defined under core
    """
    @property
    def title(self):
        return self.__class__.__name__


class AuthMixin(UserPassesTestMixin):

    def test_func(self):
        return redirect('/Denied/')
