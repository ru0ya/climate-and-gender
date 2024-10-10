# Generated by Django 5.1.1 on 2024-10-08 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('healthfacilities', '0002_alter_healthfacilities_geom'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='healthfacilities',
            index=models.Index(fields=['geom'], name='geom_index'),
        ),
    ]
