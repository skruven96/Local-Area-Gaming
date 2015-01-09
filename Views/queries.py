from django.shortcuts import render
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User

import django.contrib.auth as auth
import random
import string

from Seats.models import Seat, Ticket


@csrf_exempt
def login(request):
    username = request.POST['username']
    password = request.POST['password']

    user = auth.authenticate(username=username, password=password)
    if user is not None:
        auth.login(request, user)
        return render(request, 'navbar.html', {'page': 'mypages', 'authenticated': True})
    else:
        print('Other')
        return HttpResponse('failure')


@csrf_exempt
def logout(request):
    auth.logout(request)
    return render(request, 'navbar.html', {'page': 'home', 'authenticated': False})


@csrf_exempt
def register(request):
    username = request.POST['username']
    password = request.POST['password']

    try:
        user = User.objects.get(username=username)
        return HttpResponse('error')
    except User.DoesNotExist:
        pass

    User.objects.create_user(username, request.POST['email'], password)

    user = auth.authenticate(username=username, password=password)
    auth.login(request, user)

    return render(request, 'navbar.html', {'page': 'home', 'authenticated': True})


@csrf_exempt
def pick_seat(request):
    seat = Seat.objects.get(str_id=request.POST['seat'])
    ticket = Ticket.objects.get(unique_str_id=request.POST['ticket'])

    if seat.owned_by is not None:
        return HttpResponse('seat not empty')
    elif ticket.owned_by != request.user:
        return HttpResponse('not your ticket')

    if ticket.position is not None:
        ticket.position.owned_by = None
        ticket.position.save()

    seat.owned_by = ticket
    ticket.position = seat

    seat.save()
    ticket.save()
    return HttpResponse('success')


@csrf_exempt
def order_ticket(request):
    ticket = Ticket(owned_by=request.user)
    chars = string.ascii_lowercase + string.ascii_uppercase + string.digits

    success = False
    while not success:
        success = True
        ticket.unique_str_id = ''.join(random.SystemRandom().choice(chars) for _ in range(10))

        for t in Ticket.objects.all():
            if t.unique_str_id == ticket.unique_str_id:
                success = False

    ticket.save()
    return HttpResponse('success')
