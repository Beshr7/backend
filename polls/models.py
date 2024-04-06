from django.db import models
from datetime import datetime


class Question(models.Model):
    questionText = models.CharField(max_length=200, default="Question")
    datePublished = models.DateTimeField(
        "Date Published",
        default=datetime.now(),
    )

    # choices = models.ManyToManyField(Choice)


class Choice(models.Model):
    FirstChoice = models.CharField(max_length=200, default="First")
    SecChoice = models.CharField(max_length=200, default="Sec")
    question = models.ManyToManyField(Question, through="QuestionChoices")

    def __str__(self):
        return self.FirstChoice


class QuestionChoices(models.Model):
    choice = models.ForeignKey(Choice, on_delete=models.PROTECT)
    question = models.ForeignKey(Question, on_delete=models.PROTECT)


# class ModelB(models.Model):
#     name = models.CharField(max_length=100)
#     model_a = models.ForeignKey(ModelA, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.name
