from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin

# Register your models here.
# class AccountUserAdmin(UserAdmin):
#     ordering = ("email",)
#     list_display = ["email", "first_name"]
#     add_fieldsets = (
#         (
#             None,
#             {
#                 "classes": ("wide",),
#                 "fields": (
#                     "email",
#                     "first_name",
#                     "last_name",
#                     "password1",
#                     "password2",
#                 ),
#             },
#         ),
#     )

#     def save_model(self, request, obj, form, change):
#         obj.set_password(obj.password)
#         super().save_model(request, obj, form, change)


admin.site.register(User)
