from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from analyzer.models import FinalTableAll


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


@login_required
def home(request):
    semantic_data = []
    occurrence_data = []
    for row in FinalTableAll.objects.all().order_by('date', 'tweet_count'):
        semantic_data.append({'x': row.date, 'y': row.entity, 'heat': row.semantic_compound})
        occurrence_data.append({'x': row.date, 'y': row.entity, 'heat': row.tweet_count})

    return render(request, 'registration/index.html', {
        'semantic_data': semantic_data,
        'occurrence_data': occurrence_data
    })


@login_required
def country_page(request):
    return render(request, 'registration/country.html')


@login_required
def info_page(request):
    return render(request, 'registration/info.html')


@login_required
def contact_page(request):
    return render(request, 'registration/contact.html')
