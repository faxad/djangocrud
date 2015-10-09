from django import template

from djangocrud.core.constants import FIELD_CONFIG

register = template.Library()


def get_entity_data(instance, model, option):
    field_value = {}

    for field in model._meta.fields:
        field_config = FIELD_CONFIG[model.__name__]
        name = field.name
        if name in field_config and option in field_config[name]:
            field_value[name] = getattr(
                instance, name)

    return field_value


@register.filter(is_safe=True)
def label_with_class(value, arg):
    return value.label_tag(attrs={'class': arg})


@register.assignment_tag(takes_context=True)
def model_field_values(context, option):
    instance = context['object']
    model = type(instance)

    return get_entity_data(instance, model, option)


@register.assignment_tag(takes_context=True)
def entity_preview(context):
    _parent = {}
    instances = context['objects']
    model = type(instances[0])

    for instance in instances:
        _parent[instance.id] = get_entity_data(
            instance, model, 'preview')

    return _parent


@register.assignment_tag
def entity_type(object):
    return type(object).__name__
