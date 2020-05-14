from django.contrib import admin
django.contrib.auth.admin import UserAdmin
from .models import User

admin.site.register(User, UserAdmin)
