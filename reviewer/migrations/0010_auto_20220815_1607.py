# Generated by Django 3.2.14 on 2022-08-15 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviewer', '0009_review_settings_plan_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card',
            name='addition8',
        ),
        migrations.AlterField(
            model_name='card',
            name='answer',
            field=models.CharField(blank=True, default=None, max_length=1000),
            preserve_default=False,
        ),
    ]