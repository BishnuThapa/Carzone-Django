from django.shortcuts import render, get_object_or_404

from .models import Car

# Create your views here.


def cars(request):
    cars = Car.objects.order_by('-created_date')
    context = {
        'cars': cars,
    }
    return render(request, 'cars/cars.html', context)


def Nepal(request):
    return render(request, 'cars/nepal.html')


def car_detail(request, car_slug):
    single_car = get_object_or_404(Car, slug=car_slug)
    context = {
        'single_car': single_car
    }
    return render(request, 'cars/car_detail.html', context)
