# Generated by Django 4.1.7 on 2023-03-01 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstTask', '0007_result'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='subject',
            field=models.CharField(default='', max_length=255),
        ),
    ]
