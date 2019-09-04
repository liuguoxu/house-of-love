from django.db import models


# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_time = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text


class Choice(models.Model):

    # 通过related_name可以指定外键在另一个model中的引用名字， 默认为'foo_set'
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choice_set')
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
