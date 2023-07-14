from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login
from .models import UserProfile

from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect

from .forms import UserProfileForm

from django.shortcuts import render

def home(request):
    return render(request, 'home.html')



def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('login')
        else:
            messages.error(request, 'Username or password is incorrect')
            return render(request, 'home.html')
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})



# def login_view(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             # Redireciona para uma página de sucesso.
#         else:
#             messages.error(request, 'Usuário ou senha incorretos')
#     # Se a solicitação for um GET (ou qualquer outro método), exibimos o formulário de login em branco.
#     return render(request, 'login.html')





def signup_view(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        # password1 = request.POST.get('password1')
        # password2 = request.POST.get('password2')
        #
        # if password1 != password2:
        #     messages.error(request, 'As senhas não são iguais')
        #     form.add_error('password2', 'As senhas não são iguais')

        if form.is_valid():
            user, user_profile = form.save()
            login(request, user)
            return redirect('home')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{form.fields[field].label}: {error}")
    else:
        form = UserProfileForm(initial=request.POST)  # Passando o objeto request.POST para manter os dados preenchidos

    return render(request, 'signup.html', {'form': form})




