from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Section, Option


def menu(request):
    section_list = Section.objects.all()
    option_list = Option.objects.all()
    context = {}
    context['section_list'] = section_list
    context['option_list'] = option_list
    return render(request, 'menu/menu_editor.html', context)

def inventory(request):
    context = {}
    context['option_list'] = Option.objects.all()
    return render(request, 'menu/inventory.html', context)
