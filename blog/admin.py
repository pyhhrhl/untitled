from django.contrib import admin
from  .models import *

# Register your models here.
# 账号 admin 密码1
@admin.register(BlogType)
class BlogTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'type_name')

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id','title','blog_type','get_read_num','author','created_time')



