from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from analyzer.models import FinalTableAll, FinalTable


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
    pos_data = []
    neg_data = []
    for row in FinalTableAll.objects.all().order_by('date', '-tweet_count'):
        semantic_data.append({'x': row.date, 'y': row.entity, 'heat': str(row.semantic_compound)})
        occurrence_data.append({'x': row.date, 'y': row.entity, 'heat': row.tweet_count})
        pos_data.append({'x': row.date, 'y': row.entity, 'heat': str(row.semantic_pos)})
        neg_data.append({'x': row.date, 'y': row.entity, 'heat': str(row.semantic_neg)})

    return render(request, 'tweety/index.html', {
        'compound_data': semantic_data,
        'occurrence_data': occurrence_data,
        'positivity_data': pos_data,
        'negativity_data': neg_data
    })


@login_required
def country_page(request):
    semantic_data = []
    occurrence_data = []
    for row in FinalTable.objects.all().order_by('date', '-tweet_count'):
        semantic_data.append({'region': row.region, 'x': row.date, 'y': row.entity, 'heat': str(row.semantic_compound)})
        occurrence_data.append({'region': row.region, 'x': row.date, 'y': row.entity, 'heat': row.tweet_count})

    return render(request, 'tweety/country.html', {
        'semantic_data': semantic_data,
        'occurrence_data': occurrence_data
    })


@login_required
def info_page(request):
    return render(request, 'tweety/info.html')


@login_required
def contact_page(request):
    return render(request, 'tweety/contact.html')
