from django import template

from djangocrud.core.constants import FIELD_DISPLAY_CONFIG

register = template.Library()


@register.filter(is_safe=True)
def label_with_class(value, arg):
    return value.label_tag(attrs={'class': arg})


@register.assignment_tag(takes_context=True)
def model_field_values(context, option):
    field_value = {}

    if 'objects' in context:
        instance = context['objects'][0]
    elif 'object' in context:
        instance = context['object']

    model = type(instance)

    for field in model._meta.fields:
        field_name = field.verbose_name
        field_config = FIELD_DISPLAY_CONFIG[model.__name__]
        if field_name in field_config and option in field_config[field_name]:

            field_value[field_name] = getattr(
                instance, field.name)

    return field_value


@register.assignment_tag(takes_context=True)
def entity_preview(context):
    _parent = {}
    instances = context['objects']
    model = type(instances[0])

    for instance in instances:
        _child = {}
        for field in model._meta.fields:
            field_config = FIELD_DISPLAY_CONFIG[model.__name__]
            if field.name in field_config and 'preview' in field_config[field.name]:
                _child[field.name] = getattr(
                    instance, field.name)

        _parent[instance.id] = _child

    return _parent
