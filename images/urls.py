from django.urls import include, path

from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('images', views.ImageView)

app_name = 'images'
urlpatterns = [

    path('', views.get_image_list, name='get_image_list'),
    path('<str:slug>/', views.get_image, name='get_image'),
    path('api/', include(router.urls)),
]

