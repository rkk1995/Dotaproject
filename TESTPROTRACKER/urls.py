from django.urls import path

from . import views
app_name = 'TESTPROTRACKER'

urlpatterns = [
    path('', views.protrackertest, name='protrackertest'),
]