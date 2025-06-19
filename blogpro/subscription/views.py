from django.shortcuts import render
from app.models import Student
from django.views.decorators.csrf import csrf_exempt
from .models import Product
import razorpay

# Create your views here.
def subscribe(req):
    return render(req,'subscription.html')

def subscribe1(req,pk):
    userdata=Student.objects.get(id=pk)
    return render(req,'subscription.html',{'userdata':userdata})

from .models import Product

def payment(request):
    global payment
    if request.method=="POST":
        # amount in paisa
        amount = int(request.POST.get('amount')) * 100
        
        client = razorpay.Client(auth =("rzp_test_pr99iascS1WRtU" , "UTDIzPGwICnAssu3Q3lk7zUi"))
        # create order
        
        data = { "amount": amount, "currency": "INR", "receipt": "order_rcptid_11" }
        payment = client.order.create(data=data)
        product = Product.objects.create( amount =amount , order_id = payment['id'])

        amount=int(request.POST.get('amount'))
        
        alldata= { 'text':request.POST.get('data'),
        'text1': request.POST.get('data1'),
        'text2': request.POST.get('data2'),
        'text3': request.POST.get('data3')
        }
       
        # print(payment)
        return render(request,'subscription.html',{'key':alldata,'amount':amount,'payment':payment})
    
@csrf_exempt
def payment_status(request):
       if request.method=="POST": 
        response = request.POST
        # print(response) 
        # print(payment)

        razorpay_data = {
            'razorpay_order_id': response['razorpay_order_id'],
            'razorpay_payment_id': response['razorpay_payment_id'],
            'razorpay_signature': response['razorpay_signature']
        }

        # client instance
        client = razorpay.Client(auth =("rzp_test_pr99iascS1WRtU" , "UTDIzPGwICnAssu3Q3lk7zUi"))

        try:
            status = client.utility.verify_payment_signature(razorpay_data)
            product = Product.objects.get(order_id=response['razorpay_order_id'])
            product.razorpay_payment_id = response ['razorpay_payment_id']
            product.paid = True
            product.save()
            
            return render(request, 'success.html', {'status': True})
        except:
            return render(request, 'success.html', {'status': False})