from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import generics
from .models import Machine, Game
from .form import MachineForm, GameForm
from django.db.models import Q
from django.core.paginator import Paginator
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy
from .serializer import MachineSerializer,GameSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication



class MachineListAPI(generics.ListCreateAPIView):
    queryset = Machine.objects.all()
    serializer_class = MachineSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

class GameListAPI(generics.ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

# Create your views here.
def listMachine(request):
    query = request.GET.get('search')
    machines = Machine.objects.all()
    if query:
        machines = Machine.objects.filter(
            Q(name__icontains = query)
        )
    paginator = Paginator(machines,10)
    page = request.GET.get('page')
    machines = paginator.get_page(page)
    return render(request,'machine/list.html',{'machines':machines})

class ListMachine(ListView):
    model = Machine
    context_object_name = 'machines'
    template_name = 'machine/list.html'
    queryset = Machine.objects.all()

class AddMachine(CreateView):
    model = Machine
    template_name = 'machine/machine.html'
    #fields = ('name','number','ip','start_time','end_time','user_id')
    form_class = MachineForm
    success_url = reverse_lazy('machine:list_machine')

class EditMachine(UpdateView):
    model = Machine
    template_name = 'machine/machine.html'
    #fields = ('name','number','ip','start_time','end_time','user_id')
    form_class = MachineForm
    success_url = reverse_lazy('machine:list_machine')


class AddGames(CreateView):
    model = Game
    template_name = 'machine/game.html'
    #fields = ('name','number','ip','start_time','end_time','user_id')
    form_class = GameForm
    success_url = reverse_lazy('machine:list_game')
    
class ListGame(ListView):
    model = Game
    context_object_name = 'games'
    template_name = 'machine/listgame.html'
    queryset = Game.objects.all()

class EditGame(UpdateView):
    model = Game
    template_name = 'machine/game.html'
    #fields = ('name','number','ip','start_time','end_time','user_id')
    form_class = GameForm
    success_url = reverse_lazy('machine:list_game')
