from django.db import models
from django.utils import timezone


class Book(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    in_stock = models.TextField(default='yes')
    created_date = models.DateTimeField(
        default=timezone.now)
    section = models.TextField(default='other')

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
    
