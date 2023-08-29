from django.shortcuts import render, redirect
from .forms import AdForm
from .models import Ad

def add_ad(request):
    if request.method == 'POST':
        form = AdForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('add_ad')
    else:
        form = AdForm()
    return render(request, 'add_ad.html', {'form': form})

def list_ads(request):
    ads = Ad.objects.all()
    return render(request, 'list_ads.html', {'ads': ads})

def edit_ad(request):
    ad = get_object_or_404(Ad, id=ad_id)
    if request.method == 'POST':
        form = AdForm(request.POST, request.FILES, instance=ad)
        if form.is_valid():
            form.save()
            return redirect('list_ads')
    else:
        form = AdForm(instance=ad)
    return render(request, 'edit_ad.html', {'form': form})