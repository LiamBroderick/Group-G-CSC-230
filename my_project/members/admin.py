from django.contrib import admin
from .models import Exhibit
from .models import Section

# Register your models here.

class exhibitAdmin(admin.ModelAdmin):
  list_display = ("title", "description")

admin.site.register(Exhibit, exhibitAdmin)

class sectionAdmin(admin.ModelAdmin):
  list_display = ("title", "description")

admin.site.register(Section, sectionAdmin)