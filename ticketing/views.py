from django.shortcuts import render

tickets = [
    {
        'submitter': 'Jane Doe',
        'issue_id': '0231342342',
        'issue_description': 'Test issue 1',
        'date_identified': 'October 17, 2020',
        'due_date': 'October 20, 2020',
        'severity': 'major'
    },
    {
        'submitter': 'John Doe',
        'issue_id': '1234321223',
        'issue_description': 'Test issue 2',
        'date_identified': 'October 17, 2020',
        'due_date': 'October 20, 2020',
        'severity': 'minor'
    }
]


def home(request):
    context = {
        'tickets': tickets
    }
    return render(request, 'ticketing/home.html', context)


def tickets(request):
    context = {
        'title': 'Issues',
        'tickets': tickets
    }
    return render(request, 'ticketing/tickets.html', context)
