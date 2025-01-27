from django.shortcuts import render
from django.http import HttpResponse
from .models import Servicos
from .models import Atendentes
from .models import Resolvedores
from .models import Excluir
from .models import Modificar
from .models import Inserir
from django.shortcuts import redirect
import datetime 

# Create your views here.

def ver_catalogo(request):
    return render(request, 'ver_catalogo.html')

def login_catalogo(request):
    atendente = Atendentes.objects.all()
    global login_atendente
    global telefone
    login_atendente = request.POST.get('atendente')
    request.session['nome_save'] = login_atendente
    telefone = request.POST.get('telefone')
    request.session['telefone_save'] = telefone
    if request.method == "POST":  
        if len(telefone) >= 14:     
           return redirect("https://catalogo-glpi.trt1.jus.br/principal/escolher/")
        else:
           pass
    context = {"atendente": atendente, "telefone": telefone}
    #context = {"atendente": nome_save , "telefone": telefone_save}
    return render(request, 'login_catalogo.html', context)
    
            

def escolher_catalogo(request):
    if request.method == 'POST':      
       opcoes = request.POST.get('opcao')
       print(opcoes)
       if opcoes == 'INSERIR':
          return redirect ("https://catalogo-glpi.trt1.jus.br/principal/inserir/")
       elif opcoes == 'MODIFICAR':
           return redirect ("https://catalogo-glpi.trt1.jus.br/principal/modificar/")
       elif opcoes == 'EXCLUIR':
           return redirect ("https://catalogo-glpi.trt1.jus.br/principal/excluir/")
       elif opcoes == None:
           return redirect ("https://catalogo-glpi.trt1.jus.br/principal/pedidos/")
    return render(request, 'escolher_catalogo.html')

def inserir_catalogo(request):
    resolvedor = Resolvedores.objects.values()
    servicos = Servicos.objects.values()
    cat_n0 = list(Servicos.objects.values_list('categoria_n0', flat=True).distinct())
    nome_save = request.session['nome_save']
    telefone_save = request.session['telefone_save']
    if (not request.session.keys()) or (nome_save == None or telefone_save == None):
        return redirect("https://catalogo-glpi.trt1.jus.br/principal/login/")
    else:
        pass
    if request.method == "POST":
       fila = request.POST.get('fila')
       tipo = request.POST.get('tipo')
       area = request.POST.get('area')
       data_hora = datetime.date.today()
       categoria_n0 =  request.POST.get('categoria_n0')
       categoria_n1 = request.POST.get('categoria_n1')
       categoria_n2 = request.POST.get('categoria_n2')
       categoria_n3 = request.POST.get('categoria_n3')
       sla = request.POST.get('SLA')
       resolvedores = request.POST.get('resolvedores')
       gestores = request.POST.get('gestores')
       comentarios = request.POST.get('comentarios')
       bd_inserir = Inserir(data_criação=data_hora, nome=nome_save, telefone=telefone_save, setor=fila,  tipo=tipo, area=area, categoria_n0=categoria_n0, categoria_n1=categoria_n1, categoria_n2=categoria_n2, categoria_n3=categoria_n3, sla=sla, resolvedores=resolvedores, gestores=gestores, comentarios=comentarios)
       bd_inserir.save()
       return redirect("https://catalogo-glpi.trt1.jus.br/principal/escolher/")
    context = {"resolvedor": resolvedor, "servicos": servicos, "cat_n0": cat_n0, "nome_save": nome_save}
    return render(request, 'inserir_catalogo.html', context)

