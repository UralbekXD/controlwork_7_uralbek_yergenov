from django.shortcuts import render

from .models import GuestBook


def index(request):
    records = GuestBook.objects.exclude(status='blocked')
    return render(request, 'guestbook/index.html', context={
        'records': records.order_by('-created_at')
    })
