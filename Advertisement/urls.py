from django.urls import path
from .import views

urlpatterns = [
    path('list/', views.list_ads, name='list_ads'),
    path('manage/', views.manage_ads, name='manage_ads'),

]