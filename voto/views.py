from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from candidato.models import Candidato
from .models import Voto
from estudiante.models import Estudiante

@login_required
def votar(request):
    if request.method == "POST":
        candidato_id = request.POST.get('candidato_id')
        tipo_voto = request.POST.get('tipo_voto')

        if tipo_voto not in ['voto', 'nulo', 'blanco']:
            return HttpResponse("Tipo de voto inválido.", status=400)
        
        try:
            candidato = Candidato.objects.get(id=candidato_id)
        except Candidato.DoesNotExist:
            return HttpResponse("Candidato no encontrado.", status=404)
        
        try:
            estudiante = Estudiante.objects.get(user=request.user)
        except Estudiante.DoesNotExist:
            return HttpResponse("No se ha encontrado el perfil de estudiante.", status=404)
        
        if Voto.objects.filter(voto_de=estudiante, voto_por__dignidad=candidato.dignidad).exists():
            return HttpResponse("Ya has votado por esta dignidad.", status=400)
        
        # Crear el voto
        voto = Voto(voto_por=candidato, voto_de=estudiante)
        if tipo_voto == 'nulo':
            voto.nulo = True
        elif tipo_voto == 'blanco':
            voto.blanco = True
        else:
            voto.numero = Voto.objects.filter(voto_por=candidato).count() + 1
        
        voto.save()
        return redirect('candidatos') 

    return HttpResponse("Método no permitido.", status=405)
