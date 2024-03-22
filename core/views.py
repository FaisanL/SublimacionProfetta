from django.shortcuts import render, redirect, get_object_or_404 
from django.contrib import messages
from django.contrib.auth import logout
from .models import Taza
from .forms import *
# Create your views here.
TEMPLATE_DIR =(
    'os.path.join(BASE_DIR, "templates"),'
)
def index(request):
    return render(request, 'index.html')
def coleccion(request):
    taza = Taza.objects.all()
    datos = {
        'taza' : taza
    }
    return render(request, 'coleccion.html', datos)

def salir(request):
    logout(request)
    messages.success(request,("Has cerrado sesion correctamente..."))
    return redirect('index')

def mostrar_taza(request):
    if request.user.is_superuser:
        taza = Taza.objects.all()

        datos={
            'taza': taza
            }
        return render(request, 'mostrar_taza.html', datos)
    else:
        return redirect('index')


def form_taza(request):
    if request.user.is_superuser:
        datos = {'form': TazaForm()}
        if request.method == 'POST':
            formulario = TazaForm(request.POST, request.FILES)
            
            if formulario.is_valid():
                formulario.save()
                messages.success(request, 'Guardados correctamente')
            else:
                messages.error(request, 'Error al procesar el formulario')

        return render(request, 'form_taza.html', datos)
    else:
        return redirect('index')
    
def form_mod_taza(request, id):
    if request.user.is_superuser:
        taza = get_object_or_404(Taza, id=id)
        form = None
        if request.method == 'POST':
            form = TazaForm(request.POST, request.FILES, instance=taza)
            if form.is_valid():
                form.save()
                return redirect('mostrar_taza')
            else:
                form = TazaForm(instance=taza)

        return render(request, 'form_mod_taza.html', {'form': form, 'taza': taza})
    else:
        return redirect('index')
    

def form_del_taza(request, id):
    if request.user.is_superuser:
        taza = Taza.objects.get(id=id)
        taza.delete()
        return redirect(to="mostrar_taza")
    else:
        return redirect('index')

