from django.contrib import admin

from .models import Category, Service


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ("name",)


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "provider_name",
        "category",
        "city",
        "is_approved",
        "created_at",
    )
    list_filter = ("category", "city", "is_approved", "created_at")
    search_fields = ("title", "provider_name", "city", "description")
    list_editable = ("is_approved",)
    prepopulated_fields = {"slug": ("title", "provider_name")}
