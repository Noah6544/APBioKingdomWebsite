from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse

from .models import *

def IndexView(request):
    domains = Domain.objects.all().order_by('id')
    #return(HttpResponse("Index view"))
    return render(request,'contentpages/domainlist.html',context={'domain': domains})

def DomainView(request,domain_id):
    try:
        CurrentDomain = Domain.objects.get(pk=domain_id)
        CurrentSubheading = Subheading.objects.filter(Domain=CurrentDomain)
        CurrentImageList = Images.objects.filter(Domain=CurrentDomain)
    except (KeyError,Domain.DoesNotExist):
        print("Domain object doesn't exist")
    else:
        print("banana")
        return render(request,'contentpages/domainbase.html',context={'domain':CurrentDomain,'subheading':CurrentSubheading,'image_list': CurrentImageList})

def SourceView(request):
    return render(request,'contentpages/sources.html',context={})
