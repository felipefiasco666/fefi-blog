from django.contrib import admin
from .models import Topic,Entry
@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display=['name','date_added','image','owner']
    raw_id_fields=['owner']
    readonly_fields=['id']
admin.site.register(Entry)

# Register your models here.
