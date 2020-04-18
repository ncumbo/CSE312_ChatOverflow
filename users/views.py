from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm


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
	if request.method == 'POST':
		user_update = UserUpdateForm(request.POST, instance=request.user)
		profile_update = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

		if user_update.is_valid() and profile_update.is_valid():
			profile_update.save()
			user_update.save()
			messages.success(request, 'Profile updated!')
			return redirect('profile')

	else:
		user_update = UserUpdateForm(instance=request.user)
		profile_update = ProfileUpdateForm(instance=request.user.profile)

	keyVals = {
		'user_update': user_update,
		'profile_update': profile_update
	}
	return render(request,'users/profile.html',keyVals)