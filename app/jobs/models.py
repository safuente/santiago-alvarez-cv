from django.db import models


class Job(models.Model):
    """Class for manage jobs"""
    title = models.CharField(max_length=1000)
    company = models.CharField(max_length=1000)
    summary = models.TextField(max_length=5000)
    image = models.ImageField(upload_to='images/')
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.title


