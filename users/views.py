from django.shortcuts import render, redirect
from .form import UserRegistrationForm
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        Form =UserRegistrationForm(request.POST)
        if Form.is_valid():
            Form.save()
            username = Form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('blog-home')
        else:
            print(Form.errors)
    else:
        Form = UserRegistrationForm()

    return render(request, 'users/register.html', {'Form': Form})
