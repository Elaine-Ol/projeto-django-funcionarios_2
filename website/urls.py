from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cadastrar/', views.cadastrar_funcionario, name='cadastrar_funcionario'),
    path('listar/', views.listar_funcionarios, name='listar_funcionarios'),
    path('detalhes/<int:id>/', views.detalhes_funcionario, name='detalhes_funcionario'),
    path('editar/<int:id>/', views.editar_funcionario, name='editar_funcionario'),
    path('excluir/<int:id>/', views.excluir_funcionario, name='excluir_funcionario'),
]