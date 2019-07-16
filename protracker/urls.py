from django.urls import path

from . import views
app_name = 'protracker'

urlpatterns = [
    path('', views.index, name='index'),
]