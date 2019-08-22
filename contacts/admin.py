from django.contrib import admin

# Register your models here.
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'listing', 'contact_date' )
    list_display_links = ('id', 'name')
    search_fields = ('name', 'email', 'listings')
    list_per_page = 20


admin.site.register (Contact, ContactAdmin)
