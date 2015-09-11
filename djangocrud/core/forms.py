from django import forms
from django.forms import ModelForm
from django.forms.models import BaseModelFormSet, modelformset_factory

from djangocrud.core.models import Supplier, ContactInfo


class SupplierForm(ModelForm):
    class Meta:
        model = Supplier
        fields = ['name', 'remarks']


class ContactInfoForm(ModelForm):
    class Meta:
        model = ContactInfo
        fields = ['contact_person', 'address', 'telephone', 'mobile', 'fax', 'email']


class BaseContactInfoFormSet(BaseModelFormSet):
    def __init__(self, *args, **kwargs):
        super(BaseContactInfoFormSet, self).__init__(*args, **kwargs)

        for form in self.forms:
            form.empty_permitted = False

    def clean(self):
        super(BaseContactInfoFormSet, self).clean()

        contact_person_names = []

        for form in self.forms:
            name = form.cleaned_data.get('contact_person')

            if name in contact_person_names and name is not None:
                raise forms.ValidationError(
                    "Duplicate contact person found!")

            contact_person_names.append(name)

    def get_forms_after_delete(self):
        for form in self.deleted_forms:
            self.forms.remove(form)

        data = {
            'form-TOTAL_FORMS': len(self.forms),
            'form-INITIAL_FORMS': '0',
            'form-MAX_NUM_FORMS': '',
        }

        for index, form in enumerate(self.forms):
            [form.cleaned_data.pop(key) for key in ('id', 'DELETE')]

            for key in form.cleaned_data:
                data["form-{}-{}".format(
                    str(index), key)] = form.cleaned_data.get(key)

        return data


ContactInfoFormSet = modelformset_factory(
    ContactInfo,
    form=ContactInfoForm,
    formset=BaseContactInfoFormSet,
    extra=1,
    can_delete=True
)

ContactInfoUpdateFormSet = modelformset_factory(
    ContactInfo,
    form=ContactInfoForm,
    formset=BaseContactInfoFormSet,
    extra=0,
    can_delete=True
)
