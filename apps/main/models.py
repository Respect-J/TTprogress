from django.db import models
from models import BaseModel


class Contacts(BaseModel):
    first_contact = models.CharField(max_length=256)
    second_contact = models.CharField(max_length=256)

    def __str__(self):
        return self.first_contact


