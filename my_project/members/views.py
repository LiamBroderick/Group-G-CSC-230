from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader
from .models import Exhibit

# Create your views here.

def members(request):
  mymembers = Member.objepycts.all().values()
  template = loader.get_template('all_members.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))
  
def details(request, id):
  mymember = Member.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

  return HttpResponse(template.render(context, request))
def exhibits_page(request):
  exhibits = Exhibit.objects.all()
  return render(request, 'exhibits_page.html', {'exhibits': exhibits})
