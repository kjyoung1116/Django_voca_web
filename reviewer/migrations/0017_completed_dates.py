# Generated by Django 3.2.14 on 2022-08-21 08:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reviewer', '0016_alter_review_settings_reviewing_intensity'),
    ]

    operations = [
        migrations.CreateModel(
            name='completed_dates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('completed_date', models.DateField(auto_now_add=True)),
                ('plan_name', models.CharField(blank=True, default='', max_length=1000)),
                ('completed_or_not', models.CharField(blank=True, default='n', max_length=10)),
                ('today_quantity', models.CharField(blank=True, default='', max_length=1000)),
                ('goal_quantity', models.CharField(blank=True, default='', max_length=1000)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
