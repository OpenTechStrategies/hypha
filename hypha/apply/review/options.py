from django.utils.translation import gettext as _
from django.conf import settings
NA = 99

RATE_CHOICES = (
    (0, _('0. Need more info')),
    (1, _('1. Poor')),
    (2, _('2. Not so good')),
    (3, _('3. Is o.k.')),
    (4, _('4. Good')),
    (5, _('5. Excellent')),
    (6, _('6')),
    (7, _('7')),
    (8, _('8')),
    (9, _('9')),
    (10, _('10')),
    (NA, _('n/a - choose not to answer')),
)

RATE_CHOICES_DICT = dict(RATE_CHOICES)
RATE_CHOICE_NA = RATE_CHOICES_DICT[NA]

NO = 0
MAYBE = 1
YES = 2
recommendations = getattr(settings, "RECOMMENDATION_CHOICES", {})

RECOMMENDATION_CHOICES = (
    (0, _('Need More Info')),
    (1, _('Reject')),
    (2, _('Weak Reject')),
    (3, _('Weak Accept')),
    (4, _('Accept')),
    (5, _('Strong Accept')),
    (6, _('N/A - Choose not to answer')),
) + recommendations.get('CHOICES',((),))

YES_RECOMMENDATIONS = [3,4,5] + recommendations.get('YES',[])
NO_RECOMMENDATIONS = [1,2] + recommendations.get('NO',[])
MAYBE_RECOMMENDATIONS = [0,6] + recommendations.get('MAYBE',[])

def map_recommendation (raw_recommendation):
    if(raw_recommendation in NO_RECOMMENDATIONS):
        return NO
    if(raw_recommendation in YES_RECOMMENDATIONS):
        return YES
    if(raw_recommendation in MAYBE_RECOMMENDATIONS):
        return MAYBE

DISAGREE = 0
AGREE = 1

OPINION_CHOICES = (
    (AGREE, _('Agree')),
    (DISAGREE, _('Disagree')),
)

PRIVATE = 'private'
REVIEWER = 'reviewers'

VISIBILILTY_HELP_TEXT = {
    REVIEWER: _('Visible to other reviewers and staff.'),
    PRIVATE: _('Visible only to staff.'),
}

VISIBILITY = {
    REVIEWER: _('Reviewers and Staff'),
    PRIVATE: _('Private'),
}
