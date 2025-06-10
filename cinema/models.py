from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField()
    duration = models.PositiveIntegerField()

    def __str__(self):
        return f"Title: {self.title}, duration {self.duration} mins."
