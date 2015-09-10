from django.shortcuts import render

# Create your views here.

def dashboard(request):
	template_name = 'accounts/dashboard.html'

	return render(request, template_name)

def login(request):
	template_name = 'accounts/login.html'

	return render(request, template_name)

def register(request):
	template_name = 'accounts/register.html'

	return render(request, template_name)