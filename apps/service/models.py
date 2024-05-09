from django.db import models
from models import BaseModel


class Service(models.Model):
    id = models.AutoField(primary_key=True)
    name_ru = models.CharField(max_length=256, null=True, blank=True)
    name_en = models.CharField(max_length=256, null=True, blank=True)
    name_uz = models.CharField(max_length=256, null=True, blank=True)
    img = models.FileField(upload_to="img/service/", null=True, blank=True)

    def __str__(self):
        return self.name_ru


class SingleService(BaseModel):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    name_ru = models.CharField(max_length=256, null=True, blank=True)
    name_en = models.CharField(max_length=256, null=True, blank=True)
    name_uz = models.CharField(max_length=256, null=True, blank=True)
    description_uz = models.TextField(null=True, blank=True)
    description_ru = models.TextField(null=True, blank=True)
    description_en = models.TextField(null=True, blank=True)
    img = models.FileField(upload_to="img/singleservice/", null=True, blank=True)

    def __str__(self):
        return self.name_ru


class Plan(BaseModel):
    single = models.ForeignKey(SingleService, on_delete=models.CASCADE)
    name_ru = models.CharField(max_length=256, null=True, blank=True)
    name_en = models.CharField(max_length=256, null=True, blank=True)
    name_uz = models.CharField(max_length=256, null=True, blank=True)
    description_uz = models.TextField(null=True, blank=True)
    description_ru = models.TextField(null=True, blank=True)
    description_en = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name_ru


class PlanVip(Plan):
    pass


class PlanStandart(Plan):
    pass


