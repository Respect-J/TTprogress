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
    description_uz = models.TextField(null=True, blank=True)
    descriptio_ru = models.TextField(null=True, blank=True)
    description_en = models.TextField(null=True, blank=True)
    plan_vip_uz = models.CharField(max_length=512, null=True, blank=True)
    plan_vip_ru = models.CharField(max_length=512, null=True, blank=True)
    plan_vip_en = models.CharField(max_length=512, null=True, blank=True)
    plan_standart_uz = models.CharField(max_length=512, null=True, blank=True)
    plan_standar_ru = models.CharField(max_length=512, null=True, blank=True)
    plan_standart_en = models.CharField(max_length=512, null=True, blank=True)
    img = models.FileField(upload_to="img/singleservice/", null=True, blank=True)

    def __str__(self):
        return self.plan_vip_ru




