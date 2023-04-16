from django.db import models

# Create your models here.


class JobData(models.Model):
    resumeText = models.CharField(max_length=3000)
    jobDesc = models.CharField(max_length=3000)
