from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Bb


def index(request):
    template = loader.get_template('index.html')
    bboards = Bb.objects.order_by('-published')
    context = {'bboards': bboards}
    return HttpResponse(template.render(context, request))
