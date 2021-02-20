from django.db import models


class MyModel(models.Model):
    name = models.CharField(max_length=20, help_text="Enter field documentation")

