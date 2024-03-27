from django.urls import path
from .views import QuestionViewSet, ChoiceViewSet

# from . import views

app_name = "polls"

urlpatterns = [
    path("questions/", QuestionViewSet.as_view(), name="QuestionViewSet"),
    path("choices/", ChoiceViewSet.as_view(), name="ChoiceViewSet"),
]
