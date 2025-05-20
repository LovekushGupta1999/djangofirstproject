from django.shortcuts import render
from .models import Student,Admin,Question,Solution
from django.db.models import Q
from datetime import datetime

def home(req):
    return render(req,'home.html')

def home1(req,pk):
    userdata=Student.objects.get(id=pk)
    return render(req,'home.html',{'userdata':userdata})

def homeadm(req,pk):
    admindata=Admin.objects.get(id=pk)
    return render(req,'home.html',{'admindata':admindata})

def about(req):
    return render(req,'about.html')

def about1(req,pk):
    userdata=Student.objects.get(id=pk)
    return render(req,'about.html',{'userdata':userdata})

def aboutadm(req,pk):
    admindata=Admin.objects.get(id=pk)
    return render(req,'about.html',{'admindata':admindata})




def login(req):
    return render(req,'login.html')

def registerstu(req,pk):
    if req.method=='POST':
        n=req.POST.get('username')
        e=req.POST.get('email')
        g=req.POST.get('gender')
        pa=req.POST.get('password')
        cp=req.POST.get('cpassword')
        pc=req.FILES.get('profile_image')
        r=req.FILES.get('document')
        
        data={'name':n,'email':e,'profilepic':pc,'document':r}
        user=Student.objects.filter(User_email=e)
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
                Student.objects.create(User_name=n,
                            User_email=e,
                            User_gender=g,
                            User_password=pa,
                           )
                msg="registratin done"
                admindata=Admin.objects.get(id=pk)
                data=Student.objects.all()
                return render(req,'userdashboard.html',{'error':msg,'admindata':admindata,'data':data})
            else:
                msg="*Password and confirm password not match"
                return render(req,'signup.html',{'Perror':msg,'key':data})
    else:    
      admindata=Admin.objects.get(id=pk)
      return render(req,'usersignup.html',{'admindata':admindata})
    

def registeradm(req):
    if req.method=='POST':
        n=req.POST.get('username')
        e=req.POST.get('email')
        g=req.POST.get('gender')
        pa=req.POST.get('password')
        cp=req.POST.get('cpassword')
        data={'name':n,'email':e}
        admin=Admin.objects.filter(Admin_email=e)
        if admin:
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
                Admin.objects.create(Admin_name=n,
                            Admin_email=e,
                            Admin_gender=g,
                            Admin_password=pa,
                            )
                
                msg="registratin done"
                # admindata=Admin.objects.get(id=pk)
                return render(req,'login.html',{'error':msg})
            else:
                msg="*Password and confirm password not match"
                return render(req,'signup.html',{'Perror':msg,'key':data})
    else:    
      return render(req,'signup.html')
    



def logindata(req):
    if req.method=='POST':
        email=req.POST.get('email')
        password=req.POST.get('password')
        adlogin=req.POST.get('adlogin')
        print(adlogin)
        if not adlogin:
            print('thanks')
            users=Student.objects.filter(User_email=email)
            if users:
                userdata=Student.objects.get(User_email=email)
                
                if userdata.User_password==password:
                    error='Welcome to Dashboard'
                 
                
                    button="Logout"
                    return render(req,'userdashboard.html',{'userdata':userdata,'button':button})
                else:
                    error='*Email & Password not match'
                    return render(req,'login.html',{'error':error})             

            else:
                error='*Email is not registered'
                return render(req,'signup.html',{'key':{'email':email}})

           
        else:
          admin=Admin.objects.filter(Admin_email=email)
          if admin:
                admindata=Admin.objects.get(Admin_email=email)

          if admindata.Admin_email==email and admindata.Admin_password==password:
            button="Logout"
            return render(req,'userdashboard.html',{'admindata':admindata ,'button':button})
          else:
            error='*Email & Password not match'
            return render(req,'login.html',{'error':error})             

        

    else:
     error="404 error server not found"
     return render(req,'login.html',{'error':error})    

def feature(req):
    return render(req,'feature.html')

def feature1(req,pk):
    userdata=Student.objects.get(id=pk)
    return render(req,'feature.html',{'userdata':userdata})

