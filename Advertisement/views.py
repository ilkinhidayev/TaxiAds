from django.shortcuts import render, redirect, get_object_or_404
from .forms import AdForm
from .models import Ad
from django.http import JsonResponse
from django.urls import reverse
import math

def list_ads(request):
    ads = Ad.objects.all()
    return render(request, 'list_ads.html', {'ads': ads})

def edit_ad(request, ad_id):
    ad = get_object_or_404(Ad, id=ad_id)
    if request.method == 'POST':
        form = AdForm(request.POST, request.FILES, instance=ad)
        if form.is_valid():
            form.save()
            return redirect('manage_ads')
    else:
        form = AdForm(instance=ad)
    return render(request, 'edit_ad.html', {'form': form})

def delete_ad(request, ad_id):
    if request.method == 'POST':
        ad = get_object_or_404(Ad, id=ad_id)
        ad.delete()
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False, 'error': 'POST method required.'}, status=400)

def manage_ads(request):
    ads = Ad.objects.all()

    if request.method == 'POST':
        form = AdForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('manage_ads')

    else:
        form = AdForm()
    return render(request, 'manage_ads.html', {'form': form, 'ads': ads})

def show_ads(request):
    ads = Ad.objects.all()
    return render(request, 'show_ads.html', {'ads': ads})

def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance in kilometers between two points 
    on the earth (specified in decimal degrees)
    """
    lon1, lat1, lon2, lat2 = map(math.radians, [lon1, lat1, lon2, lat2])
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    r = 6371  # Earth radius in kilometers
    return c * r


def filter_by_location(request):
    if request.method == "POST":
        user_latitude = float(request.POST.get('latitude'))
        user_longitude = float(request.POST.get('longitude'))

        nearby_ads = []

        for ad in Ad.objects.all():
            distance = haversine(user_longitude, user_latitude, ad.longitude, ad.latitude)
            if distance <= ad.radius:
                nearby_ads.append({
                    'title': ad.title, 
                    'image': ad.image.url, 
                    'description': ad.description
                })

        return JsonResponse(nearby_ads, safe=False)
    return JsonResponse({'error': 'Invalid method'}, status=400)
