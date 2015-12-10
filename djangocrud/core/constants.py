from collections import OrderedDict as odict


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
