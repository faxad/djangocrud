# helpers
import inspect

from django.apps import apps
from django.forms.models import modelform_factory

from djangocrud.core.constants import FIELD_CONFIG


def get_errors(form_errors):
    error_list = []
    errors = form_errors.as_data().copy()
    [error_list.append(
        e + ': ' + str(
            errors[e][0][0])) for e in errors]

    return list(set(error_list))


def get_model_name(**kwargs):
    return kwargs.get('model_name', None)


def get_model(**kwargs):
    model = 'core.' + get_model_name(**kwargs)
    return apps.get_model(*model.split('.'))


def get_model_instance(**kwargs):
    return get_model(**kwargs).objects.get(id=kwargs.get("pk"))


def get_form_instance(**kwargs):
    fields = []
    field_config = FIELD_CONFIG[get_model_name(**kwargs)]
    callee = type(inspect.currentframe().f_back.f_locals['self']).__name__
    operation = 'create' if 'Create' in callee else 'update'

    for field in field_config:
        if operation in field_config[field]:
            fields.append(field)

    return modelform_factory(get_model(**kwargs), fields=fields)
