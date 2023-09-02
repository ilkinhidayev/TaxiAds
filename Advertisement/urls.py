from django.urls import path
from .import views

urlpatterns = [
    path('list/', views.list_ads, name='list_ads'),
    path('manage/', views.manage_ads, name='manage_ads'),
    path('edit/<int:ad_id>/', views.edit_ad, name='edit_ad'),
    path('show/', views.show_ads, name='show_ads'),
    path('filter_by_location/', views.filter_by_location, name='filter_by_location'),

]