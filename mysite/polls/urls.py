from django.conf.urls import url

from .import views

urlpatterns = [
    # url('', views.index, name='index'),
    url('', views.digit_recognize, name='digit_recognize'),
]