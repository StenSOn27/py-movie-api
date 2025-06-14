from django.contrib import admin
from .models import Movie


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "duration",)
    search_fields = ("title",)
    list_filter = ("duration",)
