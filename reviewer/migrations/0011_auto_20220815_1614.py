# Generated by Django 3.2.14 on 2022-08-15 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviewer', '0010_auto_20220815_1607'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='addition8',
            field=models.CharField(blank=True, default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='card',
            name='review_date',
            field=models.DateField(default=None),
            preserve_default=False,
        ),
    ]
