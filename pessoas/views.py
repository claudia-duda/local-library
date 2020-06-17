from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name =request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if not first_name.strip():
            messages.error(request , 'Field fisrt name invalid')
            return redirect('register')

        if not last_name.strip():
            messages.error(request , 'Field last name invalid')
            return redirect('register')

        if not username.strip():
            messages.error(request , 'Field username invalid')
            return redirect('register')  

        if not email.strip():
            messages.error(request , 'Field email invalid')
            return redirect('register')

        if not password == password2:
            messages.error(request , 'the password is different')
            return redirect('register')

        if User.objects.filter(email= email).exists():
            messages.error(request , 'User exists')
            return redirect('register') 

        if User.objects.filter(username= username ).exists():
            messages.error(request , 'User exists')
            return redirect('register')
            
        user = User.objects.create_user(username= username, email= email, password= password, first_name= first_name)
        user.save()
        messages.success(request, 'User registed')

        return redirect('login')

    else:
        return render(request,'registration/sign_in.html')  