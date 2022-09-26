from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import FirstApp


def index(request):
    mymembers = FirstApp.objects.all().values()
    template = loader.get_template('index.html')
    context = {
        'mymembers': mymembers,
    }
    return HttpResponse(template.render(context, request))

def add(request):
    template = loader.get_template('add.html')
    return HttpResponse(template.render({}, request))

def addrecord(request):
    x = request.POST['first']
    y = request.POST['last']
    member = FirstApp(firstname = x, lastname = y)
    member.save()
    return HttpResponseRedirect(reverse('index'))

def delete(request, id):
    member = FirstApp.objects.get(id=id)
    member.delete()
    return HttpResponseRedirect(reverse('index'))

def update(request, id):
    mymember = FirstApp.objects.get(id=id)
    template = loader.get_template('update.html')
    context = {
        'mymember':mymember,
    }
    return HttpResponse(template.render(context, request))

def updaterecord(request, id):
    first = request.POST['first']
    last = request.POST['last']
    member = FirstApp.objects.get(id=id)
    member.firstname = first
    member.lastname = last
    member.save()
    return HttpResponseRedirect(reverse('index'))

def testing(request):
    mymembers = FirstApp.objects.all().values()

    template = loader.get_template('template.html')
    context = {
        'mymembers': mymembers,
    }
    return HttpResponse(template.render(context, request))