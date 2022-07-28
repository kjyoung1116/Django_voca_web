from msilib import CreateRecord
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.models import User as user_model
from soupsieve import select
from reviewer.forms import CreateReviewSettingsForm
from .models import REVIEWING_INTENSITY, review_settings
import pandas as pd

# Create your views here.
def index(request):
    return render(request, '../templates/reviewer.html')

def reviewer_create(request):
    if request.method == 'GET':
        form = CreateReviewSettingsForm()
        return render(request, '../templates/reviewer_create.html', {'form': form})

    elif request.method == 'POST':
        user = get_object_or_404(user_model, pk=request.user.id)

        selected_voca = request.POST['selected_voca']
        voca_per_day = request.POST['voca_per_day']
        reviewing_intensity = request.POST['reviewing_intensity']
        purpose = request.POST['purpose']

        new_setting = review_settings.objects.create(
            user = user,
            selected_voca = selected_voca,
            voca_per_day = voca_per_day,
            reviewing_intensity = reviewing_intensity,
            purpose = purpose
        )

        new_setting.save()

        return render(request, '../templates/reviewer.html')


def my_reviewers(request):
    user = get_object_or_404(user_model, pk=request.user.id)
    my_reviewers = review_settings.objects.filter(user_id = user)
    if my_reviewers.selected_voca == all:
        data = pd.read_excel('voca.xlsx')
        
        voca = data['단어']
        meaning = data['의미']
        sentence = data['예문']
        significance = data['중요도']
        difficulty = data['난이도']
        number = data['번호']
        synonym = data['유의어']

    voca_data = []

    for i in zip(voca,meaning,sentence, significance, difficulty, number,synonym):
        voca_data.append(i)





    return render(request, '../templates/my_reviewers.html', {'my_reviewers': my_reviewers})

