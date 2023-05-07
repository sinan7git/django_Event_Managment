from django.db import models


class Venue(models.Model):
    name = models.CharField('Venue Name', max_length=120)
    address = models.CharField('Address',max_length=300)
    phone = models.CharField('Contact Number',max_length=25)
    email_address = models.EmailField('Email Address',)
    event_type = models.TextField(blank=True)

    def __str__(self):
        return self.name


class EventUser(models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    email = models.EmailField()
    
    
    def __str__(self):
        return self.first_name + ' ' + self.last_name
    
    
    
class Event(models.Model):
    name = models.CharField(max_length=120)
    event_date = models.DateTimeField()
    venue = models.ForeignKey(Venue, blank=True, null=True, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    attendance = models.ManyToManyField(EventUser, blank=True)
    event_type = models.TextField(blank=True)
    
    def __str__(self):
        return self.name
    
    
