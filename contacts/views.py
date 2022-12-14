from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact

from django.core.mail import send_mail
from django.contrib.auth.models import User
# Create your views here.


def inquiry(request):
    if request.method == "POST":
        car_slug = request.POST['car_slug']
        car_title = request.POST['car_title']
        user_id = request.POST['user_id']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        customer_need = request.POST['customer_need']
        city = request.POST['city']
        state = request.POST['state']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']

        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(user_id=user_id, car_slug=car_slug)
            if has_contacted:
                messages.error(
                    request, 'You have already made an inquiry about this car. Please wait until we get back to you.')
                return redirect('/cars/' + car_slug)

        contact = Contact(car_slug=car_slug, car_title=car_title, user_id=user_id,              first_name=first_name, last_name=last_name,
                          customer_need=customer_need, city=city, state=state, email=email, phone=phone, message=message)

        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email
        send_mail(
            'New car inquiry',
            'You have a new inquiry for the car.' + car_title +
            '. Please login to admin panel to for more info',
            'thapabishnu20@gmail.com',  # from user
            [admin_email],  # to user
            fail_silently=False,
        )
        contact.save()
        messages.success(
            request, 'Your request has been submitted, we will get back you shortly.')

        return redirect('/cars/'+car_slug)
