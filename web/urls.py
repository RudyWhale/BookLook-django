from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('item/<int:id>', views.item, name='item')
]