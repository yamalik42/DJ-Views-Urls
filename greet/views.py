from django.shortcuts import render
from datetime import datetime, timezone
from django.http import HttpResponse


# Create your views here.
def show_greet(request):
    utc_dt = datetime.now(timezone.utc) # UTC time
    dt = utc_dt.astimezone() # local time
    hour = dt.now().hour

    mapping = hour//12

    def evening():
        return HttpResponse('Good Evening')
    
    def morning():
        return HttpResponse('Good Morning')

    greetings = [morning, evening]
    
    return greetings[mapping]()
