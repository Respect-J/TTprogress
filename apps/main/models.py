from django.db import models
from models import BaseModel


class Contacts(BaseModel):
    first_contact = models.CharField(max_length=256)
    second_contact = models.CharField(max_length=256)

    def __str__(self):
        return self.first_contact


class Certificates(BaseModel):
    name_ru = models.CharField(max_length=256, null=True, blank=True)
    img = models.FileField(upload_to="img/certificates/", null=True, blank=True)

    def __str__(self):
        return self.name_ru


class Mentors(BaseModel):
    name_ru = models.CharField(max_length=256, null=True, blank=True)
    name_en = models.CharField(max_length=256, null=True, blank=True)
    name_uz = models.CharField(max_length=256, null=True, blank=True)
    work_ru = models.CharField(max_length=256, null=True, blank=True)
    work_en = models.CharField(max_length=256, null=True, blank=True)
    work_uz = models.CharField(max_length=256, null=True, blank=True)
    img = models.ImageField(upload_to="img/mentors/")

    def __str__(self):
        return self.name_ru


class UniverLogo(BaseModel):
    name_ru = models.CharField(max_length=256, null=True, blank=True)
    name_en = models.CharField(max_length=256, null=True, blank=True)
    name_uz = models.CharField(max_length=256, null=True, blank=True)
    img = models.FileField(upload_to="img/logo/", null=True, blank=True)

    def __str__(self):
        return self.name_ru
