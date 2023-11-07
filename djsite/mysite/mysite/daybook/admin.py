from django.contrib import admin
from .models import Record

class RecordAdmin(admin.ModelAdmin):
    list_display = ('title','content','photo', 'is_published')

admin.site.register(Record, RecordAdmin)
