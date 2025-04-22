from django.db import models

class Project(models.Model):
    topic = models.CharField(max_length=200)
    languages_used = models.TextField()
    duration_weeks = models.IntegerField()

    def _str_(self):
        return f"{self.topic} | Languages: {self.languages_used} | Duration: {self.duration_weeks} weeks"

# Create your models here.
