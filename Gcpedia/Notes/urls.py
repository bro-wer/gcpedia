from django.conf.urls import *

from . import views

app_name='notes'

urlpatterns = [
    url(r"^$", views.HomePage.as_view(), name="home"),
]
