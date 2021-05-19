from django.shortcuts import render, get_object_or_404

from trains.models import Train

from django.views.generic.detail import DetailView

from trains.forms import TrainForm

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy

from django.core.paginator import Paginator

from django.views.generic import (
    DetailView, CreateView, UpdateView, DeleteView,
    ListView
)

from django.contrib.messages.views import SuccessMessageMixin

from django.contrib import messages

from django.contrib.auth.mixins import LoginRequiredMixin


__all__ = (
    'home',
    'TrainListView',
    'TrainDetailView',
    'TrainCreateView',
    'TrainUpdateView',
    'TrainDeleteView',
)


# Create your views here:
def home(request, pk=None):
    qs = Train.objects.all()
    lst = Paginator(qs, 10)
    page_number = request.GET.get('page')
    page_obj = lst.get_page(page_number)
    context = {'page_obj': page_obj, }
    return render(request, 'trains/home.html', context)


class TrainListView(ListView):
    paginate_by = 10
    model = Train
    template_name = 'trains/home.html'


class TrainDetailView(DetailView):
    queryset = Train.objects.all()
    template_name = 'trains/detail.html'


class TrainCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Train
    form_class = TrainForm
    template_name = 'trains/create.html'
    success_url = reverse_lazy('trains:home')
    success_message = "Название поезда успешно добавлено!"


class TrainUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Train
    form_class = TrainForm
    template_name = 'trains/update.html'
    success_url = reverse_lazy('trains:home')
    success_message = "Название поезда успешно изменено!"


class TrainDeleteView(LoginRequiredMixin, DeleteView):
    model = Train
    # template_name = 'trains/delete.html'
    success_url = reverse_lazy('trains:home')

    def get(self, request, *args, **kwargs):
        messages.success(request, "Название поезда успешно удалено!")
        return self.post(request, *args, **kwargs)
