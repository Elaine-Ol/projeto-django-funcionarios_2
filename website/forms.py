from django import forms
from funcionario.models import Funcionarios

class FuncionarioForm(forms.ModelForm):
    class Meta:
        model = Funcionarios
        fields = ['nome', 'sobrenome', 'cpf', 'tempo_de_servico', 'remuneracao']
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite o nome'
            }),
            'sobrenome': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Digite o sobrenome'
            }),
            'cpf': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '000.000.000-00'
            }),
            'tempo_de_servico': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '0'
            }),
            'remuneracao': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '0.00',
                'step': '0.01'
            }),
        }