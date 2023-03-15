from django.urls import path
from .views import homed


urlpatterns = [

    path('/', homed),
]