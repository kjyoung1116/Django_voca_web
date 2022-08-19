from django.db import models
# Create your models here.

'''class Genre(models.Model):
    genre = models.CharField(max_length=200, help_text='Enter a genre (e.g. GRE, Elementary, ...)', null = True)

    def __str__(self):
        return self.genre'''


class Voca(models.Model):
    voca = models.CharField(max_length=100)
    meaning = models.CharField(max_length=100)
    sentences = models.CharField(max_length=100)
    significance = models.CharField(max_length=50)
    difficulty = models.CharField(max_length=50)
    genre = models.CharField(max_length=10, default='GRE')

    def __str__(self):
        return self.voca


class learn_review_custom(models.Model):
    voca_per_day_choices = [
        (10, 10),
        (20, 20),
        (30, 30),
        (50, 50),
        (70, 70),
        (80, 80),
        (90, 90),
        (100, 100),
        (130, 130),
        (150, 150),
        (200, 200),
        (250, 250),
        (300, 300),
    ]

    review_day_choices = [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        (6, 6),
        (7, 7),
        (8, 8),
        (9, 9),
        (10, 10),
        (11, 11),
        (12, 12),
        (13, 13),
        (14, 14),
    ]

    genre_choices = review_day_choices = [
        ('elementary', '기초 영단어'),
        ('K_SAT', '수능 영단어'),
        ('GRE', '편입, 토플, GRE 영단어'),
        ('hard', '고급 영단어'),
        ('confusing', '혼동하기 쉬운 영단어'),
        ('idiom', '숙어'),
        ('all', '모든 영단어'),
    ]

    name = models.CharField(max_length=10, help_text='커스텀 플랜의 이름을 입력하세요.')
    voca_per_day = models.CharField(
        max_length=10, choices=voca_per_day_choices, help_text='하루 동안 외울 단어의 수를 입력하세요.')
    review_day = models.CharField(
        max_length=10,  choices=review_day_choices, help_text='외운 단어의 복습이 시작될 주기를 입력하세요. ex) 1,3,7 등')
    select_genre = models.CharField(max_length=10, choices=genre_choices,
                                    help_text='외울 단어의 카테고리를 설정하세요. ex) 모든 단어, 수능 단어, 고급 단어, 기초 단어 등')
    started_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
