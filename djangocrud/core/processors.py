"""Common template processors"""

from djangocrud.core.helpers import get_model_name


def global_context(request):
    """Returns the title of the model"""
    return {'entity_title': get_model_name(request)}
