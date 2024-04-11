from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader
from .models import Exhibit
from .models import Section

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

def exhibits_page(request):
  exhibits = Exhibit.objects.all()
  return render(request, 'exhibits_page.html', {'exhibits': exhibits})

def science_of_play(request):
  template = loader.get_template('science_of_play.html')
  return HttpResponse(template.render())

def map(request):
  template = loader.get_template('map.html')
  return HttpResponse(template.render())
