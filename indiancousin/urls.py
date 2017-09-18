from django.conf.urls import url, include
from . import views

app_name='indiancousin'
urlpatterns = [
    #indiancousin/
    url(r'^$',views.IndexView.as_view(),name='index'),
    #indiancousin/21/
    url(r'^(?P<pk>[0-9]+)/',views.DetailView.as_view(),name='detail'),


]