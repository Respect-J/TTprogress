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


class Hero(BaseModel):
    title_top_uz = models.CharField(max_length=1024, null=True, blank=True)
    title_bottom_uz = models.CharField(max_length=1024, null=True, blank=True)
    title_sub_uz = models.CharField(max_length=1024, null=True, blank=True)
    title_top_ru = models.CharField(max_length=1024, null=True, blank=True)
    title_bottom_ru = models.CharField(max_length=1024, null=True, blank=True)
    title_sub_ru = models.CharField(max_length=1024, null=True, blank=True)
    title_top_en = models.CharField(max_length=1024, null=True, blank=True)
    title_bottom_en = models.CharField(max_length=1024, null=True, blank=True)
    title_sub_en = models.CharField(max_length=1024, null=True, blank=True)

    def __str__(self):
        return self.title_top_ru


class Stats(BaseModel):
    title_top_uz = models.CharField(max_length=1024, null=True, blank=True)
    title_bottom_uz = models.CharField(max_length=1024, null=True, blank=True)
    title_top_ru = models.CharField(max_length=1024, null=True, blank=True)
    title_bottom_ru = models.CharField(max_length=1024, null=True, blank=True)
    title_top_en = models.CharField(max_length=1024, null=True, blank=True)
    title_bottom_en = models.CharField(max_length=1024, null=True, blank=True)
    img = models.FileField(upload_to="img/stats/", null=True, blank=True)

    def __str__(self):
        return self.title_top_ru


class WhyUs(BaseModel):
    title_top_uz = models.CharField(max_length=1024, null=True, blank=True)
    title_bottom_uz = models.CharField(max_length=1024, null=True, blank=True)
    title_top_ru = models.CharField(max_length=1024, null=True, blank=True)
    title_bottom_ru = models.CharField(max_length=1024, null=True, blank=True)
    title_top_en = models.CharField(max_length=1024, null=True, blank=True)
    title_bottom_en = models.CharField(max_length=1024, null=True, blank=True)
    img = models.FileField(upload_to="img/whyUs/", null=True, blank=True)

    def __str__(self):
        return self.title_top_ru


class About(BaseModel):
    img = models.FileField(upload_to="img/about/")
    title_1_uz = models.CharField(max_length=1024, null=True, blank=True)
    title_1_ru = models.CharField(max_length=1024, null=True, blank=True)
    title_1_en = models.CharField(max_length=1024, null=True, blank=True)
    text_1_uz = models.TextField(null=True, blank=True)
    text_1_ru = models.TextField(null=True, blank=True)
    text_1_en = models.TextField(null=True, blank=True)
    title_2_uz = models.CharField(max_length=1024, null=True, blank=True)
    title_2_ru = models.CharField(max_length=1024, null=True, blank=True)
    title_2_en = models.CharField(max_length=1024, null=True, blank=True)
    text_2_uz = models.TextField(null=True, blank=True)
    text_2_ru = models.TextField(null=True, blank=True)
    text_2_en = models.TextField(null=True, blank=True)
    title_3_uz = models.CharField(max_length=1024, null=True, blank=True)
    title_3_ru = models.CharField(max_length=1024, null=True, blank=True)
    title_3_en = models.CharField(max_length=1024, null=True, blank=True)
    text_3_uz = models.TextField(null=True, blank=True)
    text_3_ru = models.TextField(null=True, blank=True)
    text_3_en = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title_1_ru


class AboutMentors(BaseModel):
    img = models.FileField(upload_to="img/about_mentors/")
    title_uz = models.CharField(max_length=1024, null=True, blank=True)
    title_ru = models.CharField(max_length=1024, null=True, blank=True)
    title_en = models.CharField(max_length=1024, null=True, blank=True)
    text_1_uz = models.TextField(null=True, blank=True)
    text_1_ru = models.TextField(null=True, blank=True)
    text_1_en = models.TextField(null=True, blank=True)
    text_2_uz = models.TextField(null=True, blank=True)
    text_2_ru = models.TextField(null=True, blank=True)
    text_2_en = models.TextField(null=True, blank=True)
    text_3_uz = models.TextField(null=True, blank=True)
    text_3_ru = models.TextField(null=True, blank=True)
    text_3_en = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title_ru
