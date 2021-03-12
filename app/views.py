from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import Home
from .serializers import HomeSerializer
from rest_framework.renderers import JSONRenderer
# Create your views here.

# Model Object - single Student Data

def home(request, pk):
    hom = Home.objects.get(id=pk)
    serializer = HomeSerializer(hom)
    # json_data = JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data, content_type='application/json')
    return JsonResponse(serializer.data)

def all(request):
    hom = Home.objects.all()
    serializer = HomeSerializer(hom, many=True)
    # json_data = JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data,content_type='application/json')
    return JsonResponse(serializer.data,safe=False)
