import uuid
from django.db import models


class Language(models.IntegerChoices):
    UNKNOWN = 0
    UZ = 1
    RU = 2


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)


    class Meta:
        abstract = True
