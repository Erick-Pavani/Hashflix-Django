from django.shortcuts import redirect, render, reverse
from.models import Filme, Usuario
from .forms import CriarContaForm, FormHomePage
from django.views.generic import TemplateView, ListView, DetailView, FormView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class Homepage(FormView):
    template_name = "homepage.html"
    form_class = FormHomePage

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("filme:homefilmes")
        return super().get(request, *args, **kwargs)
    
    def get_success_url(self):
        email = self.request.POST.get("email")
        usuarios = Usuario.objects.filter(email = email)
        if usuarios:
            return reverse("filme:login")
        return reverse("filme:criarconta")


class Homefilmes(LoginRequiredMixin, ListView):
    template_name = "homefilmes.html"
    model = Filme

class Detalhesfilme(LoginRequiredMixin, DetailView):
    template_name = "detalhesfilme.html"
    model = Filme

    def get(self, request, *args, **kwargs):
        filme = self.get_object()
        filme.visualizacoes += 1
        filme.save()
        usuario = request.user
        usuario.filmes_vistos.add(filme)
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(Detalhesfilme, self).get_context_data()
        filmes_relacionados = Filme.objects.filter(categoria = self.get_object().categoria).exclude(titulo = self.get_object().titulo)[0:5]
        context['filmes_relacionados'] = filmes_relacionados
        return context

class PesquisaFilme(LoginRequiredMixin, ListView):
    template_name = "pesquisa.html"
    model = Filme

    def get_queryset(self):
        termo_pesquisa = self.request.GET.get("query")
        if termo_pesquisa:
            object_list = self.model.objects.filter(titulo__icontains = termo_pesquisa)
            return object_list 
        return None
    
class EditarPerfil(LoginRequiredMixin, UpdateView):
    template_name = 'editarperfil.html'
    model = Usuario
    fields = ['first_name', 'last_name', 'email']

    def get_success_url(self):
        return reverse("filme:homefilmes")

class CriarConta(FormView):
    template_name = "criarconta.html"
    form_class = CriarContaForm

    def get_success_url(self):
        return reverse('filme:login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)