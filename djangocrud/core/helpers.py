# helpers
from django.apps import apps
from django.forms.models import modelform_factory

from djangocrud.core.constants import MODEL_FORM_FIELDS


def get_errors(form_errors):
    error_list = []
    errors = form_errors.as_data().copy()
    [error_list.append(e + ': ' + \
        str(errors[e][0][0])) for e in errors]

    return list(set(error_list))


def get_model_name(**kwargs):
    return kwargs.get('model_name', None)


def get_model(**kwargs):
    model = 'core.' + kwargs.get('model_name', None)
    return apps.get_model(*model.split('.'))


def get_model_instance(**kwargs):
    return get_model(**kwargs).objects.get(id=kwargs.get("pk"))


def get_form_instance(**kwargs):
    return modelform_factory(
        get_model(**kwargs),
        fields=MODEL_FORM_FIELDS[get_model_name(**kwargs)])
