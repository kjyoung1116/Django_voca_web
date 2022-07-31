from msilib import CreateRecord
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.models import User as user_model
from soupsieve import select
from reviewer.forms import CreateReviewSettingsForm
from .models import review_settings, Card
import pandas as pd
from django.views.generic import (ListView,CreateView,UpdateView,)
from django.urls import reverse_lazy
from .forms import CardCheckForm

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

    return render(request, '../templates/my_reviewers.html', {'my_reviewers': my_reviewers})



class reviewer_detail(ListView):
    model = Card
    queryset = Card.objects.all().order_by("box", "-date_created")
    template_name = 'reviewer_detail.html'

class new_card(CreateView):
    model = Card
    fields = ["question", "answer", "box", "addition1", "addition2", "addition3", "addition4", "addition5", "addition6", "addition7", "addition8", "addition9", "addition0"]
    success_url = reverse_lazy("reviewer:new_card")
    template_name = 'reviewer_new_card.html'

class update_card(new_card, UpdateView):
    success_url = reverse_lazy("reviewer:reviewer_detail")
    template_name = 'reviewer_update_card.html'


class box_view(reviewer_detail):
    template_name = "reviewer_box.html"
    form_class = CardCheckForm
    def get_queryset(self):
        return Card.objects.filter(box=self.kwargs["box_num"])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["box_number"] = self.kwargs["box_num"]
        if self.object_list:
            context["check_card"] = self.object_list
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            card = get_object_or_404(Card, id=form.cleaned_data["card_id"])
            card.move(form.cleaned_data["knowing_level"])

        return redirect(request.META.get("HTTP_REFERER"))
