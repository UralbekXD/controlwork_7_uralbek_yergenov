from django.shortcuts import render, redirect, get_object_or_404

from .models import GuestBook
from .forms import RecordForm


def index(request):
    records = GuestBook.objects.exclude(status='blocked')
    return render(request, 'guestbook/index.html', context={
        'records': records.order_by('-created_at')
    })


def search_record(request):
    query = request.GET.get('author')
    result = GuestBook.objects.filter(author__icontains=query)

    return render(request, 'guestbook/search.html', context={
        'records': result
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


def edit_record(request, pk):
    record = get_object_or_404(GuestBook, pk=pk)
    match request.method:
        case 'GET':
            form = RecordForm(instance=record)
            return render(request, 'guestbook/edit.html', context={
                'pk': record.pk,
                'form': form,
            })

        case 'POST':
            form = RecordForm(request.POST)
            if not form.is_valid():
                return render(request, 'guestbook/edit.html', context={
                    'form': form,
                })

            # SUCCESS
            record.author = form.cleaned_data.get('author')
            record.email = form.cleaned_data.get('email')
            record.description = form.cleaned_data.get('description')
            record.save()

            return redirect('home')


def delete_record(request, pk):
    record = get_object_or_404(GuestBook, pk=pk)
    record.delete()

    return redirect('home')
