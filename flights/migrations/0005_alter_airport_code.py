# Generated by Django 5.0.6 on 2024-06-06 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0004_rename_second_passenger_last'),
    ]

    operations = [
        migrations.AlterField(
            model_name='airport',
            name='code',
            field=models.CharField(max_length=30),
        ),
    ]
