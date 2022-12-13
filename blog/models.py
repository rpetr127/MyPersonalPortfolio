from django.db import models

class Blog(models.Model):
    date = models.DateField(auto_now=True, editable=False)
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=2000)
