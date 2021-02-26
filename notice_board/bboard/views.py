from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Bb, Category


def index(request):
    bboards = Bb.objects.all()
    category = Category.objects.all()
    context = {'bboards': bboards, 'category': category}
    return render(request, 'index.html', context)


def category(request, category_id):
    bboards = Bb.objects.filter(category=category_id)
    category = Category.objects.all()
    current_category = Category.objects.get(pk=category_id)
    context = {
        'bboards': bboards,
        'category': category,
        'current_category': current_category
        }
    return render(request, 'category.html', context)
