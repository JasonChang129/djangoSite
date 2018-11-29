from django.contrib import admin
from blog.models import *
# Register your models here.

class myAdmin(admin.ModelAdmin):
    list_display = ('id','title','price','color','publisher',)
    search_fields = ('title','price',)
    list_filter = ('title',)
    ordering = ('-id',)

admin.site.register(Book,myAdmin)