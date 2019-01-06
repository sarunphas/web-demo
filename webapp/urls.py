from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('knowledges/', views.knowledges, name='knowledges'),
    path('programs/', views.programs, name='Programs'),
    path('publications/', views.publications, name='publications'),
    path('data/', views.data, name='data'),
   
]
