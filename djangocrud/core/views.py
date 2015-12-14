from django.apps import apps
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
from django.views import generic

from djangocrud.core.helpers import (
    get_errors,
    get_model,
    get_model_instance,
    get_form_instance
)

from djangocrud.core.mixins import AuthMixin


@login_required
def index(request):
    return render(
        request,
        'index.html',
        {'models': apps.get_app_config(
            'core').models.values()})


class EntityList(LoginRequiredMixin, generic.ListView):
    template_name = 'core/index.html'
    context_object_name = 'objects'

    def dispatch(self, request, *args, **kwargs):
        self.model = get_model(**kwargs)
        queryset = self.model.objects.all()

        return super(EntityList, self).dispatch(
            request, *args, **kwargs)


class EntityDetail(generic.DetailView):
    template_name = 'core/detail.html'

    def dispatch(self, request, *args, **kwargs):
        self.model = get_model(**kwargs)
        queryset = self.model.objects.get(id=kwargs.get("pk"))

        return super(EntityDetail, self).dispatch(
            request, *args, **kwargs)


class EntityDelete(AuthMixin, generic.DeleteView):

    def dispatch(self, request, *args, **kwargs):
        self.model = get_model(**kwargs)
        instance = get_model_instance(**kwargs)
        self.success_url = reverse_lazy('index', args=(instance.title,))

        return super(EntityDelete, self).dispatch(
            request, *args, **kwargs)


class EntityUpdate(AuthMixin, generic.View):

    def get(self, request, *args, **kwargs):
        instance = get_model_instance(**kwargs)
        form = get_form_instance(**kwargs)
        context = {
            'form': form(instance=instance),
            'object': instance,
        }

        return render(request, 'core/update.html', context)

    def post(self, request, *args, **kwargs):
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

    def get(self, request, *args, **kwargs):
        form = get_form_instance(**kwargs)
        context = {'form': form}

        return render(request, 'core/create.html', context)

    def post(self, request, *args, **kwargs):
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
