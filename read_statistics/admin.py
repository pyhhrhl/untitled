from django.contrib import admin
from  .models import *

# Register your models here.

@admin.register(ReadNum)
class ReadNumAdmin(admin.ModelAdmin):
    list_display = ('id', 'read_num', 'content_type','object_id')

@admin.register(ReadDateDetail)
class ReadDateDetailAdmin(admin.ModelAdmin):
    list_display = ('id', 'read_num','date', 'content_type','object_id')