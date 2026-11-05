
from django.shortcuts import render, redirect
from .models import Booking

def home(request):

    if request.method == "POST":

        name = request.POST.get('name')
        email = request.POST.get('email')
        date = request.POST.get('date')
        time_slot = request.POST.get('time_slot')

        if Booking.objects.filter(date=date, time_slot=time_slot).exists():
            return render(request, 'home.html', {
                'error': 'This time slot is already booked!'
            })

        Booking.objects.create(
            name=name,
            email=email,
            date=date,
            time_slot=time_slot
        )

        return redirect('success')

    return render(request, 'home.html')


def success(request):
    return render(request, 'success.html')

