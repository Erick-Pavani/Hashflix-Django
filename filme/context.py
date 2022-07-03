from .models import Filme

def filmes_recentes(request):
    lista_filmes = Filme.objects.all().order_by('-data_criacao')[0:10]
    return {"lista_filmes_recentes": lista_filmes}

def filmes_alta(request):
    lista_filmes = Filme.objects.all().order_by('-visualizacoes')[0:10]
    return {"lista_filmes_alta": lista_filmes}

def filme_destaque(request):
    filme = Filme.objects.order_by('-data_criacao')[0]
    return {"filme_destaque": filme}