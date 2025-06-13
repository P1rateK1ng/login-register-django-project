from django.contrib import admin
from .models import User

@admin.register(User)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'fullname', 'email', 'role', 'status', 'created_at')
    search_fields = ('email', 'fullname')
    list_filter = ('role', 'status')
