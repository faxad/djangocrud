from django import template

from djangocrud.core.constants import MODEL_DISPLAY_FIELDS

register = template.Library()


@register.filter(is_safe=True)
def label_with_class(value, arg):
    return value.label_tag(attrs={'class': arg})


@register.assignment_tag(takes_context=True)
def model_field_values(context):
    field_value = {}
    instance = context['object']
    model = type(instance)

    for field in model._meta.fields:
        field_name = field.verbose_name
        if field_name in MODEL_DISPLAY_FIELDS[model.__name__]:
            field_value[field_name] = getattr(
                instance, field.name)

    return field_value
