from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from estudiante.models import Estudiante
from voto.models import Voto

# Create your views here.
@login_required(login_url='/')
def candidatos(request):
    id_usuario = request.user.id
    print(id_usuario)
    context = {
        'listas': Lista.objects.all(),
        'candidatos': Candidato.objects.all(),
        'estudiante': Estudiante.objects.get(user_id=id_usuario),
    }
    print(context['estudiante'])
    # if request.GET.get('id_est') and request.GET.get('id_lista'):
    #     print(request.GET.get('id_est') and request.GET.get('id_lista'))
    #     id_est, id_lista = request.GET['id_est'], request.GET['id_lista']
    #     print('estudiante: ', id_est)
    #     print('lista: ', id_lista)
    #     voto = Voto(voto_de = id_est, voto_por = id_lista)
    #     voto.save()
    #     return redirect('/')
    return render(request, 'candidato/candidatos.html', context)
