from django.urls import path

from .views import index, category, BbCreateView


urlpatterns = [
        path('<int:category_id>/', category, name='categories'),
        path('', index, name='index'),
        path('add/', BbCreateView.as_view(), name='add')
    ]
