# Generated by Django 3.2.14 on 2022-08-18 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviewer', '0014_auto_20220818_2120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review_settings',
            name='reviewing_intensity',
            field=models.CharField(choices=[('짧게', '짧게'), ('기본', '기본'), ('길게', '길게')], max_length=255),
        ),
    ]