def modificar_catalogo(request):
    resolvedor = Resolvedores.objects.values()
    servicos = Servicos.objects.values() 
    cat_n0 = list(Servicos.objects.values_list('categoria_n0', flat=True).distinct())
    nome_save = request.session['nome_save']
    telefone_save = request.session['telefone_save']
    if (not request.session.keys()) or (nome_save == None or telefone_save == None):
        return redirect("https://catalogo-glpi.trt1.jus.br/principal/login/")
    else:
        pass
    if request.method == "POST":
       fila = request.POST.get('fila')
       atual = request.POST.get('escolserv')
       tipo = request.POST.get('tipo')
       area = request.POST.get('area')
       data_hora = datetime.date.today()
       categoria_n0 =  request.POST.get('categoria_n0')
       categoria_n1 = request.POST.get('categoria_n1')
       categoria_n2 = request.POST.get('categoria_n2')
       categoria_n3 = request.POST.get('categoria_n3')
       sla = request.POST.get('SLA')
       resolvedores = request.POST.get('resolvedores')
       gestores = request.POST.get('gestores')
       comentarios = request.POST.get('comentarios')
       bd_modificar = Modificar(nome=nome_save, telefone=telefone_save, setor=fila, data_criação=data_hora, serviço_atual=atual, tipo=tipo, area=area, categoria_n0=categoria_n0, categoria_n1=categoria_n1, categoria_n2=categoria_n2, categoria_n3=categoria_n3, sla=sla, resolvedores=resolvedores, gestores=gestores, comentarios=comentarios)
       bd_modificar.save()
       return redirect("https://catalogo-glpi.trt1.jus.br/principal/escolher/")
    context = {"resolvedor": resolvedor, "servicos": servicos, "cat_n0": cat_n0}
    return render(request, 'modificar_catalogo.html', context)


def excluir_catalogo(request):
    resolvedor = Resolvedores.objects.values()
    servicos = Servicos.objects.values() 
    nome_save = request.session['nome_save']
    telefone_save = request.session['telefone_save']
    if (not request.session.keys()) or (nome_save == None or telefone_save == None):
        return redirect("https://catalogo-glpi.trt1.jus.br/principal/login/")
    else:
        pass
    if request.method == "POST":
       data_hora = datetime.date.today()
       fila = request.POST.get('fila')
       serviço = request.POST.get('escolserv')
       bd_excluir = Excluir(nome=nome_save, telefone=telefone_save, setor=fila, data_criação=data_hora, serviço=serviço)
       bd_excluir.save()
       return redirect("https://catalogo-glpi.trt1.jus.br/principal/escolher/")
    context = {"resolvedor": resolvedor, "servicos": servicos} 
    return render(request, 'excluir_catalogo.html', context)

def pedidos_catalogo(request):
    resolvedor = Resolvedores.objects.values()
    hoje = datetime.date.today()
    pedidos_inserir = Inserir.objects.filter(data_criação__range=[hoje, hoje])
    pedidos_modificar = Modificar.objects.filter(data_criação__range=[hoje, hoje])
    pedidos_excluir = Excluir.objects.filter(data_criação__range=[hoje, hoje])
    
    if request.method == "POST":
     if request.POST.get('botao') == 'insert':
      op = request.POST.get('escolserv')
      if op == None or op == '':
          pass
      else:
          excluir_inserção = Inserir.objects.filter(id = op[-4:])
          excluir_inserção.delete()
          print(op)
     if request.POST.get('botao') == 'modify':
      op2 = request.POST.get('escolserv2')
      if op2 == None or op2 == '':
          pass
      else:
          excluir_moficação = Modificar.objects.filter(id = op2[-4:])
          excluir_moficação.delete()
     if request.POST.get('botao') == 'exclude':
      op3 = request.POST.get('escolserv3')
      if op3 == None or op3 == '':
          pass
      else:
          excluir_exclusao = Excluir.objects.filter(id = op3[-4:])
          excluir_exclusao.delete()
           
    context = {"resolvedor": resolvedor, "pedidos_inserir": pedidos_inserir, "pedidos_modificar": pedidos_modificar, "pedidos_excluir": pedidos_excluir} 
    return render(request, 'pedidos_catalogo.html', context)

     

    



    



    
    