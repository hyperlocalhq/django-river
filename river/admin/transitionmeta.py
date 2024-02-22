from django import forms
from django.contrib import admin

from river.models import TransitionMeta


class TransitionMetaForm(forms.ModelForm):
    class Meta:
        model = TransitionMeta
        fields = ("workflow", "source_state", "destination_state")


@admin.register(TransitionMeta)
class TransitionMetaAdmin(admin.ModelAdmin):
    form = TransitionMetaForm
    list_display = (
        "workflow",
        "get_source_state_display",
        "get_destination_state_display",
    )
    list_filter = ("workflow",)
    search_fields = ("source_state__slug", "destination_state__slug")
    readonly_fields = ("get_source_state_display", "get_destination_state_display")

    def get_source_state_display(self, obj):
        return f"{obj.source_state} ({obj.source_state.slug})"

    get_source_state_display.short_description = "Source State"

    def get_destination_state_display(self, obj):
        return f"{obj.destination_state} ({obj.destination_state.slug})"

    get_destination_state_display.short_description = "Destination State"
