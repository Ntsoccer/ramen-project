# Generated by Django 3.1.1 on 2020-10-05 14:03

import django.core.validators
from django.db import migrations, models
import ramenapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('ramenapp', '0006_post_star'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='star',
            field=models.IntegerField(default=3, validators=[django.core.validators.MaxValueValidator(
                5), django.core.validators.MinValueValidator(1)], verbose_name='評価'),
        ),
    ]
