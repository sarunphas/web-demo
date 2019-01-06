from django.shortcuts import render
from .models import Image
from django.http import HttpResponse
from rest_framework import viewsets
from .serializers import ImageSerializer
def get_image_list(request):
    image_list = Image.objects.all()
    context = {"image_list":image_list}
    return render(request, 'images/image_list.html' , context)

def get_image(request, slug):
    image = Image.objects.filter(slug=slug).first()
    context = {"image":image}
    return render(request, 'images/image.html' , context)

class ImageView(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

    
    
