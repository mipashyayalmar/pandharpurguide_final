from django.shortcuts import render, redirect
from .models import Image, Advertisement
from .forms import ImageForm, AdvertisementForm  # Import the forms

# Home view
def home(request):
    # Fetch all images and enabled advertisements ordered by 'order'
    images = Image.objects.all()
    advertisements = Advertisement.objects.filter(status='enable').order_by('order')
    form = ImageForm()

    # Handle POST request for adding an image
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')

    # Render home template with data and form
    return render(request, 'puja/home.html', {
        'images': images,
        'advertisements': advertisements,
        'form': form
    })

# Advertisement view
def advertisement(request):
    form = AdvertisementForm()

    # Handle POST request for adding an advertisement
    if request.method == 'POST':
        form = AdvertisementForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('advertisement')

    # Render advertisement template with the form
    return render(request, 'advertisements/adverhome.html', {'form': form})
