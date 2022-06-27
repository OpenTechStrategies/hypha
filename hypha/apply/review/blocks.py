import json

from django import forms
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _
from wagtail.core.blocks import (
    IntegerBlock,
    RichTextBlock,
)

from hypha.apply.review.fields import ScoredAnswerField
from hypha.apply.review.options import (
    NA,
    REVIEWER,
    RATE_CHOICE_NA,
    RATE_CHOICES,
    RATE_CHOICES_DICT,
    RECOMMENDATION_CHOICES,
    VISIBILILTY_HELP_TEXT,
    VISIBILITY,
)
from hypha.apply.stream_forms.blocks import (
    CharFieldBlock,
    CheckboxFieldBlock,
    DropdownFieldBlock,
    OptionalFormFieldBlock,
    TextFieldBlock,
)
from hypha.apply.utils.blocks import CustomFormFieldsBlock, MustIncludeFieldBlock
from hypha.apply.utils.options import RICH_TEXT_WIDGET_SHORT


class ScoreFieldBlock(OptionalFormFieldBlock):
    field_class = ScoredAnswerField

    class Meta:
        label = _('Score')
        icon = 'order'
        template = 'review/render_scored_answer_field.html'

    def get_field_kwargs(self, struct_value):
        kwargs = super().get_field_kwargs(struct_value)
        kwargs['initial'] = ['', NA]
        return kwargs

    def render(self, value, context=None):
        try:
            comment, score = context['data']
        except ValueError:
            # TODO: Remove json load as data moved away from JSON
            comment, score = json.loads(context['data'])
        context.update(**{
            'comment': comment,
            'score': RATE_CHOICES_DICT.get(int(score), RATE_CHOICE_NA)
        })

        return super().render(value, context)


class ScoreFieldWithoutTextBlock(OptionalFormFieldBlock):
    """
    There are two ways score could be accepted on reviews.

    One is to use ScoreFieldBlock, where you need to put text answer along with
    giving score on the review.

    Second is to use this block to just select a reasonable score with adding
    any text as answer.

    This block modifies RATE_CHOICES to have empty string('') in place of NA
    for text value `n/a - choose not to answer` as it helps to render this value
    as default to the forms and also when this field is
    required it automatically handles validation on empty string.
    """
    name = 'score without text'

    min = IntegerBlock(min_value=0, max_value=9,  default=0, required=False)
    max = IntegerBlock(min_value=1, max_value=10, default=10, required=False)

    field_class = forms.ChoiceField

    class Meta:
        icon = 'order'

    def get_field_kwargs(self, struct_value):
        kwargs = super().get_field_kwargs(struct_value)
        kwargs['choices'] = self.get_choices(RATE_CHOICES)
        if struct_value.get('min') is None:
            struct_value['min'] = 0
        if struct_value.get('max') is None:
            struct_value['max'] = 10
        if struct_value['min'] > struct_value['max']:
            struct_value['min'] = struct_value['max']
        kwargs['choices'] = kwargs['choices'][
            int(struct_value['min']) + 1 : int(struct_value['max']) + 2
        ]
        return kwargs

    def render(self, value, context=None):
        data = context['data']
        if context['data'] != '':
            data = int(context['data'])
        choices = dict(self.get_choices(RATE_CHOICES))
        context['data'] = choices[data]

        return super().render(value, context)

    def get_choices(self, choices):
        """
        Replace 'NA' option with an empty string choice.
        """
        rate_choices = list(choices)
        rate_choices.pop(-1)
        rate_choices = [('', 'n/a - choose not to answer')] + rate_choices
        return tuple(rate_choices)


class ReviewMustIncludeFieldBlock(MustIncludeFieldBlock):
    pass


class RecommendationBlock(ReviewMustIncludeFieldBlock):
    name = 'recommendation'
    description = 'Overall recommendation'
    field_class = forms.ChoiceField

    class Meta:
        icon = 'pick'

    def get_field_kwargs(self, struct_value):
        kwargs = super().get_field_kwargs(struct_value)
        kwargs['choices'] = RECOMMENDATION_CHOICES
        return kwargs

    def render(self, value, context=None):
        data = int(context['data'])
        choices = dict(RECOMMENDATION_CHOICES)
        context['data'] = choices[data]

        return super().render(value, context)


class RecommendationCommentsBlock(ReviewMustIncludeFieldBlock):
    name = 'comments'
    description = 'Recommendation comments'
    widget = RICH_TEXT_WIDGET_SHORT

    class Meta:
        icon = 'openquote'
        template = 'stream_forms/render_unsafe_field.html'

    def get_field_kwargs(self, struct_value):
        kwargs = super().get_field_kwargs(struct_value)
        kwargs['required'] = False
        return kwargs


class VisibilityBlock(ReviewMustIncludeFieldBlock):
    name = 'visibility'
    description = 'Visibility'
    field_class = forms.ChoiceField
    widget = forms.RadioSelect()

    class Meta:
        icon = 'radio-empty'

    def get_field_kwargs(self, struct_value):
        kwargs = super(VisibilityBlock, self).get_field_kwargs(struct_value)
        kwargs['choices'] = VISIBILITY.items()
        kwargs['initial'] = REVIEWER
        kwargs['help_text'] = mark_safe('<br>'.join(
            [VISIBILITY[choice] + ': ' + VISIBILILTY_HELP_TEXT[choice] for choice in VISIBILITY]
        ))
        return kwargs


class ReviewCustomFormFieldsBlock(CustomFormFieldsBlock):
    char = CharFieldBlock(group=_('Fields'))
    text = TextFieldBlock(group=_('Fields'))
    text_markup = RichTextBlock(group=_('Fields'), label=_('Paragraph'))
    score = ScoreFieldBlock(group=_('Fields'))
    score_without_text = ScoreFieldWithoutTextBlock(group=_('Fields'))
    checkbox = CheckboxFieldBlock(group=_('Fields'))
    dropdown = DropdownFieldBlock(group=_('Fields'))

    required_blocks = ReviewMustIncludeFieldBlock.__subclasses__()
