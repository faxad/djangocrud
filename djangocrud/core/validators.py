"""Custom validation logic"""

from django.core.exceptions import ValidationError


def validate_name(value):
    """Sample validation"""
    if not value[0].isupper():
        raise ValidationError('First character should be capital')
