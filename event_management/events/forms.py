from django.forms import ModelForm
from .models import Venue,Event
from django import forms



class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ('name','event_type', 'event_date', 'venue', 'description')
        labels = {
            'event_date' : 'YYYY-MM-DD'
        }
        
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control', 'placeholder':''}),
            'event_type' :forms.TextInput(attrs={'class':'form-control', 'placeholder':'Event Type'}),
            'event_date' :forms.TextInput(attrs={'class':'form-control', 'placeholder':'Date'}),
            'venue' :forms.Select(attrs={'class':'form-control', 'placeholder':'Venue'}),
            'description':forms.Textarea(attrs={'class':'form-control', 'placeholder':'Description'}),
                    
        }


class VenueForm(ModelForm):
    class Meta:
        model = Venue
        fields = ('name', 'address', 'event_type', 'email_address', 'phone' )
        
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Venue Name'}),
            'address' :forms.TextInput(attrs={'class':'form-control', 'placeholder':'Address'}),
            'phone' :forms.TextInput(attrs={'class':'form-control', 'placeholder':'Phone Number'}),
            'email_address':forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email Address'}),
            'event_type' :forms.TextInput(attrs={'class':'form-control', 'placeholder':'Event Type'}),
        }