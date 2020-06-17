from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth

# Create your views here.
def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name =request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        '''if campo_vazio(nome):
            messages.error(request , 'O campo nome não pode ficar em branco')
            return redirect('cadastro')
        if campo_vazio(email):
            messages.error(request , 'O campo email não pode ficar em branco')
            return redirect('cadastro')
        if senhas_nao_sao_iguais(senha,senha2):
            messages.error(request , 'As senhas não são iguais')
            return redirect('cadastro')
        if User.objects.filter(email=email).exists():
            messages.error(request , 'Usuário já cadastrado')
            return redirect('cadastro') 
        if User.objects.filter(username=nome).exists():
            messages.error(request , 'Usuário já cadastrado')
            return redirect('cadastro')'''
        user = User.objects.create_user(username= username, email= email, password= password, first_name= first_name)
        user.save()
        '''messages.success(request, 'User registed')'''
        return redirect('login')
    else:
        return render(request,'registration/sign_in.html')  