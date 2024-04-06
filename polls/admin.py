from django.contrib import admin
from .models import Choice, Question, QuestionChoices


class QuestionChoicesInline(admin.TabularInline):
    model = QuestionChoices


class QuestionAdmin(admin.ModelAdmin):
    inlines = [
        QuestionChoicesInline,
    ]
    extra = 2


class ChoiceAdmin(admin.ModelAdmin):

    class Meta:
        model = Choice
        fields = "__all__"


# admin.site.register(QuestionChoices)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)

# class QuestionAdmin(admin.ModelAdmin):
#     list_display = ("questionText", "getChoice")

#     def getChoice(self, obj):
#         return obj.choice.FirstChoice

#     getChoice.short_description = "Choice"
