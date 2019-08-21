
from django.contrib import admin
from django.urls import path
from restaurants import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/',views.welcome ,name='hello-world'),
    path('restaurants/list/',views.restaurant_list ,name='restaurant-list'),
    path('restaurants_detail/<int:restaurant_id>/',views.restaurant_detail ,name='restaurant-detail'),
]
