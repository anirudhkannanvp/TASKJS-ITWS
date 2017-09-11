from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^display/$', views.new_disp, name="new_disp"),
    url(r'^display/(?P<sensor1>[0-9]+.[0-9]+)/(?P<sensor2>[0-9]+.?[0-9]*)/$',views.Display,name="Display"),
]