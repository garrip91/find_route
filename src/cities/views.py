from django.shortcuts import render, get_object_or_404

from cities.models import City

from django.views.generic.detail import DetailView



__all__ = (
    'home',
    'CityDetailView',
)



# Create your views here:
def home(request, pk=None):
    # if pk:
        # city = get_object_or_404(City, id=pk)
        # context = {'object': city}
        # return render(request, 'cities/detail.html', context)
    qs = City.objects.all()
    context = {'objects_list': qs}
    return render(request, 'cities/home.html', context)
    
    
    
class CityDetailView(DetailView):
    queryset = City.objects.all()
    template_name = 'cities/detail.html'