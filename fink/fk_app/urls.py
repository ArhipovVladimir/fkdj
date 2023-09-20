from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('add_proc/', views.add_process, name='add_process'),
    path('add_oper/', views.add_operation, name='add_operation'),
    path('add_sert/', views.add_sertif, name='add_sertif'),
    path('add_volat/', views.add_violation, name='add_volation'),
    path('reestr/', views.reestr, name='reestr'),
]