from django.conf.urls import url

from djangocrud.core.views import (
    EntityList,
    EntityDetail,
    EntityUpdate,
    EntityDelete,
    EntityCreate
)

urlpatterns = [
    url(r'^(?P<model_name>\w+)/List/$', EntityList.as_view(), name='index'),
    url(r'^(?P<model_name>\w+)/(?P<pk>\d+)/$', EntityDetail.as_view(), name='detail'),
    url(r'^(?P<model_name>\w+)/Delete/(?P<pk>\d+)$', EntityDelete.as_view(), name='delete'),
    url(r'^(?P<model_name>\w+)/Update/(?P<pk>\d+)/$', EntityUpdate.as_view(), name='update'),
    url(r'^(?P<model_name>\w+)/Create/$', EntityCreate.as_view(), name='create'),
]
