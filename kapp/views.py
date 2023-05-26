from django.shortcuts import render

from .models import Enquiry



# Create your views here.
def indexPage(request):
   return render(request, "index.html")

def contactPage(request):
   return render(request,"getintouch.html")

def websitePage(request):
   return render(request, "website.html")

def aboutPage(request):
   return render(request, "about.html")

def DigitalPage(request):
   return render(request,"digital.html")

def SoftwarePage(request):
   return render(request, "software.html")

def ClientPage(request):
   return render(request, "client.html")

def SaveData(request):
   if request.method=="POST": 
      name=request.POST['name']
      email=request.POST['email']
      mob=request.POST['mob']
      subject=request.POST['subject']
      purpose=request.POST['purpose']
      query=request.POST['query']
      file=request.FILES['cv'] 
      document=Enquiry.objects.create(file=file)
      newData=Enquiry(name=name,email=email,mobile=mob,purpose=purpose,subject=subject,query=query)
      newData.save()
      msg="Successfully Submitted.........!"
   return render(request, "submit.html",{'msg':msg})

   





