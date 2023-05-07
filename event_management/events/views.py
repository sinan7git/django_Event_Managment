from django.shortcuts import render, redirect
from .models import Event, Venue
from .forms import VenueForm, EventForm
from django.http import HttpResponseRedirect


def delete_venue(request, venue_id):
    venue = Venue.objects.get(id=venue_id)
    venue.delete()
    return redirect('list-venues')


def delete_event(request, event_id):
    event = Event.objects.get(id=event_id)
    event.delete()
    return redirect('list-events')


def add_event(request):
    submitted = False
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('add_event?submitted=True')                
    else:
        form = EventForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'add_event.html', {'form':form, 'submitted':submitted})


def update_event(request, event_id):
    event = Event.objects.get(pk=event_id)
    form = EventForm(request.POST or None, instance=event)
    if form.is_valid():
        form.save()
        return redirect('list-events')
    return render(request, 'update_event.html',  { 'event' :event, 'form':form})


def update_venue(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    form = VenueForm(request.POST or None, instance=venue)
    if form.is_valid():
        form.save()
        return redirect('list-venues')
    return render(request, 'update_venue.html',  { 'venue' :venue, 'form':form})


def search_venue(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        venues = Venue.objects.filter(name__contains=searched)
    return render(request, 'search_venue.html',  {'searched': searched, 'venues' :venues})


def show_venue(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    return render(request, 'show_venue.html',  { 'venue' :venue})


def list_venues(request):
    venue_list = Venue.objects.all()
    return render(request, 'venue.html', {'venue_list':venue_list})


def add_venue(request):
    submitted = False
    if request.method == 'POST':
        form = VenueForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('add_venue?submitted=True')
            
                     
    else:
        form = VenueForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'add_venue.html', {'form':form, 'submitted':submitted})


def home(request):
    return render(request, 'home.html')


def event_items(request):
    if request.method == 'POST':
        from_date=request.POST.get('from_date')
        to_date=request.POST.get('to_date')
        search_result=Event.objects.raw('name, event_date, venue, event_type, description "'+from_date+'" and "'+to_date+'"')
        return render(request, 'event_items.html',{"data":search_result})
    else:
        displaydata=Event.objects.all()
        event_list = Event.objects.all().order_by("name")
        return render(request, 'event_items.html',  {'event_list': event_list,'data': displaydata})


