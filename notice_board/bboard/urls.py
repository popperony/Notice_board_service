from django.urls import path

from .views import index, category


urlpatterns = [
        path('<int:category_id>/', category),
        path('', index),
    ]
