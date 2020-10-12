

# Create your views here.

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Auto,Make
from .forms import MakeForm

class MainView(LoginRequiredMixin, View):
    def get(self, request):
        mc = Make.objects.all().count()
        al = Auto.objects.all()

        ctx = {'make_count': mc, 'auto_list': al}
        return render(request, 'autos/auto_list.html', ctx)


class MakeView(LoginRequiredMixin, View):
    def get(self, request):
        ml = Make.objects.all()
        ctx = {'make_list': ml}
        return render(request, 'autos/make_list.html', ctx)


#make views 

class MakeCreate(LoginRequiredMixin, View):
    template = 'autos/make_form.html'
    success_url = reverse_lazy('autos:all')

    def get(self, request):
        form = MakeForm()
        ctx = {'form': form}
        return render(request, self.template, ctx)

    def post(self, request):
        form = MakeForm(request.POST)
        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.template, ctx)

        make = form.save()
        return redirect(self.success_url)


class Makeiew(LoginRequiredMixin, UpdateView):
    model = Make
    fields = '__all__'
    success_url = reverse_lazy('autos:all')

class MakeUpdate(LoginRequiredMixin, UpdateView):
    model = Make
    fields = '__all__'
    success_url = reverse_lazy('autos:all')


class MakeDelete(LoginRequiredMixin, DeleteView):
    model = Make
    fields = '__all__'
    success_url = reverse_lazy('autos:all')

#Auto views

class Autoview(LoginRequiredMixin, UpdateView):
    model = Auto
    fields = '__all__'
    success_url = reverse_lazy('autos:all')

class AutoUpdate(LoginRequiredMixin, UpdateView):
    model = Auto
    fields = '__all__'
    success_url = reverse_lazy('autos:all')


class AutoDelete(LoginRequiredMixin, DeleteView):
    model = Auto
    fields = '__all__'
    success_url = reverse_lazy('autos:all')