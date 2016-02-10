# djangoCRUD

[![Build Status](https://travis-ci.org/faxad/djangoCRUD.svg?branch=master)](https://travis-ci.org/faxad/djangoCRUD)
[![Coverage Status](https://coveralls.io/repos/github/faxad/djangoCRUD/badge.svg?branch=master)](https://coveralls.io/github/faxad/djangoCRUD?branch=master)
[![Codacy Badge](https://api.codacy.com/project/badge/grade/82d97392eecb4ffab85403390f6b25af)](https://www.codacy.com/app/fawadhq/djangoCRUD)
[![Code Issues](https://www.quantifiedcode.com/api/v1/project/2807a5b5bcdb46258ef0bcf7bb4e4d0f/badge.svg)](https://www.quantifiedcode.com/app/project/2807a5b5bcdb46258ef0bcf7bb4e4d0f)

### About
The intention was to develop a generic framework for rapid development of CRUD based web applications. The framework simplifies the development process by relying only on Model creation. The generic framework takes care of providing the necessary Views, Templates, Forms and URLs.

Additionally, a simple configuration allows the developer to specify what fields to display in Create, Update, Display and Preview operations.

### Technology Stack
- Python 2.7x, 3.x
- Django 1.9
- Bootstrap 3.x

### Usage

#### Step 1: Define Model
- Model definition should go under **core/models**
- All models must inherit from **AbstractEntity** combined with **BaseEntityMixin**
```sh
class Supplier(AbstractEntity, BaseEntityMixin):
    """Sample representation of Supplier"""
    name = CharField("Name", max_length=200, validators=[validate_name])
    category = CharField(verbose_name="Category/Type", max_length=10, choices=(
        ('PB', 'Public'), ('PR', 'Private')))
    remarks = TextField("Remarks", blank=True)

    def clean(self):
        """Custom validation logic should go here"""
        pass
```
#### Step 2: Define Validation Logic (Optional)
- Custom validation logic should go under **clean()** on the model itself
- Custom field specific validation should be defined in **core/validators** and applied to the field as **validators** attribute

#### Step 3: Configure Field Visibility
Nested Ordered Dictionary in core/constants must define the visbility of fields on the templates and forms.
- **create:** available on create form
- **update:** available on update form
- **display:** available for display in detail view
- **preview:** available for display in list view
```sh
FIELD_CONFIG = odict([
    ('Supplier', odict([
        ('name', ['create', 'update', 'display', 'preview']),
        ('category', ['create', 'update', 'display']),
        ('remarks', ['create', 'update', 'display', 'preview']),
        ('creation_date', ['display']),
        ('last_updated', ['display'])
    ])),
])
```
#### Step 4: Configure Search & Indexing (Optional)
For search to work, the Haystack configuration should be added under **core/search_indexes**

#### Step 5: Configure Permissions
To configure the permission, run the following management command
- ./manage.py configauth

### Who do I talk to? ###

* Fawad H Qureshi | <fawad@outlook.com>
