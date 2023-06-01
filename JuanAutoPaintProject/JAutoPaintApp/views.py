from django.shortcuts import render, redirect
from .models import car

# Create your views here.

def index(request):
   return render (request, 'JAutoPaintApp/index.html')

def newpaintjob(request):
    if(request.method == "POST"):
        plate_num = request.POST.get("plate_num")
        curr_color = request.POST.get("curr_color")
        target_color = request.POST.get("target_color")
        car.objects.create(plate_num=plate_num, curr_color=curr_color, target_color=target_color)
        return redirect('paintjobs')

    else:
        return render (request, 'JAutoPaintApp/newpaintjob.html')


def paintjobs(request):
    allpjobs = car.objects.all()
    return render(request, 'JAutoPaintApp/paintjobs.html', {'pjobs':allpjobs})



