from django.shortcuts import render 
from DMPages.models import Contact
from datetime import datetime
from django.contrib import messages

# messages.debug(request, '%s SQL statements were executed.' % count)
# messages.info(request, 'Three credits remain in your account.')
# messages.success(request, 'Profile details updated.')
# messages.warning(request, 'Your account expires in three days.')
# messages.error(request, 'Document deleted.')

# Create your views here.
def home (request):
    if request.method =="POST":
        Name = request.POST.get('name')
        Email = request.POST.get('email')
        Phone = request.POST.get('phone')
        Description = request.POST.get('description')
        contact = Contact(Name=Name,Email=Email,Phone=Phone,Description=Description,Date=datetime.today())
        contact.save()
        messages.success(request, 'Your Details has been submit Successfully !')
    return render(request, 'home.html')

def about (request):
    if request.method =="POST":
        Name = request.POST.get('name')
        Email = request.POST.get('email')
        Phone = request.POST.get('phone')
        Description = request.POST.get('description')
        contact = Contact(Name=Name,Email=Email,Phone=Phone,Description=Description,Date=datetime.today())
        contact.save()
        messages.success(request, 'Your Details has been submit Successfully !')
    return render(request, 'about.html')

def services (request):
    if request.method =="POST":
        Name = request.POST.get('name')
        Email = request.POST.get('email')
        Phone = request.POST.get('phone')
        Description = request.POST.get('description')
        contact = Contact(Name=Name,Email=Email,Phone=Phone,Description=Description,Date=datetime.today())
        contact.save()
        messages.success(request, 'Your Details has been submit Successfully !')
    return render(request, 'services.html')

def trainings (request):
    if request.method =="POST":
        Name = request.POST.get('name')
        Email = request.POST.get('email')
        Phone = request.POST.get('phone')
        Description = request.POST.get('description')
        contact = Contact(Name=Name,Email=Email,Phone=Phone,Description=Description,Date=datetime.today())
        contact.save()
        messages.success(request, 'Your Details has been submit Successfully !')
    return render(request, 'trainings.html')

def consultancy (request):
    if request.method =="POST":
        Name = request.POST.get('name')
        Email = request.POST.get('email')
        Phone = request.POST.get('phone')
        Description = request.POST.get('description')
        contact = Contact(Name=Name,Email=Email,Phone=Phone,Description=Description,Date=datetime.today())
        contact.save()
        messages.success(request, 'Your Details has been submit Successfully !')
    return render(request, 'consultancy.html')

def contact (request):
    if request.method =="POST":
        Name = request.POST.get('name')
        Email = request.POST.get('email')
        Phone = request.POST.get('phone')
        Description = request.POST.get('description')
        contact = Contact(Name=Name,Email=Email,Phone=Phone,Description=Description,Date=datetime.today())
        contact.save()
        messages.success(request, 'Your Details has been submit Successfully !')
    return render(request, 'contact.html')