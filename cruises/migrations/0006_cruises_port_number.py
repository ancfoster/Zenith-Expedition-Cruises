# Generated by Django 3.2.18 on 2023-04-17 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cruises', '0005_auto_20230405_1748'),
    ]

    operations = [
        migrations.AddField(
            model_name='cruises',
            name='port_number',
            field=models.PositiveSmallIntegerField(default=2, verbose_name='Number of Ports'),
            preserve_default=False,
        ),
    ]