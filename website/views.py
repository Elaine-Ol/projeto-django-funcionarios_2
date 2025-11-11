from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Avg
from funcionario.models import Funcionarios
from .forms import FuncionarioForm

def index(request):
    """Página inicial com dashboard"""
    funcionarios = Funcionarios.objects.all()
   
    total_funcionarios = funcionarios.count()
    tempo_medio = funcionarios.aggregate(Avg('tempo_de_servico'))['tempo_de_servico__avg'] or 0
    salario_medio = funcionarios.aggregate(Avg('remuneracao'))['remuneracao__avg'] or 0
    
    context = {
        'funcionarios': funcionarios,
        'total_funcionarios': total_funcionarios,
        'tempo_medio': round(tempo_medio, 1),
        'salario_medio': round(salario_medio, 2),
    }
    return render(request, 'website/index.html', context)

def cadastrar_funcionario(request):
    """Cadastrar novo funcionário"""
    if request.method == 'POST':
        form = FuncionarioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Funcionário cadastrado com sucesso!')
            return redirect('listar_funcionarios')
    else:
        form = FuncionarioForm()
    
    return render(request, 'website/cadastrar_funcionario.html', {'form': form})

def listar_funcionarios(request):
    """Listar todos os funcionários"""
    funcionarios = Funcionarios.objects.all()
    return render(request, 'website/listar_funcionarios.html', {'funcionarios': funcionarios})

def detalhes_funcionario(request, id):
    """Detalhes de um funcionário"""
    funcionario = get_object_or_404(Funcionarios, id=id)
    return render(request, 'website/detalhes_funcionario.html', {'funcionario': funcionario})

def editar_funcionario(request, id):
    """Editar funcionário existente"""
    funcionario = get_object_or_404(Funcionarios, id=id)
    
    if request.method == 'POST':
        form = FuncionarioForm(request.POST, instance=funcionario)
        if form.is_valid():
            form.save()
            messages.success(request, 'Funcionário atualizado com sucesso!')
            return redirect('listar_funcionarios')
    else:
        form = FuncionarioForm(instance=funcionario)
    
    return render(request, 'website/editar_funcionario.html', {'form': form, 'funcionario': funcionario})

def excluir_funcionario(request, id):
    """Excluir funcionário"""
    funcionario = get_object_or_404(Funcionarios, id=id)
    
    if request.method == 'POST':
        funcionario.delete()
        messages.success(request, 'Funcionário excluído com sucesso!')
        return redirect('listar_funcionarios')
    
    return render(request, 'website/excluir_funcionario.html', {'funcionario': funcionario})