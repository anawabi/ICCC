from django.db import models
from django.db import models

class iqama(models.Model):
    iq_fajr     = models.CharField(max_length=50)
    iq_dhur     = models.CharField(max_length=50)
    iq_asr      = models.CharField(max_length=50)
    iq_maghrib  = models.CharField(max_length=50)
    iq_isha     = models.CharField(max_length=50)
    iq_jumma    = models.CharField(max_length=50)


class Prayer_time(models.Model):
    date = models.DateField()
    Fajr_Salat = models.TimeField()
    Sunrise_Time = models.TimeField()
    Duhr_Salat = models.TimeField()
    Asr_Salat = models.TimeField()
    Maghrib_Salat = models.TimeField()
    Isha_Salat = models.TimeField()

class events(models.Model):
    event_name = models.CharField(max_length=100)
    event_frequency = models.CharField(max_length=50)
    event_date = models.DateField()
    event_time = models.TimeField()
    event_type = models.CharField(max_length=50)
    event_speaker = models.CharField(max_length=50)
    even_venue = models.CharField(max_length=100)
    event_image = models.ImageField(upload_to='images/events/')
   