# Generated by Django 4.0.4 on 2022-06-17 14:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='profile',
        ),
    ]