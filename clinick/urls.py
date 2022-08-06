from django.urls import path
from .views import index

app_name = 'clinick'

urlpatterns = [
    path('', index, name='index'),
]
