from django.shortcuts import render
from .models import Ticket
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    context = {
        'tickets': Ticket.objects.all(),
        'title': 'Dashboard'
    }
    return render(request, 'ticketing/home.html', context)

@login_required
def tickets(request):
    context = {
        'tickets': Ticket.objects.all(),
        'title': 'Issues'
    }
    return render(request, 'ticketing/tickets.html', context)
