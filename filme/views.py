from multiprocessing import context
from django.shortcuts import render
from.models import Filme
from django.views.generic import TemplateView, ListView, DetailView

# Create your views here.

class Homepage(TemplateView):
    template_name = "homepage.html"

class Homefilmes(ListView):
    template_name = "homefilmes.html"
    model = Filme

class Detalhesfilme(DetailView):
    template_name = "detalhesfilme.html"
    model = Filme

    def get(self, request, *args, **kwargs):
        filme = self.get_object()
        filme.visualizacoes += 1
        filme.save()
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(Detalhesfilme, self).get_context_data()
        filmes_relacionados = Filme.objects.filter(categoria = self.get_object().categoria).exclude(titulo = self.get_object().titulo)[0:5]
        context['filmes_relacionados'] = filmes_relacionados
        return context

class PesquisaFilme(ListView):
    template_name = "pesquisa.html"
    model = Filme

    def get_queryset(self):
        termo_pesquisa = self.request.GET.get("query")
        if termo_pesquisa:
            object_list = self.model.objects.filter(titulo__icontains = termo_pesquisa)
            return object_list 
        return None