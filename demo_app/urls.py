from django.contrib import admin
from django.urls import path, include

from demo_app import views

urlpatterns = [
    path("",views.dash,name='test'),
    path("home",views.home,name='test1'),
    path("forms",views.forms,name='test2'),
    path("child",views.data,name='test3'),
    path('delete/<int:id>/',views.delete_1,name='delete'),
    path('update/<int:id>/',views.update_1,name='update'),


]
