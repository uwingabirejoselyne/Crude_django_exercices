# Generated by Django 4.1.7 on 2023-03-01 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstTask', '0006_alter_student_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Regno', models.IntegerField()),
                ('course', models.CharField(max_length=200)),
                ('marks', models.IntegerField()),
            ],
        ),
    ]