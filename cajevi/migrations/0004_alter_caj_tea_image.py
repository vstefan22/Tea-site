# Generated by Django 3.2.9 on 2022-01-13 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cajevi', '0003_caj_tea_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caj',
            name='tea_image',
            field=models.ImageField(blank=True, null=True, upload_to='Images/'),
        ),
    ]
