from django.shortcuts import render

# Create your views here.


def cars(request):
    return render(request, 'cars/cars.html')


def Nepal(request):
    return render(request, 'cars/nepal.html')
