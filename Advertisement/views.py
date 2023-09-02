from django.shortcuts import render, redirect, get_object_or_404
from .forms import AdForm
from .models import Ad
from django.http import JsonResponse
from django.urls import reverse

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