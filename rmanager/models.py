from django.db import models

class Sms(models.Model):
    to = models.BigIntegerField()
    text = models.TextField()