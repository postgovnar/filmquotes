from django.utils.timezone import now

from django.db import models

class Sources(models.Model):
    source = models.CharField(unique=True)
    usage = models.IntegerField(default=0)

    def  __str__(self):
        return self.source

class Quotes(models.Model):
    quote = models.TextField(unique=True)
    source = models.ForeignKey(Sources, on_delete = models.CASCADE)
    weight = models.IntegerField(default=1)
    add_date = models.DateTimeField(default=now)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)

    def  __str__(self):
        return f'Цитата из {self.source}'

