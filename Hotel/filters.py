from .models import *
import django_filters
from django import forms


class HotelFilter(django_filters.FilterSet):
    town = django_filters.ModelMultipleChoiceFilter(queryset=City.objects.all(),
                                                    widget=forms.CheckboxSelectMultiple)
    venue = django_filters.ModelMultipleChoiceFilter(queryset=VendorType.objects.all(),
                                                     widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Listings
        fields = ['town', 'venue', 'vegprice', 'maxcap']
