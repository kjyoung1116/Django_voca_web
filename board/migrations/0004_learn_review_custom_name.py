# Generated by Django 3.2.14 on 2022-07-28 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0003_learn_review_custom_delete_learn_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='learn_review_custom',
            name='name',
            field=models.CharField(default=1, help_text='커스텀 플랜의 이름을 입력하세요.', max_length=10),
            preserve_default=False,
        ),
    ]
