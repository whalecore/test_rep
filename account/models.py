from django.db import models

# Create your models here.
class Text(models.Model):
    text = models.TextField()

class Title(models.Model):
    title = models.CharField(max_length=200)
    text = models.ForeignKey(Text, on_delete=models.CASCADE)

class Something(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    desc = models.TextField()