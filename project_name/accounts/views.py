from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
from project_name.core.utils import generate_hash_key
from .forms import RegisterForm, EditAccountForm, PasswordResetForm
from .models import UserPasswordReset

# Create your views here.
User = get_user_model

@login_required
def dashboard(request):
	template_name = 'accounts/dashboard.html'
	context = {}
	
	return render(request,template_name, context)

@login_required
def profile(request, user):
	template_name = 'accounts/profile.html'
	context = {}
	user_profile = get_object_or_404(User.objects.all, username=user)
	#context['userprofile'] = user_profile
	
	return render(request,template_name, context)

def register(request):
	template_name = 'accounts/register.html'
	form = RegisterForm(request.POST or None)
	
	if form.is_valid():
		user = form.save()
		user = authenticate(username=user.username, password=form.cleaned_data['password1'])
		login(request, user)
		return redirect('core:home')

	context = {
		'form': form
		}
	return render(request, template_name,context)

def password_reset(request):
	template_name = 'accounts/password_reset.html'
	print(request.POST)
	form = PasswordResetForm(request.POST or None)
	context = {}

	if form.is_valid():
		form.save()
		context['success']=True

	context['form']=form

	return render(request, template_name,context)

def password_reset_confirm(request, key):
	template_name = 'accounts/password_reset_confirm.html'
	context = {}
	print(key)
	reset = get_object_or_404(UserPasswordReset, key=key)
	print('Password Reset Request. Username: %s, Email: %s' % (reset.user.username, reset.user.email))
	form = SetPasswordForm(user=reset.user, data=request.POST or None)
	if form.is_valid():
		form.save()
		print('Success Password Reset form %s' % (reset.user.username))
		context['success'] = True
	context['form'] = form
	return render(request, template_name, context)