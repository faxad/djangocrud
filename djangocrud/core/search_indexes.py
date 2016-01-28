"""Haystack search index configuration.
This must be kept in sync with the models"""

from haystack import indexes
from djangocrud.core.models import Supplier


class SupplierIndex(indexes.SearchIndex, indexes.Indexable):
    """Indexing configuration for Supplier"""
    text = indexes.CharField(document=True, use_template=True)
    name = indexes.CharField(model_attr='name')
    remarks = indexes.CharField(model_attr='remarks')

    def get_model(self):
        return Supplier

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()
