from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from filmes.forms import FilmeForm, GeneroForm
from filmes.models import Filme, Genero

class GeneroListView(ListView):
    model = Genero
    template_name = 'genero/genero_list.html'
    context_object_name = 'generos'
    paginate_by = 8
    queryset = Genero.objects.order_by('-id')

class GeneroDetailView(DetailView):
    model = Genero
    template_name = 'genero/genero_detail.html'

class GeneroCreateView(CreateView):
    model = Genero
    form_class = GeneroForm
    template_name = 'genero/genero_form.html'
    success_url = reverse_lazy('genero_list')

class GeneroUpdateView(UpdateView):
    model = Genero
    fields = ['nome', 'filmes']
    template_name = 'genero/genero_form.html'
    success_url = reverse_lazy('genero_list')

class GeneroDeleteView(DeleteView):
    model = Genero
    template_name = 'genero/genero_confirm_delete.html'
    success_url = reverse_lazy('genero_list')

class FilmeListView(ListView):
    model = Filme
    template_name = 'filmes/filme_list.html'

class FilmeDetailView(DetailView):
    model = Filme
    template_name = 'filmes/filme_detail.html'
    
class FilmeCreateView(CreateView):
    model = Filme
    form_class = FilmeForm
    template_name = 'filmes/filme_form.html'
    success_url= reverse_lazy('filme_list')

class FilmeUpdateView(UpdateView):
    model = Filme
    form_class = FilmeForm
    template_name = 'filmes/filme_form.html'
    success_url = reverse_lazy('filme_list')

class FilmeDeleteView(DeleteView):
    model = Filme
    template_name = 'filmes/filme_confirm_delete.html'
    success_url = reverse_lazy('filme_list')