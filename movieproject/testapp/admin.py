from django.contrib import admin
from testapp.models import moviemodel

class movieAdmin(admin.ModelAdmin):
    list_display=['moviename','rating']


# Register your models here.
admin.site.register(moviemodel,movieAdmin)
