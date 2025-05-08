from django.shortcuts import render
from .models import User
from .models import Student

def home(req):
    return render(req,'home.html')

def home1(req,pk):
    userdata=User.objects.get(id=pk)
    print(userdata)
    userdata1={    
                   'id':userdata.id,
                   'name':userdata.User_name,
                   'email':userdata.User_email,
                   'password':userdata.User_password,
                   'image':userdata.User_image,
                   'mycv':userdata.User_document,
                   'img':userdata.User_image

                }
    return render(req,'home.html',{'userdata':userdata1})

def about(req):
    return render(req,'about.html')

def about1(req,pk):
    userdata=User.objects.get(id=pk)
    print(userdata)
    userdata1={    'id':userdata.id,
                   'name':userdata.User_name,
                   'email':userdata.User_email,
                   'password':userdata.User_password,
                   'image':userdata.User_image,
                   'mycv':userdata.User_document,
                   'img':userdata.User_image

                }
    return render(req,'about.html',{'userdata':userdata1})


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
       return render(req,'login.html',{'error1':msg}) 
    else: 
        for i in range(0,10):
            if str(i) in n:
                msg='*Number is not allowed in username'
                return render(req,'signup.html',{'error':msg})
            
        if "@" not in e or "." not in e:
            msg = "*Invalid email"
            return render(req, 'signup.html', {'error1': msg})
        if "@." in e or ".@" in e:
            msg = "*Invalid email"
            return render(req, 'signup.html', {'error1': msg})
        
        if len(pa)<8:
                    msg='*Please must be Password length 8 or more'
                    return render(req,'signup.html',{'Perror':msg})
        

        checker=False       
        for i in pa:
          if i.isdigit():
            checker=True
            break
        if(checker==False):
                    msg='*Please make sure your password contains at least one digit'        
                    return render(req,'signup.html',{'Perror':msg})    
        

        checker=False      
        for i in pa:
            if i.isupper():
                        checker=True
                        break   
        if(checker==False):
                    msg='*Please make sure your password contains at least one upper case letter'        
                    return render(req,'signup.html',{'Perror':msg})


        checker=False 
        spchar="!@#$%^&*()-_+={}[]:;'\"<>,.?/"
        for i in pa:
            if i in spchar:
                checker=True
                break
        if(checker==False):
                    msg='*Please make sure your password contains at least one special character'        
                    return render(req,'signup.html',{'Perror':msg})    
                    
       
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
            msg="*Password and confirm password not match"
            return render(req,'signup.html',{'Perror':msg,'key':data})


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
                userdata1={
                    'id':userdata.id,
                   'name':userdata.User_name,
                   'email':userdata.User_email,
                   'password':userdata.User_password,
                   'img':userdata.User_image
                }
                print(userdata.User_name)
                button="Logout"
                return render(req,'userdashboard.html',{'userdata':userdata1 ,'button':button})
            else:
                error='*Email & Password not match'
                return render(req,'login.html',{'error':error})             

        else:
            error='*Email is not registered'
            return render(req,'signup.html',{'key':{'email':email}})

    else:
        error="404 error server not found"
        return render(req,'login.html',{'error':error})    

def feature(req):
    return render(req,'feature.html')

def feature1(req,pk):
    userdata=User.objects.get(id=pk)
    print(userdata)
    userdata1={    'id':userdata.id,
                   'name':userdata.User_name,
                   'email':userdata.User_email,
                   'password':userdata.User_password,
                   'image':userdata.User_image,
                   'mycv':userdata.User_document,
                   'img':userdata.User_image

                }
    return render(req,'feature.html',{'userdata':userdata1})


def account(req):
    msg="Please Register your Account"
    button="Login"
   
    return render(req,'userdashboard.html' ,{'error': msg,'button':button})



def account1(req,pk):
    userdata=User.objects.get(id=pk)
    button="Logout"
    print(userdata)
    userdata1={    'id':userdata.id,
                   'name':userdata.User_name,
                   'email':userdata.User_email,
                   'password':userdata.User_password,
                  
                   'img':userdata.User_image,
                   'mycv':userdata.User_document,
                }
    return render(req,'userdashboard.html',{'userdata':userdata1 ,'button':button})




def fn1(req):
    data=Student.objects.all()[:5]
    return render(req,'home.html', {'data':data})


def fn2(req):
    data=Student.objects.all()[::-1][:5]
    return render(req,'home.html', {'data':data})

def fn3(req):
    data=Student.objects.all()
    return render(req,'home.html', {'data':data})

def fn4(req):
    data=Student.objects.order_by('id')
    return render(req,'home.html', {'data':data})

def fn5(req):
    data=Student.objects.order_by('-id')
    return render(req,'home.html', {'data':data})