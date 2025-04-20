from django.shortcuts import render
from .models import User

def home(req):
    return render(req,'home.html')

# def home1(req,pk=None):
#     userdata=User.objects.get(stu_id=pk)
#     print(userdata)
#     userdata={
#                    'name':userdata.stu_name,
#                    'email':userdata.stu_email,
#                    'password':userdata.stu_password,
#                    'image':userdata.stu_image,
#                    'mycv':userdata.stu_document
#                 }
#     return render(req,'home.html',{'user':userdata})

def about(req):
    return render(req,'about.html')

# def about1(req,pk=None):
#     userdata=User.objects.get(stu_id=pk)
#     print(userdata)
#     userdata={
#                    'name':userdata.stu_name,
#                    'email':userdata.stu_email,
#                    'password':userdata.stu_password,
#                    'image':userdata.stu_image,
#                    'mycv':userdata.stu_document
#                 }
#     return render(req,'about.html',{'user':userdata})


def login(req):
    return render(req,'login.html')
def register(req):
    return render(req,'signup.html')

def registerdata(req):
    n=req.POST.get('username')
    e=req.POST.get('email')
    g=req.POST.get('gender')
    pa=req.POST.get('password')
    cp=req.POST.get('cpassword')
    pc=req.FILES.get('profile_image')
    r=req.FILES.get('document')
    # print(n,e,g,pa,pc,cp,r)
    data={'name':n,'email':e,'profilepic':pc,'document':r}
    user=User.objects.filter(User_email=e)
    if user:
        msg="Email exist"
        return render(req,'signup.html',{'error':msg})  
    else:
        if pa==cp:
            User.objects.create(User_name=n,
                          User_email=e,
                          User_gender=g,
                          User_password=pa,
                          User_image=pc,
                          User_document=r)
            msg="registratin done"
            return render(req,'login.html',{'error':msg})
        else:
            msg="Password and confirm password not match"
            return render(req,'signup.html',{'error':msg,'key':data})


def logindata(req):
    if req.method=='POST':
        email=req.POST.get('email')
        password=req.POST.get('password')
        users=User.objects.filter(User_email=email)
        if users:
            userdata=User.objects.get(User_email=email)
            print(userdata)
            if userdata.User_password==password:
                error='Welcome to Dashboard'
                userdata={
                   'name':userdata.User_name,
                   'email':userdata.User_email,
                   'password':userdata.User_password,
                   'img':userdata.User_image
                }
                print(userdata)
                return render(req,'userdashboard.html',{'user':userdata})
            else:
                error='Email & Password not match'
                return render(req,'login.html',{'error':error})             

        else:
            error='email is not registered'
            return render(req,'signup.html',{'key':{'email':email}})

    else:
        error="404 error server not found"
        return render(req,'login.html',{'error':error})    

def feature(req):
    return render(req,'feature.html')

def account(req):
    return render(req,'account.html')

def account(req):
    return render(req,'userdashboard.html')