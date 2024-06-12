from django.db import models
from models import Language


class User(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    username = models.CharField(max_length=30)
    language = models.IntegerField(choices=Language.choices, default=Language.UNKNOWN)

    def __str__(self) -> str:
        return f"{self.username}"
