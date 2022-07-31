from hashlib import new
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

###############################################################

NUM_BOXES = 5
BOXES = range(1, NUM_BOXES + 1)

class Card(models.Model):
    question = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)
    #추가 사항들 ex) 예문, 발음기호 등
    addition1 =models.CharField(max_length=100, blank=True, default='')
    addition2 =models.CharField(max_length=100, blank=True, default='')
    addition3 =models.CharField(max_length=100, blank=True, default='')
    addition4 =models.CharField(max_length=100, blank=True, default='')
    addition5 =models.CharField(max_length=100, blank=True, default='')
    addition6 =models.CharField(max_length=100, blank=True, default='')
    addition7 =models.CharField(max_length=100, blank=True, default='')
    addition8 =models.CharField(max_length=100, blank=True, default='')
    addition9 =models.CharField(max_length=100, blank=True, default='')
    addition0 =models.CharField(max_length=100, blank=True, default='')
    box = models.IntegerField(
        choices=zip(BOXES, BOXES),
        default=BOXES[0],
    )
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question


    def move(self, knowing_level):
        new_box = int(self.box) + int(knowing_level)

        if new_box in BOXES:
            self.box = new_box
            self.save()

        return self
        
