from django.contrib import admin
"""from django.contrib.auth.admin import UserAdmin

from Compilation.Forms.create_and_change import SignUpForm, CustomUserChangeForm
from Compilation.models import Account"""


"""class CustomUserAdmin(UserAdmin):
    add_form = SignUpForm
    form = CustomUserChangeForm
    model = Account
    list_display = ('email', 'is_staff', 'is_active',)
    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
"""

"""admin.site.register(Account, CustomUserAdmin)"""