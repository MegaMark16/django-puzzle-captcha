from django.db import models

class Submission(models.Model):
    name = models.CharField(max_length=255)
    comments = models.TextField(blank=True, null=True)
    submission_date = models.DateField(auto_now_add=True)
