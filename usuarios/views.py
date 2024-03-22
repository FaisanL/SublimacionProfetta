from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from django.http import HttpResponse

# Create your views here.

def login_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']

        if not request.user.is_authenticated:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)

                # Set a session variable to indicate that the user is already logged in
                request.session['is_logged_in'] = True

                return redirect('index')
            else:
                messages.success(request, '¡Verifique las credenciales!', extra_tags='alert alert-success')
                return redirect('login')
        else:
            # User already authenticated, redirect to index page
            return redirect('index')
    else:
        # Handle GET requests for the login form
        return render(request, 'authenticate/login.html')

def is_logged_in(request):
    # Check the session variable to see if the user is already logged in
    return request.session.get('is_logged_in', False)

def protected_view(request):
    # Check if the user is logged in
    if not request.user.is_authenticated:
        # User is not logged in, redirect to login page
        return redirect('login')

    # User is logged in, do something here
    return HttpResponse('¡Estás autenticado!')

def registro_usuario(request):
    if request.user.is_authenticated:
        return redirect('index')
    password_requirements = CustomUserCreationForm().fields['password1'].help_text
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            
            if password1 == password2:
                user.set_password(password1)
                user.save()

                username = form.cleaned_data['username']
                user = authenticate(username=username, password=password1)
                login(request, user)

                # Mostrar un mensaje de éxito
                messages.success(
                    request,
                    'Registro exitoso',
                    extra_tags='alert alert-success'
                )
                return redirect('index')
            else:
                # Mostrar mensaje de error si las contraseñas no coinciden
                messages.warning(
                    request,
                    'Las contraseñas no coinciden',
                    extra_tags='alert alert-danger'
                )
        else:
            # Mostrar mensajes de error para cada campo inválido
            for field, errors in form.errors.items():
                for error in errors:
                    message = f"{field} {error}"
                    if field == 'username':
                        messages.warning(
                            request,
                            'El nombre de usuario ya está en uso.',
                            extra_tags='alert alert-danger'
                        )
                    elif field == 'email':
                        messages.warning(
                            request,
                            'El correo ya está en uso.',
                            extra_tags='alert alert-danger'
                        )
                    elif field.startswith('password1'):
                        messages.warning(
                            request,
                            'La contraseña no cumple con los requisitos de seguridad.',
                            extra_tags='alert alert-danger'
                        )
    else:
        form = UserCreationForm()

    return render(request, 'authenticate/registro_usuario.html', {'form': form, 'password_requirements': password_requirements})