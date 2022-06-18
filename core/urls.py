from django.urls import path

from core.views import index, create_tech, create_request

urlpatterns = [
    path('', index, name='mainpage'),
    path('create_tech/', create_tech, name='create_tech'),
    path('create_request/',create_request,name='create_request')
]
