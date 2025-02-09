from django.shortcuts import render
from django.core.mail import EmailMessage
from django.core.mail import send_mail
from django.conf import settings

def home(request):
	return render(request, 'home.html', {})

def contact(request):
	if request.method == "POST":
		your_name = request.POST['name']
		email = request.POST['email']
		subject = request.POST['subject']
		message = request.POST['message']



		email = EmailMessage(
			subject,
			message,
			email,
			to=['jazzuchi69@gmail.com'],
			reply_to=['', email],
			)
		email.send()



		return render(request, 'contact.html', {'message_name': your_name})
	else:
		return render(request, 'contact.html', {})


def menu(request):
	return render(request, 'menu.html', {})


def about(request):
	return render(request, 'about.html', {})

def service(request):
	return render(request, 'service.html', {})


# Create your views here.
