from django.contrib import admin

from fl_tag.models import Tag


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("label", "content_type", "object_id")

    class Meta:
        model = Tag
        fields = ("label", "content_type", "object_id")

