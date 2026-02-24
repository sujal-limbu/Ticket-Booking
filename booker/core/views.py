from django.shortcuts import render
from .models import Transportation

# Create your views here.
def index(request):
    return render(request,'core/index.html')

def book(request):
    transports = None

    start = request.GET.get('source')
    end = request.GET.get('destination')
    vehicle = request.GET.get('vehicle')

    if start and end:
        transports = Transportation.objects.filter(
            start__iexact=start,
            end__iexact=end
        )
        if vehicle:
            transports = transports.filter(vehicletype__Tname__iexact=vehicle)

    return render(request, 'core/book.html', {'transports': transports})