# Generated by Django 3.2.14 on 2022-08-21 07:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0004_learn_review_custom_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='learn_review_custom',
        ),
        migrations.DeleteModel(
            name='Voca',
        ),
    ]