def featureadm(req,pk):
    admindata=Admin.objects.get(id=pk)
    return render(req,'feature.html',{'admindata':admindata})


def account(req):
    msg="Please Register your Account"
    button="Login"
    return render(req,'userdashboard.html' ,{'error': msg,'button':button})



def account1(req,pk):
    userdata=Student.objects.get(id=pk)
    button="Logout"
    return render(req,'userdashboard.html',{'userdata':userdata,'button':button})

def accountadm(req,pk):
    admindata=Admin.objects.get(id=pk)
    button="Logout"
    return render(req,'userdashboard.html',{'admindata':admindata,'button':button})







def allstudent(req,pk):
    admindata=Admin.objects.get(id=pk)
    button="Logout" 
    
   
    data=Student.objects.all()
    return render(req,'userdashboard.html', {'data':data,'admindata':admindata,'button':button})


def fn10(req,pk):
    admindata=Admin.objects.get(id=pk)
    button="Logout" 
    
    today=datetime.now().date()
    taskdata=Question.objects.filter(date=today)
    return render(req,'userdashboard.html', {'taskdata':taskdata,'admindata':admindata,'button':button})

def fn11(req,pk):
    userdata=Student.objects.get(id=pk)
    button="Logout" 
    
    today=datetime.now().date()
    taskdata=Question.objects.filter(date=today)
    return render(req,'userdashboard.html', {'taskdata':taskdata,'userdata':userdata,'button':button})




def edit(req,pk,it):
    userdata=Student.objects.get(id=pk)
    button="Logout" 
    userdata1={    'id':userdata.id,
                   'name':userdata.User_name,
                   'email':userdata.User_email,
                   'password':userdata.User_password,
                   'image':userdata.User_image,
                   'mycv':userdata.User_document,
                   'img':userdata.User_image

                }
    
    data1=Student.objects.get(id=it)
    data2={   
                   'id':data1.id,
                   'name':data1.name,
                   'email':data1.email,
                   'contact':data1.contact,
                   

                }
    print(data2)
    print('hello')
    return render(req,'userdashboard.html', {'data1':data2,'userdata':userdata1,'button':button,'name':"update"})
    
def editstubyadmin(req,pk,it):
    admindata=Admin.objects.get(id=pk)
    button="Logout" 
    data1=Student.objects.get(id=it)
    data2={   
                   'id':data1.id,
                   'name':data1.User_name,
                   'email':data1.User_email,
                   'contact':data1.User_contact,
                   'password':data1.User_password,
                   

                }
    print(data2)
    return render(req,'userdashboard.html', {'data1':data2,'admindata':admindata,'button':button})
    

def editsol(req,pk,it):
    userdata=Student.objects.get(id=pk)
    button="Logout" 
    userdata1={    'id':userdata.id,
                   'name':userdata.User_name,
                   'email':userdata.User_email,
                   'password':userdata.User_password,
                   'image':userdata.User_image,
                   'mycv':userdata.User_document,
                   'img':userdata.User_image

                }
    
    data1=Solution.objects.get(id=it)
    data2={   
                   'id':data1.id,
                   'ques':data1.quest.ques,
                   'sol':data1.sol,
                   

                }
    return render(req,'userdashboard.html', {'esoldata':data2,'userdata':userdata1,'button':button,'name':"update"})


def delete(req,pk,it):
    userdata=Student.objects.get(id=pk)
    button="Logout" 

    data1=Student.objects.get(id=it)
    data1.delete()

    data=Student.objects.all()
    print(data)
    print('hello')
    return render(req,'userdashboard.html', {'data':data,'userdata':userdata,'button':button})
    

def deletestubyadmin(req,pk,it):
    admindata=Admin.objects.get(id=pk)
    button="Logout" 
   
    
    data1=Student.objects.get(id=it)
    data1.delete()

    data=Student.objects.all()
    return render(req,'userdashboard.html', {'data':data,'admindata':admindata,'button':button})
    

