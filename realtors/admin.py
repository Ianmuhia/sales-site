from django.contrib import admin
# Register your models here.
from .models import Realtors

class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id','name','email','hire_date')
    list_display_links = ('id','name')
    search_fields = ('name',)
    list_per_page = 20
    list_filter = ('name',)

admin.site.register(Realtors, RealtorAdmin)
