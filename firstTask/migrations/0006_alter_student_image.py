# Generated by Django 4.1.7 on 2023-03-01 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstTask', '0005_student_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
