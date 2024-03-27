from django.db import models
from datetime import datetime


class Question(models.Model):
    questionText = models.CharField(max_length=200, default="Question")
    datePublished = models.DateTimeField(
        "Date Published",
        default=datetime.now(),
    )


class Choice(models.Model):
    FirstChoice = models.CharField(max_length=200, default="First")
    SecChoice = models.CharField(max_length=200, default="Sec")
    question = models.ForeignKey(Question, null=True, on_delete=models.PROTECT)

    def __str__(self):
        return self.FirstChoice


# class ModelB(models.Model):
#     name = models.CharField(max_length=100)
#     model_a = models.ForeignKey(ModelA, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.name
