from django.shortcuts import render, get_object_or_404

from .models import Car
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
# Create your views here.


def cars(request):
    cars = Car.objects.order_by('-created_date')
    paginator = Paginator(cars, 4)  # 3 items to display per page
    page = request.GET.get('page')
    paged_cars = paginator.get_page(page)
    context = {
        # 'cars': cars,
        'cars': paged_cars

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
