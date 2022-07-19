from django.contrib import admin
from .models import Voca, learn_review_custom




class VocaAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ['voca', 'genre', 'significance', 'difficulty', 'sentences']
    list_editable = ['genre','significance', 'difficulty', 'sentences']
    list_filter = ('genre', 'difficulty', 'significance')
    search_fields = ['voca', 'sentences']
    ordering = ['voca', 'genre']

admin.site.register(Voca,VocaAdmin) #admin에 앱 저장
admin.site.register(learn_review_custom)
