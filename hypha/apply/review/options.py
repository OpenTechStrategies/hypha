from django.utils.translation import gettext as _

NA = 99

RATE_CHOICES = (
    (0, _('0. Need more info')),
    (1, _('1. Poor')),
    (2, _('2. Not so good')),
    (3, _('3. Is o.k.')),
    (4, _('4. Good')),
    (5, _('5. Excellent')),
    (NA, _('n/a - choose not to answer')),
)

RATE_CHOICES_DICT = dict(RATE_CHOICES)
RATE_CHOICE_NA = RATE_CHOICES_DICT[NA]

NO = 0
MAYBE = 1
YES = 2

RECOMMENDATION_CHOICES = (
    (0, _('Need More Info')),
    (1, _('Reject')),
    (2, _('Weak Reject')),
    (3, _('Weak Accept')),
    (4, _('Accept')),
    (5, _('Strong Accept')),
    (6, _('N/A - Choose not to answer')),
)

NO_RECOMMENDATIONS = [1,2]
YES_RECOMMENDATIONS = [3,4,5]
MAYBE_RECOMMENDATIONS = [0,6]

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
