# Generated by Django 2.2.4 on 2019-09-01 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='pub_time',
            field=models.DateTimeField(verbose_name='date published'),
        ),
    ]