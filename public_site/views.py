from django.shortcuts import render
from datetime import datetime
from .models import iqama
from .models import Prayer_time
from .models import events

def home(request):
    Today_date = datetime.now()
    iqamas = iqama.objects.first()
    Prayer_times = Prayer_time.objects.get(date=Today_date)
    weekly_events = events.objects.all()
    salat = {
        'iqamas': iqamas,
        'prayer_times': Prayer_times,
        'events': weekly_events
    }
    return render(request, 'public_site/home.html', {'salat':salat})
    # return render(request, 'public_site/home.html', {'iqamas':iqamas}, {'prayer_time':Prayer_times})

def test(request):
    
    return render(request, 'public_site/test.html')