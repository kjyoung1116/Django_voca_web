# Generated by Django 3.2.14 on 2022-08-18 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviewer', '0015_alter_review_settings_reviewing_intensity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review_settings',
            name='reviewing_intensity',
            field=models.CharField(choices=[('1', '짧게'), ('2', '기본'), ('3', '길게')], max_length=255),
        ),
    ]
