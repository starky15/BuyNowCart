from django.contrib import admin
from .models import Account


# if in case we need to customize the admin area..
# for eg: currently password is editable
# so we want it to be not editable
# so we will use below way:
from django.contrib.auth.admin import UserAdmin

class AccountAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'username', 'date_joined', 'last_login', 'is_active')
    filter_horizontal = ()
    list_filter = ()
    fieldsets= ()
# till here we have the bare minimum settings

#some more changes to make fn, ln clickable
    list_display_links = ('email', 'first_name', 'last_name')

#to make f readonly
    readonly_fields = ('date_joined', 'last_login')


# Register your models here.
admin.site.register(Account, AccountAdmin)
