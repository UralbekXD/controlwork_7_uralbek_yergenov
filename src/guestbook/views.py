from django.shortcuts import render, redirect

from .models import GuestBook
from .forms import RecordForm


def index(request):
    records = GuestBook.objects.exclude(status='blocked')
    return render(request, 'guestbook/index.html', context={
        'records': records.order_by('-created_at')
    })


def add_record(request):
    match request.method:
        case 'GET':
            form = RecordForm()
            return render(request, 'guestbook/create.html', context={
                'form': form,
            })

        case 'POST':
            form = RecordForm(request.POST)
            if not form.is_valid():
                return render(request, 'guestbook/create.html', context={
                    'form': form,
                })

            # SUCCESS
            GuestBook.objects.create(
                author=form.cleaned_data.get('author'),
                email=form.cleaned_data.get('email'),
                description=form.cleaned_data.get('description')
            )

            return redirect('home')
