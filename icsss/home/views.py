from django.shortcuts import render
from .models import Details
from django.http import HttpResponse


# Create your views here.
def home(request):
    if request.method == "POST":
        details = Details()
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        inquiry = request.POST.get('inquiry')
        details.name = name
        details.phone = phone
        details.email = email
        details.inquiry = inquiry
        details.save()
        return HttpResponse("<h2>Thanks for Your Queries</h2><h4>We will Contact you Soon</h4>")
    return render(request, 'homeicss.html')

