from django.urls import path
from . import views

app_name = 'app1'

urlpatterns = [
    path('/v1', views.index, name='app1'),
    path('/v2', views.index, name='app2'),
]