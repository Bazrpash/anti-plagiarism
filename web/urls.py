from django.urls import path

from . import views

urlpatterns = [
    path('submit', views.submit, name='submit'),
    path('validate/<str:user_id>', views.validate, name='validate'),
    path('index/<int:is_verified>', views.index, name='index'),
    path('', views.index, name='index'),
]
