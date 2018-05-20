from django.conf.urls import url

from CRUD_FBVs import views

app_name = 'CRUD_FBVs'

urlpatterns = [
  url(r'^$', views.movies_list, name='movies_list'),
  url(r'^new$', views.movies_create, name='movies_new'),
  url(r'^edit/(?P<pk>\d+)$', views.movies_update, name='movies_edit'),
  url(r'^delete/(?P<pk>\d+)$', views.movies_delete, name='movies_delete'),
]
