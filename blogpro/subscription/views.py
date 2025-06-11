from django.shortcuts import render
from app.models import Student

# Create your views here.
def subscribe(req):
    return render(req,'subscription.html')

def subscribe1(req,pk):
    userdata=Student.objects.get(id=pk)
    return render(req,'subscription.html',{'userdata':userdata})