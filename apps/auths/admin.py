from django.contrib import admin
from auths.models import Contact


# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ("email", "name")


admin.site.register(Contact, ContactAdmin)
