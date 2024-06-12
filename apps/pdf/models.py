from django.db import models
from models import BaseModel
from django.core.exceptions import ValidationError


def validate_file_size(value):
    limit = 2 * 1024 * 1024  # 2 MB
    if value.size > limit:
        raise ValidationError('File too large. Size should not exceed 2 MB.')


class Data(BaseModel):
    title_ru = models.CharField(max_length=256, null=True, blank=True)
    date = models.FileField(upload_to="pdf/", null=True, blank=True, validators=[validate_file_size])


class RusData(Data):
    pass


class UzbData(Data):
    pass
