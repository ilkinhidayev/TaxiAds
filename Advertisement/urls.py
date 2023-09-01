from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('list/', views.list_ads, name='list_ads'),
    path('edit/<int:ad_id>/', views.edit_ad, name='edit_ad'),
    path('manage/', views.manage_ads, name='manage_ads'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)