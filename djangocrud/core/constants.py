
# model fields to diplay on the form

MODEL_FORM_FIELDS = MODEL_DISPLAY_FIELDS = {
    'Supplier': ("name", "remarks")
}

# C: Create, U: Update, D: Display, P: Preview

FIELD_DISPLAY_CONFIG = {
    'Supplier': {
        'name': ['create', 'update', 'display', 'preview'],
        'remarks': ['create', 'update', 'display', 'preview']
    }
}
