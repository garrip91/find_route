from django.shortcuts import render

from routes.forms import RouteForm, RouteModelForm

from django.contrib import messages

from routes.utils import get_routes

from django.shortcuts import redirect

from trains.models import Train
from cities.models import City
from routes.models import Route

from django.views.generic import ListView, DetailView

from django.contrib.auth.decorators import login_required

from django.views.generic.edit import DeleteView

from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here:
# @login_required
def home(request):
    form = RouteForm()
    return render(request, 'routes/home.html', {'form': form})


def find_routes(request):
    if request.method == 'POST':
        form = RouteForm(request.POST)
        print(form)
        if form.is_valid():
            try:
                context = get_routes(request, form)
            except ValueError as e:
                messages.error(request, e)
                return render(request, 'routes/home.html', {'form': form})
            return render(request, 'routes/home.html', context)
        return render(request, 'routes/home.html', {'form': form})
    else:
        form = RouteForm()
        messages.error(request, "Нет данных для поиска!")
        return render(request, 'routes/home.html', {'form': form})


def add_route(request):
    if request.method == 'POST':
        context = {}
        data = request.POST
        if data:
            total_time = int(data['total_time'])
            from_city_id = int(data['from_city'])
            to_city_id = int(data['to_city'])
            trains = data['trains'].split(', ')
            trains_list = [int(t) for t in trains if t.isdigit()]
            qs = Train.objects.filter(id__in=trains_list).select_related(
                'from_city', 'to_city')
            cities = City.objects.filter(
                id__in=[from_city_id, to_city_id]).in_bulk()
            form = RouteModelForm(
                initial={
                    'from_city': cities[from_city_id],
                    'to_city': cities[to_city_id],
                    'travel_times': total_time,
                    'trains': qs
                }
            )
            context['form'] = form
        return render(request, 'routes/create.html', context)
    else:
        messages.error(request, "Невозможно сохранить несуществующий маршрут!")
        return redirect('/')
        
        
def save_route(request):
    if request.method == 'POST':
        form = RouteModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Маршрут успешно сохранён!")
        return redirect('/')
        return render(request, 'routes/create.html', {'form': form})
    else:
        messages.error(request, "Невозможно сохранить несуществующий маршрут!")
        return redirect('/')


class RouteListView(ListView):
    paginate_by = 10
    model = Route
    template_name = 'routes/list.html'
    
    
class RouteDetailView(DetailView):
    queryset = Route.objects.all()
    template_name = 'routes/detail.html'
    
    
class RouteDeleteView(LoginRequiredMixin, DeleteView):
    model = Route
    success_url = reverse_lazy('home')

    def get(self, request, *args, **kwargs):
        messages.success(request, "Маршрут успешно удалён!")
        return self.post(request, *args, **kwargs)