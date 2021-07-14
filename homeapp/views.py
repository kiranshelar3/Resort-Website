from django.shortcuts import render, HttpResponse
from datetime import date, datetime
from homeapp.models import Contact
from django.contrib import messages

# Create your views here.

def index(request):
    context = {
        'variable1' : ' im the one fo yopu',
        'variable2' : 'dont you know girl'
    }
    return render(request, 'index.html', context)
    # return HttpResponse(" this is home")

def about(request):
    # return HttpResponse(" this is about")
    return render (request, "about.html")

def contact(request):
    # return HttpResponse(" this is contact")
    if request.method == "POST":
        name = request.POST.get('name')
        number = request.POST.get('number')
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        contact = Contact(name=name, number= number, email=email, desc= desc, date = datetime.today())
        contact.save()
        messages.success(request, 'Your enquiery form has been submitted!')

    
    return render(request, 'contact.html')

def services(request):
    # return HttpResponse(" this is services")
    return render(request, 'services.html')
