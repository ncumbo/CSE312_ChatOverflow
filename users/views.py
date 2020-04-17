from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm

def registerView(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.clean_data.get('username') #protects against sql injection
			messages.success(request, 'Account created for {username}')
			return redirect('feed-home')
	else:
		form = UserRegisterForm()
	return render(request, 'users/register.html', {'form': form})

@login_required	#user must be logged in to view this page
def profile(request):
    return render(request, 'users/profile.html')