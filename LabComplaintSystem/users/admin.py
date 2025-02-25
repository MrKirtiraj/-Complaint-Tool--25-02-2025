from django.contrib import admin

# Register your models here.
from users.models import UserProfile
class admin1(admin.ModelAdmin):
    list_display = ("ROLE_CHOICES", "role", "phone")

admin.site.register(UserProfile,admin1)