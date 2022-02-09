
from django.shortcuts import render, redirect
from datetime import datetime

def index(request):
    now = datetime.now()
    context = {
       
        'time': datetime.strftime(now, "%b %d, %Y"),
        'time2': datetime.strftime(now, " %H:%M %p")
         
    }
    return render(request, 'app/index.html', context)


  