def deletesol(req,pk,it):
    userdata=Student.objects.get(id=pk)
    button="Logout" 
    userdata1={    'id':userdata.id,
                   'name':userdata.User_name,
                   'email':userdata.User_email,
                   'password':userdata.User_password,
                   'image':userdata.User_image,
                   'mycv':userdata.User_document,
                   'img':userdata.User_image

                }
    
    data1=Solution.objects.get(id=it)
    data1.delete()

    soldata=Solution.objects.filter(stu=userdata.id)
    return render(req,'userdashboard.html', {'soldata':soldata,'userdata':userdata1,'button':button})
    
def updatesol(req,pk):
    userdata=Student.objects.get(id=pk)
    button="Logout" 
   
    
    it=req.POST.get('ID')
    data1=Solution.objects.get(id=it)
    data1.sol=req.POST.get('sol')
    data1.save()


    soldata=Solution.objects.filter(stu=userdata.id)
    return render(req,'userdashboard.html', {'soldata':soldata,'userdata':userdata,'button':button})    

   
  
   

def update(req,pk):
    userdata=Student.objects.get(id=pk)
    button="Logout" 
   
    
    it=req.POST.get('ID')
    data1=Student.objects.get(id=it)
    data1.name=req.POST.get('name')
    data1.contact=req.POST.get('contact')
    data1.email=req.POST.get('email')
    data1.save()
   
    data=Student.objects.all()
    return render(req,'userdashboard.html', {'data':data,'userdata':userdata,'button':button})    


def updatestubyadmin(req,pk):
    admindata=Admin.objects.get(id=pk)
    button="Logout" 
   
    
    it=req.POST.get('ID')
    data1=Student.objects.get(id=it)
    data1.User_name=req.POST.get('name')
    data1.User_contact=req.POST.get('contact')
    data1.User_email=req.POST.get('email')
    data1.save()
   
    data=Student.objects.all()
    return render(req,'userdashboard.html', {'data':data,'admindata':admindata,'button':button})    

def editprofile(req,pk):
    userdata=Student.objects.get(id=pk)
    button="Logout" 
    data=True
    return render(req,'userdashboard.html', {'data3':data,'userdata':userdata,'button':button})

def editadmprofile(req,pk):
    admindata=Admin.objects.get(id=pk)
    button="Logout" 
    data=True
    return render(req,'userdashboard.html', {'data3':data,'admindata':admindata,'button':button})


    
def updateadmprofile(req,pk):
   
  if req.POST:  
    data1=Admin.objects.get(id=pk)
    data1.Admin_name=req.POST.get('name')
    data1.Admin_email=req.POST.get('email')
    data1.Admin_password=req.POST.get('password')
    data1.Admin_image=req.POST.get('profile_image')
    data1.save()
    

  
    admindata=Admin.objects.get(id=pk)
    button="Logout" 
   
    return render(req,'userdashboard.html', {'admindata':admindata,'button':button})    

    
def updateprofile(req,pk):
   
  if req.POST:  
    data1=Student.objects.get(id=pk)
    data1.User_name=req.POST.get('name')
    data1.User_email=req.POST.get('email')
    data1.User_password=req.POST.get('password')
    data1.User_image=req.POST.get('profile_image')
    data1.save()

  
    userdata=Student.objects.get(id=pk)
    button="Logout" 
    return render(req,'userdashboard.html', {'userdata':userdata,'button':button})    


def addstudentform(req,pk):
    userdata=Student.objects.get(id=pk)
    button="Logout" 
    userdata1={    'id':userdata.id,
                   'name':userdata.User_name,
                   'email':userdata.User_email,
                   'password':userdata.User_password,
                   'image':userdata.User_image,
                   'mycv':userdata.User_document,
                   'img':userdata.User_image

                }
    
    data2=True
    return render(req,'userdashboard.html', {'data1':data2,'userdata':userdata1,'button':button})


def addtaskwindow(req,pk):
    admindata=Admin.objects.get(id=pk)
    button="Logout" 
    taskform=True
    return render(req,'userdashboard.html', {'taskform':taskform,'admindata':admindata,'button':button})


