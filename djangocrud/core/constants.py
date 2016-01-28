"""Core CRUD configuration/constants"""

from collections import OrderedDict as odict


CRUD_OPERATIONS = {
    'create': 'add',
    'update': 'change',
    'delete': 'delete',
    'list': 'view',
    'detail': 'view'
    }

# model fields to diplay on the form

FIELD_CONFIG = odict([
    ('Supplier', odict([
        ('name', ['create', 'update', 'display', 'preview']),
        ('category', ['create', 'update', 'display']),
        ('remarks', ['create', 'update', 'display', 'preview']),
        ('creation_date', ['display']),
        ('last_updated', ['display'])
    ])),
])
