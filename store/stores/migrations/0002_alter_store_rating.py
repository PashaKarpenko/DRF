# Generated by Django 4.0.6 on 2022-07-17 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='rating',
            field=models.IntegerField(),
        ),
    ]