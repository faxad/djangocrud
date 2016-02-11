"""Helpers"""

import inspect

from django.apps import apps
from django.forms.models import modelform_factory

from djangocrud.core.constants import FIELD_CONFIG


def get_errors(form_errors):
    """Returns compiled form errors"""
    error_list = []
    errors = form_errors.as_data().copy()
    errors = [error_list.append(
        e + ': ' + str(
            list(errors[e][0])[0])) for e in errors]

    return list(set(errors))


def get_all_models():
    """Returns all models"""
    return apps.get_app_config('core').models


def get_model_name(request=None, **kwargs):
    """Returns the name of model"""
    return kwargs.get(
        'model_name', request.path.split('/')[1] if request else None)


def get_model(**kwargs):
    """Returns model"""
    model = 'core.' + get_model_name(**kwargs)
    return apps.get_model(*model.split('.'))


def get_model_instance(**kwargs):
    """Returns model instance"""
    return get_model(**kwargs).objects.get(id=kwargs.get("pk"))


def get_form_instance(**kwargs):
    """Returns form instance"""
    fields = []
    field_config = FIELD_CONFIG[get_model_name(**kwargs)]
    callee = type(inspect.currentframe().f_back.f_locals['self']).__name__
    operation = 'create' if 'Create' in callee else 'update'

    for field in field_config:
        if operation in field_config[field]:
            fields.append(field)

    return modelform_factory(get_model(**kwargs), fields=fields)
