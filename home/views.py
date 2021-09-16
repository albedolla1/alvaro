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


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


def home(request):
    context = {}
    context['sixa'] = StorageSixA.objects.all()    
    context['sixb'] = StorageSixB.objects.all()    
    context['sixc'] = StorageSixC.objects.all()    
    context['sixe'] = StorageSixE.objects.all()    
    return render(request, "index.html", context)


def sixA(request):
    context = {}
    context['items'] = StorageSixA.objects.all()
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


# Add
@method_decorator(login_required, name='dispatch')
class AddSixA(CreateView):
    model = StorageSixA
    form_class = SixAForm
    template_name = 'add.html'

    success_url = reverse_lazy('sixA')\

@method_decorator(login_required, name='dispatch')
class AddSixB(CreateView):
    model = StorageSixB
    form_class = SixBForm
    template_name = 'add.html'

    success_url = reverse_lazy('sixB')

@method_decorator(login_required, name='dispatch')
class AddSixC(CreateView):
    model = StorageSixC
    form_class = SixCForm
    template_name = 'add.html'

    success_url = reverse_lazy('sixC')

@method_decorator(login_required, name='dispatch')
class AddSixE(CreateView):
    model = StorageSixE
    form_class = SixEForm
    template_name = 'add.html'

    success_url = reverse_lazy('sixE')


# Edit
@method_decorator(login_required, name='dispatch')
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

# Delete
@method_decorator(login_required, name='dispatch')    
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