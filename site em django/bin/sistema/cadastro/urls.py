from django.urls import path
from . import views

urlpatterns = (
    path('',views.index,name='index'),
    path('pessoas',views.list_pessoas,name='list_pessoas'),

)