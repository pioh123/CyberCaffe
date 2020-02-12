from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from .models import Machine
from .form import MachineForm
from django.db.models import Q
from django.core.paginator import Paginator
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy


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



    
