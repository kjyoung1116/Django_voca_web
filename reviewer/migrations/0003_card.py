# Generated by Django 3.2.14 on 2022-07-28 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviewer', '0002_auto_20220728_1525'),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=100)),
                ('answer', models.CharField(max_length=100)),
                ('box', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=1)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]