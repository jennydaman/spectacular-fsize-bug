from django.db import models


class FooFile(models.Model):
    fname = models.FileField(max_length=1024, unique=True)
