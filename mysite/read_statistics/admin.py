from django.contrib import admin
from .models import ReadNum, ReadDetail
from blog.models import Blog

@admin.register(ReadNum)
class ReadNumAdmin(admin.ModelAdmin):
    list_display = ('id', 'read_num', 'content_object')

@admin.register(ReadDetail)
class ReadDetailAdmin(admin.ModelAdmin):
    list_display = ('date', 'read_num', 'content_object')