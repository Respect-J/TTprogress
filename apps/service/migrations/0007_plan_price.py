# Generated by Django 5.0.1 on 2024-06-12 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0006_remove_plan_created_at_remove_plan_updated_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='plan',
            name='price',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
    ]
