from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^all$', views.post_list_all, name='post_list_all'),
    url(r'^archived$', views.post_list_archived, name='post_list_archived'),
]
