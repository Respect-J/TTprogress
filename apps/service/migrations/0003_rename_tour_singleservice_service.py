# Generated by Django 5.0.1 on 2024-05-02 10:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0002_rename_name_service_name_en_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='singleservice',
            old_name='tour',
            new_name='service',
        ),
    ]
