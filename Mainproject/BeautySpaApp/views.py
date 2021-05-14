from django.shortcuts import render,redirect
from .models import Appoint_details
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def homepage(request):
    return render(request, 'homepage.html')
def contactpage(request):
    return render(request, 'contactpage.html')
def thankyoupage(request):
    return render(request, 'Thankyoupage.html')
def logfunc(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        print(user)
        return redirect('/')
    else:
        return render(request,'registration/login.html')

def logoutfun(request):
    logout(request)
    return redirect('login')

def spec(request):
    return render(request, 'Specpage.html')

def book_appointment(request):
    try:
        District=request.POST['district']
        careType=request.POST['services']
        location=request.POST['location']
        dateOfAppointment=request.POST['date']
        timeOfAppointment=request.POST['time']
        fullname=request.POST['name']
        phone = request.POST['phone']
        detail_list=Appoint_details(careType=careType,location=location,District=District,dateOfAppointment=dateOfAppointment,timeOfAppoinment=timeOfAppointment,fullname=fullname,phone=phone)
        detail_list.save()
        return render(request,'Thankyoupage.html')
    except Exception as e:
        print(e)
        return render(request,'Specpage.html')

def status_check(request):
    responseDic={}
    flag=0
    try:
        phonenum=int(request.POST['phonenum'])
        print(phonenum)
        all_list = Appoint_details.objects.all()
        for i in all_list:
            if (i.phone== phonenum):
                status = i.Status
                print(status)
                flag=1
                break;
            else:
                flag=0

        if (flag==1):
            responseDic['msg1'] = 'Your Request is '+status+'. We will Contact you soon...'
            return render(request, 'statuspage.html', responseDic)
        elif (flag==0):
            responseDic['msg2'] =' You have not submitted any request'
            return render(request, 'statuspage.html', responseDic)
    except Exception as e:
        print(e)
        return render(request,'statuspage.html')
