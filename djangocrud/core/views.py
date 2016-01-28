"""Generic views for CRUD operations"""

from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.views import generic

from djangocrud.core.helpers import (
    get_errors,
    get_model,
    get_model_instance,
    get_form_instance,
    get_all_models
)

from djangocrud.core.mixins import AuthMixin


@login_required
def index(request):
    """Discovers models available for CRUD operations"""
    return render(
        request,
        'index.html',
        {'models': get_all_models().values()})


class EntityList(AuthMixin, generic.ListView):
    """Generic view for List/Display operation"""
    template_name = 'core/index.html'
    context_object_name = 'objects'

    def dispatch(self, request, *args, **kwargs):
        """Overriding dispatch on ListView"""
        self.model = get_model(**kwargs)
        queryset = self.model.objects.all()

        return super(EntityList, self).dispatch(
            request, *args, **kwargs)


class EntityDetail(AuthMixin, generic.DetailView):
    """Generic view for Detail operation"""
    template_name = 'core/detail.html'

    def dispatch(self, request, *args, **kwargs):
        """Overriding dispatch on DetailView"""
        self.model = get_model(**kwargs)
        queryset = self.model.objects.get(id=kwargs.get("pk"))

        return super(EntityDetail, self).dispatch(
            request, *args, **kwargs)


class EntityDelete(AuthMixin, generic.DeleteView):
    """Generic view for Delete operation"""
    def dispatch(self, request, *args, **kwargs):
        """Overriding dispatch on DeleteView"""
        self.model = get_model(**kwargs)
        instance = get_model_instance(**kwargs)
        self.success_url = reverse_lazy('index', args=(instance.title,))

        return super(EntityDelete, self).dispatch(
            request, *args, **kwargs)


class EntityUpdate(AuthMixin, generic.View):
    """Generic view for Update operation"""
    def get(self, request, *args, **kwargs):
        """GET request handler for Update operation"""
        instance = get_model_instance(**kwargs)
        form = get_form_instance(**kwargs)
        context = {
            'form': form(instance=instance),
            'object': instance,
        }

        return render(request, 'core/update.html', context)

    def post(self, request, *args, **kwargs):
        """POST request handler for Update operation"""
        instance = get_model_instance(**kwargs)
        form = get_form_instance(
            **kwargs)(request.POST, instance=instance)

        if form.is_valid():
            form.save()

            return HttpResponseRedirect(
                reverse('index', args=(instance.title,)))
        else:
            context = {
                'form': form,
                'object': instance,
                'error_message': get_errors(form.errors)
            }

            return render_to_response(
                'core/update.html',
                context,
                context_instance=RequestContext(request))


class EntityCreate(AuthMixin, generic.View):
    """Generic view for Create operation"""
    def get(self, request, *args, **kwargs):
        """GET request handler for Create operation"""
        form = get_form_instance(**kwargs)
        context = {'form': form}

        return render(request, 'core/create.html', context)

    def post(self, request, *args, **kwargs):
        """POST request handler for Create operation"""
        model = get_model(**kwargs)
        form = get_form_instance(**kwargs)(request.POST)

        if form.is_valid():
            instance = model(**form.cleaned_data)
            instance.save()

            return HttpResponseRedirect(
                reverse('index', args=(instance.title,)))
        else:
            context = {
                'form': form,
                'error_message': get_errors(form.errors)
            }

            return render_to_response(
                'core/create.html',
                context,
                context_instance=RequestContext(request))
