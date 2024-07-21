from django.shortcuts import render, redirect,  get_object_or_404
from django.contrib import messages
from django.contrib.auth import login, authenticate
from estudiante.models import Estudiante
from voto.models import Voto
from candidato.models import Candidato

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
        if request.GET.get('id_est') and request.GET.get('id_lista'):
            print(request.GET.get('id_est') and request.GET.get('id_lista'))
            id_est, id_lista = request.GET['id_est'], request.GET['id_lista']
            print('estudiante: ', id_est)
            print('lista: ', id_lista)
            candidato = get_object_or_404(Candidato, pk=id_lista)
            estudiante = get_object_or_404(Estudiante, pk=id_est)
            voto = Voto(voto_de=estudiante, voto_por=candidato)
            voto.save()
            return redirect('/')
        return render(request, 'estudiante/inicio_login.html', {})

    