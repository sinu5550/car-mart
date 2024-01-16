from django.shortcuts import render
from car.models import Car
from brand.models import Brand

def home(request,brand_slug = None):
    data = Car.objects.all()
    if brand_slug is not None:
        brand = Brand.objects.get(slug = brand_slug)
        data = Car.objects.filter(brand  = brand)
    brands = Brand.objects.all()
    return render(request, 'home.html', {'car' : data, 'brand' : brands})