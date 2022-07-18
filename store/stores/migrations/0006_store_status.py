# Generated by Django 4.0.6 on 2022-07-17 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0005_rename_creator_store_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='status',
            field=models.CharField(choices=[('active', 'Active'), ('deactivated', 'Deactivated'), ('in_review', 'In review')], default='in_review', max_length=20),
        ),
    ]