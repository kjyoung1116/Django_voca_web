from audioop import add
from pydoc import plain
from re import M
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.models import User as user_model
from soupsieve import select
from reviewer.forms import CreateReviewSettingsForm
from .models import review_settings, Card
import pandas as pd
from django.views.generic import (ListView, CreateView, UpdateView, DetailView)
from django.urls import reverse_lazy
from .forms import CardCheckForm
from datetime import datetime, timedelta, date
import schedule
# Create your views here.


def index(request):
    user = get_object_or_404(user_model, pk=request.user.id)
    my_reviewers = review_settings.objects.filter(user_id=user)
    today = date.today()
    return render(request, '../templates/reviewer.html', {'my_reviewers': my_reviewers, 'today': today, 'user': user})


def plan_delete(request, plan_name):
    user = get_object_or_404(user_model, pk=request.user.id)
    review_setting = get_object_or_404(
        review_settings, user_id=user.id, plan_name=plan_name)
    review_setting.delete()
    cards = Card.objects.filter(addition0=user, addition9=plan_name)
    cards.delete()
    return redirect('/reviewer')


def reviewer_create(request):

    if request.method == 'GET':
        form = CreateReviewSettingsForm()
        return render(request, '../templates/reviewer_create.html', {'form': form})

    elif request.method == 'POST':
        user = get_object_or_404(user_model, pk=request.user.id)

        plan_name = request.POST['plan_name']
        selected_voca = request.POST['selected_voca']
        voca_per_day = request.POST['voca_per_day']
        reviewing_intensity = request.POST['reviewing_intensity']
        purpose = request.POST['purpose']

        new_setting = review_settings.objects.create(
            user=user,
            plan_name=plan_name,
            selected_voca=selected_voca,
            voca_per_day=voca_per_day,
            reviewing_intensity=reviewing_intensity,
            purpose=purpose
        )
        new_setting.save()

        # 데이터셋마다 변경
        if selected_voca == 'all':
            data_filtered = pd.read_excel('voca.xlsx')
            number = data_filtered['번호']
            voca = data_filtered['단어']
            meaning = data_filtered['의미']
            genre = data_filtered['장르']
            synonyms = data_filtered['유의어']
            pronunciations = data_filtered['발음기호']

        elif selected_voca == 'elementary':
            data_filtered = pd.read_excel('voca.xlsx', sheet_name='elementary')
            number = data_filtered['번호']
            voca = data_filtered['단어']
            meaning = data_filtered['의미']
            genre = data_filtered['장르']
            synonyms = data_filtered['유의어']
            pronunciations = data_filtered['발음기호']

        elif selected_voca == 'K_SAT':
            data = pd.read_excel('voca.xlsx')
            data_filtered = data.loc[data['장르'] == 'K_SAT']
            number = data_filtered['번호']
            voca = data_filtered['단어']
            meaning = data_filtered['의미']
            genre = data_filtered['장르']
            synonyms = data_filtered['유의어']
            pronunciations = data_filtered['발음기호']

        elif selected_voca == 'GRE':
            data = pd.read_excel('voca.xlsx')
            data_filtered = data.loc[data['장르'] == 'GRE']
            number = data_filtered['번호']
            voca = data_filtered['단어']
            meaning = data_filtered['의미']
            genre = data_filtered['장르']
            synonyms = data_filtered['유의어']
            pronunciations = data_filtered['발음기호']

        '''elif selected_voca =='confusing':
            data_filtered = pd.read_excel('voca.xlsx', sheet_name='confusing')
            number = data_filtered['번호']
            voca = data_filtered['단어']
            meaning = data_filtered['의미']
            genre = data_filtered['장르']
            synonyms = data_filtered['유의어']
            pronunciations = data_filtered['발음기호']'''  # 수정 필요, 혼동어휘끼리 묶어서 나오도록 템플릿 변경해야함.

        for i, j, k, l, m, n in zip(voca, meaning, number, genre, synonyms, pronunciations):
            new_card = Card.objects.create(
                question=i,
                answer=j,
                addition0=user,
                addition1=k,
                addition2=l,
                addition3=m,
                addition4=n,
                addition9=plan_name
            )

        return redirect('reviewer:index')
        '''return render(request, 'reviewer:index')'''


