from django.shortcuts import render
from . models import Contact,User

# Create your views here.
def index(request):
    return render(request,'index.html')

def contact(request):
    if request.method=="POST":
        Contact.objects.create(
            name=request.POST['name'],
            email=request.POST['email'],
            mobile=request.POST['mobile'],
            remarks=request.POST['remarks']
        )
        msg="Contact Saved Successfully"
        contacts=Contact.objects.all().order_by("-id")[:5]
        return render(request,'contact.html',{'msg':msg, 'contacts':contact})
    else:
        return render(request,'contact.html',{'contacts':contact})

def signup(request):
    if request.method=="POST":
       try: 
          User.objects.get(email=request.POST['email'])
          msg="email allredy registerd"
          return render(request,'signup.html',{'msg':msg})

       except:
        if request.POST['password']==request.POST['cpassword']:
           User.objects.create(
                fname=request.POST['fname'],
                lname=request.POST['lname'],
                email=request.POST['email'],
                mobile=request.POST['mobile'], 
                address=request.POST['address'],
                gender=request.POST['gender'],
                password=request.POST['password'],
            
           )
           msg="User sign up successfully"
           return render(request,'signup.html',{'msg':msg})
        else:
           msg="Password & Confirm Password Does Not Matched"
           return render(request,'signup.html',{'msg':msg})          
    else:
       return render(request,'signup.html')

def login(request):
    return render(request,'login.html')