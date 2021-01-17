from collections import Counter

from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from twitter.models import Entities


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
    labels = []
    data = []

    values = Entities.objects.values("normalized_text")
    result = [value["normalized_text"] for value in values]

    counter = Counter(result)

    for k, v in counter.most_common(20):
        labels.append(k)
        data.append(v)

    return render(request, 'registration/index.html', {
        'labels': labels,
        'data': data,
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
