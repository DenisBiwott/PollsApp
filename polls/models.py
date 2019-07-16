from django.db import models
from django.utils import timezone
import datetime
from django_prometheus.models import ExportModelOperationsMixin

# Create your models here.


class Question(ExportModelOperationsMixin('question'), models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(ExportModelOperationsMixin('choice'), models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

    def __qes__(self):
        return self.question

    def __vot__(self):
        return self.votes
