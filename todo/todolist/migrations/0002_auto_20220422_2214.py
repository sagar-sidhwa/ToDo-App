# Generated by Django 3.0.1 on 2022-04-22 16:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='createdon',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
