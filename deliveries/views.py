from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse,  HttpResponseRedirect

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.contrib.auth import login

from datetime import datetime
from .models import *

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

def home(request):
    items = Items.objects.all()
    if request.method == 'POST':
        item = request.POST.get("item")
        quantity = request.POST.get("quantity")
        date = request.POST.get("date")
        time = request.POST.get("time")
        delivery = Delivery.objects.create(customer=request.user, item=item, quantity=quantity, date=date, time=time)
        return  HttpResponseRedirect('home')
    heading = "These Woes"
    date = datetime.today().strftime('%Y-%m-%d')
    time = datetime.today().strftime('%H:%M')
    context = {
        'heading':heading,
        'date':date,
        'time':time,
        'items':items
    }
    print(time)
    return render(request, 'deliveries/index.html', context)