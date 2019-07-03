from django.contrib import admin
from django.db import models


class AddressCustomAdmin(admin.ModelAdmin):
    # The forms to add and change gallery instances
    empty_value_display = "----"

    readonly_fields = ["country"]

    # The fields to be used in displaying the Gallery model.
    list_display = ("street", "city", "state", "zip_code")
    list_filter = ("state", "city", "zip_code")

    # The fields to be used in updates on Gallery model.
    fieldsets = (
        (
            "Informações básicas",
            {
                "classes": ("grp-collapse grp-open",),
                "fields": ("country", "state", "city", "street", "number", "zip_code"),
            },
        ),
    )

    # Search and ordering
    search_fields = ("zip_code", "city", "state")
    ordering = ("state","city")