# Generated by Django 4.1.7 on 2023-03-17 14:20

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0003_alter_post_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='likes',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.BigIntegerField(blank=True, null=True), blank=True, null=True, size=None),
        ),
    ]
