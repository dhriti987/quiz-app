from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
USER_MODEL = get_user_model()


class Question(models.Model):
    class OptionChoices(models.IntegerChoices):
        OPTION1 = 1
        OPTION2 = 2
        OPTION3 = 3
        OPTION4 = 4
    question = models.CharField(max_length=256)
    option_1 = models.CharField(max_length=256)
    option_2 = models.CharField(max_length=256)
    option_3 = models.CharField(max_length=256)
    option_4 = models.CharField(max_length=256)
    correct_option = models.PositiveSmallIntegerField(choices=OptionChoices)


class Submission(models.Model):
    user = models.ForeignKey(
        USER_MODEL, on_delete=models.CASCADE, related_name='submissions')
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name='submissions')
    is_correct = models.BooleanField()
