from django.urls import path

from . import views

urlpatterns = [
    path('submit', views.submit, name='submit'),
    path('validate/<str:user_id>', views.validate, name='validate'),
    path('index/<int:status>', views.index, name='index'),
    path('NameList', views.name_list, name='name_list'),
    path('', views.index, name='index'),
]
