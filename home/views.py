from django.shortcuts import render,HttpResponse
from home.models import contact
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def services(request):
    return render(request,'services.html')

def contact(request):
    if request.method == "post":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        query=contact(name=name, email=email, message=message)
        query.save()
        messages.success(request, "Your Message sent sucessfully!")
        
        return HttpResponse('Your message has been sent!')

    return render(request,'contact.html')
