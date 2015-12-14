from djangocrud.core.helpers import get_model_name


def global_context(request):
    return {'entity_title': get_model_name(request)}
