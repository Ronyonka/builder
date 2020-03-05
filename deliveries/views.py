from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse,  HttpResponseRedirect

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

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

@login_required
def home(request):
    items = Items.objects.all()
    if request.method == 'POST':
        item = request.POST.get("item")
        selected_item = Items.objects.get(id=item)
        quantity = request.POST.get("quantity")
        dateTime = request.POST.get("dateTime")
        delivery = Delivery.objects.create(customer=request.user, item=selected_item, quantity=quantity, dateTime=dateTime)
        return  HttpResponseRedirect('/')
    heading = "Log Deliveries Here"
    date = datetime.today().strftime('%Y-%m-%d')
    time = datetime.today().strftime('%H:%M')
    deliveries = Delivery.objects.all()
    dates_list = set([i.dateTime.date for i in deliveries])
    context = {
        'heading':heading,
        'date':date,
        'time':time,
        'deliveries':deliveries,
        'items':items
    }
    print(dates_list)
    return render(request, 'deliveries/index.html', context)

@login_required
def delivery_logs(request):
    heading = "Delivery Logs"
    try:
        deliveries = Delivery.objects.filter(customer=request.user)
    except Delivery.DoesNotExist:
        deliveries = []
    dates_list = set([i.dateTime.date for i in deliveries])
    context = {
        'heading':heading,
        'deliveries':deliveries
    }
    return render(request, 'deliveries/log.html', context)

def logout_request(request):
    logout(request) 
    return redirect("login")