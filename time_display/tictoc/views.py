from django.shortcuts import render, HttpResponse
from time import gmtime, strftime
import datetime
def index(request):
    context = {
        "time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M %p")
    }
    return render(request,'index.html', context)
