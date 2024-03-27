from django.contrib import admin
from .models import Choice, Question


class ChoiceInline(admin.TabularInline):
    model = Choice


class QuestionAdmin(admin.ModelAdmin):
    inlines = [
        ChoiceInline,
    ]
    extra = 2


admin.site.register(Choice)
admin.site.register(Question, QuestionAdmin)


# class QuestionAdmin(admin.ModelAdmin):
#     list_display = ("questionText", "getChoice")

#     def getChoice(self, obj):
#         return obj.choice.FirstChoice

#     getChoice.short_description = "Choice"
