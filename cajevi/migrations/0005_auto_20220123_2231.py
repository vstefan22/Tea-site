# Generated by Django 3.2.9 on 2022-01-23 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cajevi', '0004_alter_caj_tea_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='caj',
            name='price_with_shipping',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='caj',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=4),
        ),
    ]
