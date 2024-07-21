from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate

def inicio_login(request):
    if request.method == 'POST':
        user_cedula = request.POST.get('cedula', None)
        user_password = request.POST.get('password', None)
        errors = 'Credenciales incorrectas'
        usuario = authenticate(username = user_cedula, password = user_password)
        #print(request.POST, user_cedula, user_password)
        if usuario:
            #return redirect('candidatos')
            login(request, usuario)
            return redirect('candidatos')  # redireccionar a la vista de candidatos cuando se loguea correctamente
        else:
            messages.error(request, errors)
            return redirect('inicio_login')
    else:
        print(request.GET)
        return render(request, 'estudiante/inicio_login.html', {})
