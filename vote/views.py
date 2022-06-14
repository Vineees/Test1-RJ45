from django.contrib import messages
from django.shortcuts import render, HttpResponseRedirect
from vote.models import Alunos

# Create your views here.

def voteEmpty(request):
  return HttpResponseRedirect('vote/')

def vote(request):
  if request.method == 'POST':
    global matriculaForm
    matriculaForm = request.POST['matricula']
    voto_rei = request.POST['voto_rei']
    voto_rainha = request.POST['voto_rainha']

    if (Alunos.objects.filter(matricula=matriculaForm)) and ((Alunos.objects.get(matricula=matriculaForm).statusvoto) == 'N'):
      nome = Alunos.objects.get(matricula=matriculaForm).nome
      computar_votos = Alunos(matricula=matriculaForm, nome=str(nome) ,voto_rei=voto_rei, voto_rainha=voto_rainha, statusvoto='S')
      computar_votos.save()
      return HttpResponseRedirect('/finished/')
    elif (Alunos.objects.filter(matricula=matriculaForm)) and ((Alunos.objects.get(matricula=matriculaForm).statusvoto) == 'S'):
      messages.error(request, 'Você já votou!')
      return render(request, 'vote.html')
    else:
      messages.error(request, 'Matrícula incorreta!')
      return render(request, 'vote.html')

  return render(request, 'vote.html')

def finished(request):
  votosGui = Alunos.objects.filter(voto_rei=2021305180).count()
  votosIan = Alunos.objects.filter(voto_rei=2020302405).count()
  votosDan = Alunos.objects.filter(voto_rei=2020307045).count()
  votosKau = Alunos.objects.filter(voto_rei=2021303766).count()
  votosGil = Alunos.objects.filter(voto_rei=2021303701).count()

  votosAla = Alunos.objects.filter(voto_rainha=2020301800).count()
  votosKhe = Alunos.objects.filter(voto_rainha=2022306898).count()
  votosMil = Alunos.objects.filter(voto_rainha=2021303828).count()
  votosMon = Alunos.objects.filter(voto_rainha=2021303864).count()

  context_contagem = {
    'votosGui': votosGui,
    'votosIan': votosIan,
    'votosDan': votosDan,
    'votosKau': votosKau,
    'votosGil': votosGil,
    'votosAla': votosAla,
    'votosKhe': votosKhe,
    'votosMil': votosMil,
    'votosMon': votosMon,
  }

  return render(request, 'finished.html', context_contagem)