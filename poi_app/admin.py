from django.contrib import admin
from .models import PointOfInterest
# Register your models here.

# additional for admin
@admin.register(PointOfInterest)
class PointOfInterestAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'created_at')
    search_fields = ('name', 'category')