from django.shortcuts import render
from .models import Question, Choice
from .serializers import QuestionSerializers, ChoiceSerializers
from rest_framework import generics


class QuestionViewSet(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializers


class ChoiceViewSet(generics.ListCreateAPIView):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializers
