# Generated by Django 3.2.18 on 2023-04-18 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cruises', '0006_cruises_port_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cruises',
            name='description',
            field=models.TextField(max_length=360, verbose_name='Cruise Description'),
        ),
    ]