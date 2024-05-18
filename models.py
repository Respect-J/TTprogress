import uuid
from django.utils import timezone
from django.db import models


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)


    class Meta:
        abstract = True
