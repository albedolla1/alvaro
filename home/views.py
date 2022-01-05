from django.shortcuts import render
from django.http import request
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Storage, StorageSixA, StorageSixB, StorageSixC, StorageSixE
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.decorators import login_required
from .forms import SixAForm, SixBForm, SixCForm, SixEForm
from django.utils.decorators import method_decorator

# View for create account handling
class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


def home(request):
    context = {}
    # Storing all the table data information inside this 'sixa, sixb, sixc and sixe', this variable will be passed inside index.html
    context['sixa'] = StorageSixA.objects.all()    
    context['sixb'] = StorageSixB.objects.all()    
    context['sixc'] = StorageSixC.objects.all()    
    context['sixe'] = StorageSixE.objects.all()    
    return render(request, "index.html", context)


def sixA(request):
    context = {}
    # Storing all sixa table info inside items variable
    context['items'] = StorageSixA.objects.all()

    # This snippet is for searching and filtering information
    query = request.GET.get('q')
    if query:
        if query == 'all':
            pass
        else:
            context['items'] = StorageSixA.objects.filter(
                Q(item__icontains=query) | Q(location__icontains=query)
            )
    return render(request, "sixA.html", context)


def sixB(request):
    context = {}
    context['items'] = StorageSixB.objects.all()
    query = request.GET.get('q')
    if query:
        if query == 'all':
            pass
        else:
            context['items'] = StorageSixB.objects.filter(
                Q(item__icontains=query) | Q(location__icontains=query)
            )
    return render(request, "sixB.html", context)


def sixC(request):
    context = {}
    context['items'] = StorageSixC.objects.all()
    query = request.GET.get('q')
    if query:
        if query == 'all':
            pass
        else:
            context['items'] = StorageSixC.objects.filter(
                Q(item__icontains=query) | Q(location__icontains=query)
            )
    return render(request, "sixC.html", context)

def sixE(request):
    context = {}
    context['items'] = StorageSixE.objects.all()
    query = request.GET.get('q')
    if query:
        if query == 'all':
            pass
        else:
            context['items'] = StorageSixE.objects.filter(
                Q(item__icontains=query) | Q(location__icontains=query)
            )
    return render(request, "sixE.html", context)


# Add More rows to the sixA Table Handler View
@method_decorator(login_required, name='dispatch')
# CreateView refers to a view (logic) to create an instance of a table in the database.
class AddSixA(CreateView):
    model = StorageSixA
    form_class = SixAForm
    template_name = 'add.html'

    success_url = reverse_lazy('sixA')\

# Add More rows to the sixB Table Handler View
@method_decorator(login_required, name='dispatch')
# CreateView refers to a view (logic) to create an instance of a table in the database.
class AddSixB(CreateView):
    model = StorageSixB
    form_class = SixBForm
    template_name = 'add.html'

    success_url = reverse_lazy('sixB')

# Add More rows to the sixC Table Handler View
@method_decorator(login_required, name='dispatch')
# CreateView refers to a view (logic) to create an instance of a table in the database.
class AddSixC(CreateView):
    model = StorageSixC
    form_class = SixCForm
    template_name = 'add.html'

    success_url = reverse_lazy('sixC')

# Add More rows to the sixE Table Handler View
@method_decorator(login_required, name='dispatch')
# CreateView refers to a view (logic) to create an instance of a table in the database.
class AddSixE(CreateView):
    model = StorageSixE
    form_class = SixEForm
    template_name = 'add.html'

    success_url = reverse_lazy('sixE')


# Edit / Update existing rows
@method_decorator(login_required, name='dispatch')
# UpdateView refers to a view (logic) to update a particular instance of a table from the database with some extra details
class EditSixA(UpdateView):
    model = StorageSixA
    form_class = SixAForm
    template_name = 'edit.html'
    success_url = reverse_lazy('sixA')

@method_decorator(login_required, name='dispatch')
class EditSixB(UpdateView):
    model = StorageSixB
    form_class = SixBForm
    template_name = 'edit.html'
    success_url = reverse_lazy('sixB')

@method_decorator(login_required, name='dispatch')
class EditSixC(UpdateView):
    model = StorageSixC
    form_class = SixCForm
    template_name = 'edit.html'
    success_url = reverse_lazy('sixC')

@method_decorator(login_required, name='dispatch')
class EditSixE(UpdateView):
    model = StorageSixE
    form_class = SixEForm
    template_name = 'edit.html'
    success_url = reverse_lazy('sixE')

# Delete rows
@method_decorator(login_required, name='dispatch')    
# Delete View refers to a view (logic) to delete a particular instance of a table from the database
class DeleteSixA(DeleteView):
    model = StorageSixA
    template_name = 'delete.html'
    success_url = reverse_lazy('sixA')

@method_decorator(login_required, name='dispatch')
class DeleteSixB(DeleteView):
    model = StorageSixB
    template_name = 'delete.html'
    success_url = reverse_lazy('sixB')

@method_decorator(login_required, name='dispatch')
class DeleteSixC(DeleteView):
    model = StorageSixC
    template_name = 'delete.html'
    success_url = reverse_lazy('sixC')

@method_decorator(login_required, name='dispatch')
class DeleteSixE(DeleteView):
    model = StorageSixE
    template_name = 'delete.html'
    success_url = reverse_lazy('sixE')