def my_reviewers(request):

    return render(request, '../templates/reviewer_current.html')


class reviewer_plan_detail(ListView):

    model = Card
    template_name = 'reviewer_plan_detail.html'

    def get_context_data(self, **kwargs):
        user = self.request.user
        context = super(reviewer_plan_detail, self).get_context_data(**kwargs)
        context['card'] = Card.objects.filter(addition0=user)
        context['plan_name'] = self.kwargs['plan_name']
        context['user'] = user
        dates = set(Card.objects.filter(
            addition0=user, addition9=self.kwargs['plan_name']).values_list('review_date', flat=True))
        context["review_date"] = sorted(dates)
        return context


class new_card(CreateView):
    model = Card
    fields = ["question", "answer", "box", "addition1", "addition2", "addition3", "addition4",
              "addition5", "addition6", "addition7", "addition8", "addition9", "addition0"]
    success_url = reverse_lazy("reviewer:new_card")
    template_name = 'reviewer_new_card.html'


class update_card(new_card, UpdateView):
    success_url = reverse_lazy("reviewer:reviewer_detail")
    template_name = 'reviewer_update_card.html'


global daily_review_num
daily_review_num = 0


def daily_review_num_update():
    global daily_review_num
    daily_review_num = 0


schedule.every().day.at("00:00").do(daily_review_num_update)


class box_view(reviewer_plan_detail):
    template_name = "reviewer_box.html"
    form_class = CardCheckForm

    def get_queryset(self):
        user = self.request.user
        return Card.objects.filter(review_date=self.kwargs['review_date'], addition0=user, addition9=self.kwargs['plan_name'])[0:1]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        for i in set(Card.objects.filter(addition0=user).values_list('review_date', flat=True)):
            context["box_count"] = len(Card.objects.filter(
                review_date=self.kwargs['review_date'], addition0=user, addition9=self.kwargs['plan_name']))

        context["box_name"] = self.kwargs['review_date']

        if self.object_list:
            context["check_card"] = self.object_list

        dates = set(Card.objects.filter(
            addition0=user, addition9=self.kwargs['plan_name']).values_list('review_date', flat=True))
        context["review_date"] = sorted(dates)
        context["user"] = user
        context["plan_name"] = self.kwargs['plan_name']
        context["date"] = self.kwargs['review_date']
        context["voca_per_day"] = review_settings.objects.get(
            user_id=user.id, plan_name=self.kwargs['plan_name']).voca_per_day
        global daily_review_num
        context['daily_review_num'] = daily_review_num
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        global daily_review_num
        if form.is_valid():
            user = self.request.user
            card_id = get_object_or_404(Card, id=form.cleaned_data["card_id"])
            knowing_level = form.cleaned_data["knowing_level"]
            card = Card.objects.get(
                question=card_id, addition0=self.request.user, addition9=self.kwargs['plan_name'])

            if review_settings.objects.get(user_id=user.id, plan_name=self.kwargs['plan_name']).reviewing_intensity == '1':
                if knowing_level < 3:
                    card.review_date = date.today()
                else:
                    card.review_date = date.today() + \
                        timedelta(days=knowing_level)
                    daily_review_num += 1
            elif review_settings.objects.get(user_id=user.id, plan_name=self.kwargs['plan_name']).reviewing_intensity == '2':
                if knowing_level == 1:
                    card.review_date = date.today()
                elif knowing_level == 2:
                    card.review_date = date.today() + timedelta(days=1)
                    daily_review_num += 1
                elif knowing_level == 3:
                    card.review_date = date.today() + timedelta(days=5)
                    daily_review_num += 1

            elif review_settings.objects.get(user_id=user.id, plan_name=self.kwargs['plan_name']).reviewing_intensity == '3':
                if knowing_level == 1:
                    card.review_date = date.today() + timedelta(days=1)
                    daily_review_num += 1
                elif knowing_level == 2:
                    card.review_date = date.today() + timedelta(days=4)
                    daily_review_num += 1
                elif knowing_level == 3:
                    card.review_date = date.today() + timedelta(days=7)
                    daily_review_num += 1
            card.save()

        return redirect(request.META.get("HTTP_REFERER"))
