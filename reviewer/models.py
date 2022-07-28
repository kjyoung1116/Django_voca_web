from asyncio import selector_events
from django.db import models
from platformdirs import user_cache_dir
from django.contrib.auth.models import User as user_model

VOCA_SELECTIONS = [
    ('all', 'Whole words'),
    ('K_SAT', 'K_SAT'),
    ('GRE','GRE'),
    ('elementary','elementary'),
    # etc.
]

REVIEWING_INTENSITY = [
    ('1','1'),
    ('2','2'),
    ('3','3'),
    ('4','4'),
    ('5','5')
]

class TimeStampedModel(models.Model):
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

class review_settings(TimeStampedModel):
    # user는 외래키 사용
    user = models.ForeignKey(
        user_model, 
        null=True, 
        on_delete=models.CASCADE, 
        related_name='user_id')

    selected_voca = models.CharField(
        blank=False, 
        choices = VOCA_SELECTIONS, 
        max_length=255)

    voca_per_day = models.CharField(
        blank=False, 
        max_length=255,
        )

    reviewing_intensity =models.CharField(
        blank=False, 
        choices = REVIEWING_INTENSITY, 
        max_length=255)

    purpose = models.CharField(
        blank=True,
        max_length=255)
