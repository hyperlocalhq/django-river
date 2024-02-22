from django.contrib import admin
from django import forms

from river.models.transitionapprovalmeta import TransitionApprovalMeta


class TransitionApprovalMetaForm(forms.ModelForm):
    class Meta:
        model = TransitionApprovalMeta
        fields = ("workflow", "transition_meta", "permissions", "groups", "priority")


@admin.register(TransitionApprovalMeta)
class TransitionApprovalMetaAdmin(admin.ModelAdmin):
    form = TransitionApprovalMetaForm
    list_display = (
        "workflow",
        "get_transition_meta_display_slug",
        "get_transition_meta_display_verbose",
        "priority",
    )
    list_filter = ("workflow",)
    readonly_fields = (
        "get_transition_meta_display_slug",
        "get_transition_meta_display_verbose",
    )

    def get_transition_meta_display_verbose(self, obj):
        meta = obj.transition_meta
        return f"{meta.source_state} --> {meta.destination_state}"

    get_transition_meta_display_verbose.short_description = "Transition Meta (verbose)"

    def get_transition_meta_display_slug(self, obj):
        meta = obj.transition_meta
        return f"{meta.source_state.slug} --> {meta.destination_state.slug}"

    get_transition_meta_display_slug.short_description = "Transition Meta (slug)"
