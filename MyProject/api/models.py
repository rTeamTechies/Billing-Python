from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.title
