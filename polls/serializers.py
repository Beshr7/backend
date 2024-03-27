from rest_framework import serializers
from .models import Question, Choice


class QuestionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ("questionText", "datePublished")


class ChoiceSerializers(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ("FirstChoice", "SecChoice")
