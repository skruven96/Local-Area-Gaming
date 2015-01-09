from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from Tournaments.models import Game, Team
from Seats.models import Ticket


@csrf_exempt
def home(request):
    context = {
        'authenticated': request.user.is_authenticated()
    }

    if request.is_ajax():
        return render(request, 'home.html', context)
    else:
        context['page'] = 'home'
        return render(request, 'navbar.html', context)


@csrf_exempt
def seats(request):
    payed_seats = []
    your_seat = None

    for ticket in Ticket.objects.all():
        if ticket.position is not None:
            if ticket.owned_by == request.user:
                your_seat = ticket.position.str_id
            else:
                payed_seats.append(ticket.position.str_id)

    context = {
        'authenticated': request.user.is_authenticated(),
        'payed_seats': payed_seats,
        'your_seat': your_seat,

        'tickets': Ticket.objects.filter(owned_by=request.user)
    }

    if context['authenticated']:
        context['tickets'] = Ticket.objects.filter(owned_by=request.user)

    if request.is_ajax():
        return render(request, 'seats.html', context)
    else:
        context['page'] = 'seats'
        return render(request, 'navbar.html', context)


@csrf_exempt
def tournaments(request):
    context = {
        'authenticated': request.user.is_authenticated(),
        'games': Game.objects.all()
    }

    if request.is_ajax():
        return render(request, 'tournaments.html', context)
    else:
        context['page'] = 'tournaments'
        return render(request, 'navbar.html', context)


@csrf_exempt
def mypages(request):
    context = {
        'authenticated': request.user.is_authenticated(),
        'tickets': Ticket.objects.filter(owned_by=request.user),
        'teams': [],

        'username': request.user.username
    }

    if request.is_ajax():
        return render(request, 'mypages.html', context)
    else:
        context['page'] = 'mypages'
        return render(request, 'navbar.html', context)


@csrf_exempt
def login(request):
    context = {
        'authenticated': request.user.is_authenticated()
    }

    if request.is_ajax():
        return render(request, 'login.html', context)
    else:
        context['page'] = 'login'
        return render(request, 'navbar.html', context)

