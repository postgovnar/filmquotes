from django.db import models

class Sources(models.Model):
    quote = models.TextField()
    usage = models.IntegerField()
    pass

class Quotes(models.Model):
    quote = models.TextField()
    source = models.ForeignKey(Sources, on_delete = models.CASCADE)
    weight = models.IntegerField()
    add_date = models.DateTimeField()
    views = models.IntegerField()
    likes = models.IntegerField()
    dislikes = models.IntegerField()
