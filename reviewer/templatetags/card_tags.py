from django import template
from django.contrib.auth.models import User as user_model
from reviewer.models import BOXES, Card, review_settings
from django.shortcuts import get_object_or_404


register = template.Library()

@register.inclusion_tag("../templates/reviewer_box_links.html")
def boxes_as_links():
    boxes = []
    
    for box_num in BOXES:
        card_count = len(Card.objects.filter(box=box_num))
        if box_num == 1:
            box_name = 'Today'
        elif box_num == 2:
            box_name = 'Yesterday'
        elif box_num == 3:
            box_name = '3 days ago'
        elif box_num == 4:
            box_name = '5 days ago'
        elif box_num == 5:
            box_name = '7 days ago'

        boxes.append({
            "number": box_num,
            "card_count": card_count,
            "box_name": box_name,
        })

    return {"boxes": boxes}
