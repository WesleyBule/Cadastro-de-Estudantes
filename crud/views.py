from .models import Estudantes
from django.views.generic import ListView , CreateView  , UpdateView , DeleteView 
from django.urls import reverse_lazy

class EstudanteListView(ListView):
    model = Estudantes


class EstudanteCreateView(CreateView):
    model = Estudantes
    fields = ['nome','idade','turma']
    success_url = reverse_lazy("estudante_list")    


class EstudanteUpdateView(UpdateView):
    model = Estudantes
    fields = ['nome','idade','turma']
    success_url = reverse_lazy("estudante_list")

class EstudanteDeleteView(DeleteView):
    model = Estudantes
    success_url = reverse_lazy("estudante_list")