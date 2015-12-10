class BaseEntityMixin(object):
    """Properties and methods that apply to all
    models defined under core
    """
    @property
    def title(self):
        return self.__class__.__name__
