from django.db import models
import uuid


class Config(models.Model):
    version = models.TextField(max_length=25, blank=False)
    description = models.TextField(blank=False)
    hyperparameters = models.TextField(blank=False)


class Task(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    configuration = models.ForeignKey(Config, on_delete=models.SET_NULL, related_name='configuration', null=True)
