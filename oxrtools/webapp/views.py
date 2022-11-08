from django.shortcuts import render
from .models import Aadhar_Front
from .forms import AadharFront, AadharBack
from django.http import HttpResponseRedirect
# Create your views here.


def home(request):

    return render(request, 'home.html')

def get_files(request):
    aadharfront = Aadhar_Front.objects.get()
    return render(request, 'show.html',{
        'aadharfront':aadharfront,
    })

def add_aadhar_front(request):
    submitted = False
    if request.method == "POST":
        form = AadharFront(request.POST, request.FILES)
        if form.is_valid:
            form.save()
            return HttpResponseRedirect('add_aadhar_front?submitted=True')

    else:
        form = AadharFront
        if 'submitted' in request.GET:
            submitted =True
    return render(request, 'add_aadhar_front.html', {
        'form':form, 'submitted':submitted,
    })

def add_aadhar_back(request):
        submitted = False
        if request.method == "POST":
            form = AadharBack(request.POST, request.FILES)
            if form.is_valid:
                form.save()
                return HttpResponseRedirect('add_aadhar_back?submitted=True')

        else:
            form = AadharBack
            if 'submitted' in request.GET:
                submitted =True
        return render(request, 'add_aadhar_back.html', {
            'form':form, 'submitted':submitted,
        })
