# from django.contrib.auth.models import User
from .models import *
from django.shortcuts import render
from .filters import HotelFilter


def search(request):
    hotel_list = Listings.objects.all()
    hotel_filter = HotelFilter(request.GET, queryset=hotel_list)
    return render(request, 'Hotel/hotel_list.html', {'filter': hotel_filter})
