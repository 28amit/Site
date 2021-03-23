from django.shortcuts import render, HttpResponse,redirect, get_object_or_404
from datetime import datetime
from womenlab.models import Contact
from django.contrib import messages
from womenlab.models import Banner
from womenlab.models import FirstBanner
from womenlab.models import Course
from womenlab.models import Order
import razorpay
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def index(request):
	if request.method == 'POST':
		name=request.POST.get('name')
		phone=request.POST.get('phone')
		comments=request.POST.get('comments')
		contact=Contact(name=name, phone=phone, comments=comments, date=datetime.today())
		contact.save()
		messages.success(request, 'We will contact you as soon as posible.')
		return redirect('/')

	ban = Banner.get_banner();
	fban = FirstBanner.get_fbanner();
	courses = Course.get_course();

	return render(request,'index.html' , {'banners':ban ,'fban':fban , 'courses':courses})


def course_detail(request, id, slug):
	course = get_object_or_404(Course, id=id, slug=slug)
	lesson = Course.get_course();
	return render(request,'product.html',{'course':course,'lesson':lesson})

def pay_detail(request, id, slug, price):
	
		

	course = get_object_or_404(Course, id=id, slug=slug, price=price)
	return render(request,'payment.html',{'course':course})

def pay(request, id):
	course = get_object_or_404(Course, id=id)
	if request.method == 'POST':
		name=request.POST.get('name')
		email=request.POST.get('email')
		phone=request.POST.get('phone')
		course_name=request.POST.get('course_name')
		amount=int(request.POST.get('amount'))
		client = razorpay.Client(auth=('rzp_live_iEoz4RLh015vCh','JQK9DeLIF277oe1B6iNsHhx6'))
		payment = client.order.create({'amount':amount*100, 'currency':'INR', 'payment_capture':'1'})
		order = Order(course_name=course_name, name=name, email=email, phone=phone, amount=amount, payment_id=payment['id'])
		info = {'name':name,'phone':phone,'email':email}
		order.save()
		return render(request, 'pay.html',{'payment':payment,'course':course,'info':info})
		
	return render(request, 'pay.html',{'course':course})

@csrf_exempt
def success(request):
	if request.method == "POST":
		a = request.POST
		order_id = ""
		for key , val in a.items():
			if key == 'razorpay_order_id':
				order_id = val
				break
		user = Order.objects.filter(payment_id=order_id).first()
		user.paid = True
		user.save()
		return redirect('womenlab:success')
	return render(request,'success.html')
