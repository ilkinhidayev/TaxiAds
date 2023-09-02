from django.urls import path
from .import views

urlpatterns = [
    path('list/', views.list_ads, name='list_ads'),
    path('edit/<int:ad_id>/', views.edit_ad, name='edit_ad'),
    path('manage/', views.manage_ads, name='manage_ads'),
]