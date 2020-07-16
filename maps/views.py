from django.shortcuts import render

# Create your views here.


def maps(request):
    return render(request, 'maps/map.html')
