from django import forms
from .models import review_settings
from django.forms import ModelForm, TextInput, EmailInput, NumberInput

class CreateReviewSettingsForm(forms.ModelForm):
    class Meta:
        model = review_settings

        fields = [
            'selected_voca',
            'voca_per_day',
            'reviewing_intensity',
            'purpose',

        ]

        labels = {
            "selected_voca":"단어 선택",
            'voca_per_day': '하루에 학습할 단어 개수',
            'reviewing_intensity':'복습 강도',
            'purpose':'학습 목적'
        }



class CardCheckForm(forms.Form):
    card_id = forms.IntegerField(required=True)
    knowing_level = forms.IntegerField(required=True)

