from django.shortcuts import render
from .models import Ticket


def home(request):

    return render(request, 'ticketing/home.html')


def tickets(request):
    context = {
        'tickets': Ticket.objects.all(),
        'title': 'Issues'
    }
    return render(request, 'ticketing/tickets.html', context)
