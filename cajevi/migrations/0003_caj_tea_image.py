# Generated by Django 3.2.9 on 2022-01-13 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cajevi', '0002_auto_20220104_0006'),
    ]

    operations = [
        migrations.AddField(
            model_name='caj',
            name='tea_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
