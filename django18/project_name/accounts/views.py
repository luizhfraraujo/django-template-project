from django.shortcuts import render

# Create your views here.

def dashboard(request):
	template_name = 'accounts/dashboard.html'

	return render(request, template_name)

def index(request):
	template_name = 'accounts/index.html'

	return render(request, template_name)