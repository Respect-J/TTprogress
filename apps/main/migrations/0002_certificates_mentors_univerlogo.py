# Generated by Django 5.0.1 on 2024-05-01 13:23

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certificates',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, max_length=256, null=True)),
                ('img', models.FileField(blank=True, null=True, upload_to='img/certificates/')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Mentors',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, max_length=256, null=True)),
                ('work', models.CharField(blank=True, max_length=256, null=True)),
                ('img', models.ImageField(upload_to='img/mentors/')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UniverLogo',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, max_length=256, null=True)),
                ('img', models.FileField(blank=True, null=True, upload_to='img/logo/')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
