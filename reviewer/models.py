from hashlib import new
from django.db import models
from platformdirs import user_cache_dir
from django.contrib.auth.models import User as user_model
from datetime import datetime
from django.utils.dateformat import DateFormat

VOCA_SELECTIONS = [

    ('elementary', '기초 영단어'),
    ('K_SAT', '수능 영단어'),
    ('GRE', '편입/GRE 영단어'),
    ('all', '모든 영단어'),
    ('confusing', '혼동하기 쉬운 영단어'),
    # etc.
]

REVIEWING_INTENSITY = [
    ('1', '짧게'),
    ('2', '기본'),
    ('3', '길게'),
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

    plan_name = models.CharField(
        blank=False,
        max_length=255)

    selected_voca = models.CharField(
        blank=False,
        choices=VOCA_SELECTIONS,
        max_length=255)

    voca_per_day = models.CharField(
        blank=False,
        max_length=255,
    )

    reviewing_intensity = models.CharField(
        blank=False,
        choices=REVIEWING_INTENSITY,
        max_length=255)

    purpose = models.CharField(
        blank=True,
        max_length=255)

###############################################################


NUM_BOXES = 5
BOXES = range(1, NUM_BOXES + 1)


class Card(models.Model):
    question = models.CharField(max_length=1000)
    answer = models.CharField(max_length=1000, blank=True)
    #추가 사항들 ex) 예문, 발음기호 등
    addition1 = models.CharField(
        max_length=1000, blank=True, default='')    # 단어 번호
    addition2 = models.CharField(
        max_length=1000, blank=True, default='')    # 장르
    addition3 = models.CharField(
        max_length=1000, blank=True, default='')    # 유의어
    addition4 = models.CharField(
        max_length=1000, blank=True, default='')    # 발음기호
    addition5 = models.CharField(max_length=1000, blank=True, default='')
    addition6 = models.CharField(max_length=1000, blank=True, default='')
    addition7 = models.CharField(max_length=1000, blank=True, default='')
    addition8 = models.CharField(max_length=1000, blank=True, default='')
    addition9 = models.CharField(
        max_length=1000, blank=True, default='')    # 생성 플랜명
    addition0 = models.CharField(
        max_length=1000, blank=True, default='')    # 생성자 아이디
    date_created = models.DateTimeField(auto_now_add=True)
    review_date = models.DateField(auto_now_add=True)  # 복습일, 기본: 생성일

    def __str__(self):
        return self.question
