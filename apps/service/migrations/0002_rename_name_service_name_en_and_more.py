# Generated by Django 5.0.1 on 2024-05-02 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service',
            old_name='name',
            new_name='name_en',
        ),
        migrations.RenameField(
            model_name='singleservice',
            old_name='description',
            new_name='descriptio_ru',
        ),
        migrations.RenameField(
            model_name='singleservice',
            old_name='plan_standart',
            new_name='plan_standar_ru',
        ),
        migrations.RenameField(
            model_name='singleservice',
            old_name='plan_vip',
            new_name='plan_standart_en',
        ),
        migrations.AddField(
            model_name='service',
            name='name_ru',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='name_uz',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='singleservice',
            name='description_en',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='singleservice',
            name='description_uz',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='singleservice',
            name='plan_standart_uz',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='singleservice',
            name='plan_vip_en',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='singleservice',
            name='plan_vip_ru',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='singleservice',
            name='plan_vip_uz',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
    ]
