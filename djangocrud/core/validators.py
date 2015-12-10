from django.core.exceptions import ValidationError

# Custom validators goes here.


def validate_name(value):
    if not value[0].isupper():
        raise ValidationError('First character should be capital')
