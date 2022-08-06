from django import template
from django.utils.safestring import mark_safe

from ..models import MAYBE, NO, YES

register = template.Library()


TRAFFIC_LIGHT_COLORS = {
    YES: {
        'color': 'green',
        'value': 'Y',
    },
    MAYBE: {
        'color': 'amber',
        'value': 'M',
    },
    NO: {
        'color': 'red',
        'value': 'N'
    }
}

TRAFFIC_LIGHT_TEMPLATE = '<span class="traffic-light traffic-light--{color}"></span>'


@register.filter()
def traffic_light(value):
    try:
        return mark_safe(TRAFFIC_LIGHT_TEMPLATE.format(**TRAFFIC_LIGHT_COLORS[value]))
    except KeyError:
        return ''


@register.filter
def can_review(user, submission):
    return submission.can_review(user)


@register.filter
def has_draft(user, submission):
    return submission.can_review(user) and submission.assigned.draft_reviewed().filter(reviewer=user).exists()

@register.filter_function
def order_by(reviewers):
    reviewers.sort(key=lambda reviewer: reviewer.review.recommendation if not reviewer.has_review else -1,reverse=True)
    return reviewers

@register.filter
def average_review_score(reviewers):
    if reviewers:
        scores = [
            reviewer.review.score
            for reviewer in reviewers
            if not reviewer.has_review and not reviewer.review.is_draft
        ]
        if len(scores) > 0:
            return sum(scores) / len(scores)
        else:
            return None
    else:
        return reviewers
