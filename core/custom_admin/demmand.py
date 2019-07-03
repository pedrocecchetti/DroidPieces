from django.contrib import admin
from django.db import models


class DemmandCustomAdmin(admin.ModelAdmin):
    # The forms to add and change gallery instances
    empty_value_display = "----"

    readonly_fields = ["announcer", "created_at", "updated_at"]

    # The fields to be used in displaying the Gallery model.
    list_display = ("description", "announcer", "is_finalized", "deliver_address",)
    list_filter = ("announcer", "description", "deliver_address", "created_at", "updated_at")

    # The fields to be used in updates on Gallery model.
    fieldsets = (
        (
            "Informações básicas",
            {
                "classes": ("grp-collapse grp-open",),
                "fields": ("description","deliver_address", "is_finalized"),
            },
        ),
        (
            "Monitoramento",
            {
                "classes": ("grp-collapse grp-open",),
                "fields": ("announcer", "created_at", "updated_at",),
            },
        ),
    )

    # Search and ordering
    search_fields = ("announcer", "created_at", "updated_at")
    ordering = ("announcer", "created_at","description")

    def save_model(self, request, demmand, form, change):
        if not demmand.created_at:
            demmand.announcer = request.user
        

        super().save_model(request, demmand, form, change)
