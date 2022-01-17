from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

import destinations

from .forms import AddDestinationForm, AddCountryForm
from traveling import conn_user
from .models import Region, Country, Destination

# Create your views here.

def index(request):
    regions = Region.objects.all()
    countries = Country.objects.all()
    destinations = Destination.objects.all()
    return render(request, "destinations/index.html", {
		'user': request.user,
        'regions': regions,
        'countries': countries,
		'destinations': destinations,
	})

@method_decorator(login_required(login_url='login'), name='dispatch')
class Add(TemplateView):
    template_name = 'destinations/add.html'

    def post(self, request, **kwargs):
        form = AddDestinationForm(request.POST, request.FILES)
        if form.is_valid():
            user = request.user
            conn_user(request, user)
            name = form.cleaned_data.get('name')
            region = form.cleaned_data.get('region')
            country = form.cleaned_data.get('country')
            introduction = form.cleaned_data.get('introduction')
            photo = form.cleaned_data.get('photo')
            country = Country.objects.get(name = country)
            if country != None and country.region == region:
                Destination.objects.create(
                    name = name,
                    country = country,
                    introduction = introduction,
                    photo = photo,
                    publisher = request.user,
                ).save()
            return redirect('/destinations/')
        print(form.errors)
        print(form.is_bound)
        return redirect('/destinations/')

    def get(self, request, **kwargs):
        form = AddDestinationForm()
        return render(request, self.template_name, {
            'form': form,
        })

class AddCountry(TemplateView):
    template_name = 'destinations/add_country.html'

    def post(self, request, **kwargs):
        form = AddCountryForm(request.POST)
        if form.is_valid():
            user = request.user
            conn_user(request, user)
            user = request.user
            conn_user(request, user)
            name = form.cleaned_data.get('name')
            region = form.cleaned_data.get('region')
            Country.objects.create(
                name = name,
                region = region,
            ).save()
            return redirect('/destinations/')

    def get(self, request, **kwargs):
        user = request.user
        conn_user(request, user)
        form = AddCountryForm()
        return render(request, self.template_name, {
            'form': form,
        })

class Detail(TemplateView):
    template_name = 'destinations/detail.html'

    def get(self, request, id, **kwargs):
        user = request.user
        conn_user(request, user)
        destination = Destination.objects.get(id = int(id))
        if destination == None:
            return redirect('/random/pass/to/access/404')
        return render(request, self.template_name, {
            'dest': destination,
        })