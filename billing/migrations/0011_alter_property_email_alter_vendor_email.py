# Generated by Django 4.1.7 on 2023-06-06 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0010_alter_property_email_alter_user_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='email',
            field=models.EmailField(max_length=30, verbose_name='Электронная почта'),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='email',
            field=models.EmailField(max_length=50, verbose_name='Электронная почта'),
        ),
    ]
