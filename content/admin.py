from django.contrib import admin
from .models import *





class SubheadingInLine(admin.TabularInline):
    model = Subheading

class DomainAdmin(admin.ModelAdmin):
    fieldsets = [
        ("General information", {'fields': ['title','description']}),
        ("Specific Information", {'fields': ['characteristics','divergent_event','cell_type',
         'body_plan','metabolism','circulatory','respiratory','reproduction','examples','keytraits','vocabulary']})
    ]
    inlines = [SubheadingInLine]


admin.site.register(Domain,DomainAdmin)
admin.site.register(Images)