def edittaskwindow(req,pk,it):
    admindata=Admin.objects.get(id=pk)
    button="Logout" 
    edittaskdata=Question.objects.get(id=it)
    return render(req,'userdashboard.html', {'edittaskdata':edittaskdata,'admindata':admindata,'button':button})
  

def addfeedback(req,pk,it):
    admindata=Admin.objects.get(id=pk)
    button="Logout" 
    if req.method=='POST':
      data=Solution.objects.get(id=it)
      data.feedback=req.POST.get('feedback')
      data.save()

    soldata=Solution.objects.all()  
    return render(req,'userdashboard.html', {'soldata':soldata,'admindata':admindata,'button':button})



def edittask(req,pk,it):
    admindata=Admin.objects.get(id=pk)
    button="Logout" 
    
    if req.method=='post':
       edittaskdata=Question.objects.get(id=it)
       edittaskdata.ques=req.POST.get('ques')
       edittaskdata.date=req.POST.get('date')
       edittaskdata.save()

    taskdata=Question.objects.all()
    return render(req,'userdashboard.html', {'taskdata':taskdata,'admindata':admindata,'button':button})


def deletetask(req,pk,it):
    admindata=Admin.objects.get(id=pk)
    button="Logout" 
    
   
    edittaskdata=Question.objects.get(id=it)
    edittaskdata.delete()
   

    taskdata=Question.objects.all()
    return render(req,'userdashboard.html', {'taskdata':taskdata,'admindata':admindata,'button':button})


def addtask(req,pk):
    admindata=Admin.objects.get(id=pk)
    button="Logout" 
    
    if req.method=='POST':
          Question.objects.create(ques=req.POST.get('ques'),
                                  date=req.POST.get('date'))
   
    
    taskdata=Question.objects.all()
    return render(req,'userdashboard.html', {'taskdata':taskdata,'admindata':admindata,'button':button})
 

def showtask(req,pk):
    admindata=Admin.objects.get(id=pk)
    button="Logout" 
    
    taskdata=Question.objects.all()
    return render(req,'userdashboard.html', {'taskdata':taskdata,'admindata':admindata,'button':button})


def showsol(req,pk):
    admindata=Admin.objects.get(id=pk)
    button="Logout" 
    
    soldata=Solution.objects.all()
    return render(req,'userdashboard.html', {'soldata':soldata,'admindata':admindata,'button':button})


def showtaskuser(req,pk):
    userdata=Student.objects.get(id=pk)
    button="Logout" 
    
    taskdata=Question.objects.all()
    return render(req,'userdashboard.html', {'taskdata':taskdata,'userdata':userdata,'button':button})


def solsubmit(req,pk,sk):
    userdata=Student.objects.get(id=pk)
    button="Logout" 
    if req.method=='POST':
       quest1=Question.objects.get(id=sk)
    

    Solution.objects.create(quest=quest1,
                       stu=userdata ,
                       sol=req.POST.get('solu'))
    
    soldata=Solution.objects.filter(stu=userdata.id)
    return render(req,'userdashboard.html', {'soldata':soldata,'userdata':userdata,'button':button})


def showsolstu(req,pk):
    userdata=Student.objects.get(id=pk)
    button="Logout" 
    soldata=Solution.objects.filter(stu=userdata.id)
    return render(req,'userdashboard.html', {'soldata':soldata,'userdata':userdata,'button':button})


def addstudent(req,pk):
    admindata=Student.objects.get(id=pk)
    button="Logout" 
    data2=True
    return render(req,'userdashboard.html', {'data1':data2,'admindata':admindata,'button':button})



def filterdata(req,pk):
    admindata=Admin.objects.get(id=pk)
    button="Logout" 
   
    if req.method=='POST':
      value=req.POST.get('record')
      value1=req.POST.get('record1')
      value2=req.POST.get('record2')
    
      data=Student.objects.filter(Q(User_name__icontains=value) | Q(User_contact__icontains=value1) | Q(User_email__icontains=value2))
      print(data)

   
      return render(req,'userdashboard.html', {'data':data,'admindata':admindata,'button':button})
    else:
      return render(req,'userdashboard.html', {'admindata':admindata,'button':button})


# -------------------------------admin---------------------------------------------------