# Generated by Django 4.1.7 on 2023-06-10 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0018_alter_reading_reading_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reading',
            name='reading_value',
            field=models.FloatField(auto_created=True, blank=True, null=True, verbose_name='Значение считывания'),
        ),
    ]
