import random
import factory

from hypha.apply.funds.tests.factories import (
    ApplicationSubmissionFactory,
    AssignedReviewersFactory,
)
from hypha.apply.stream_forms.testing.factories import FormDataFactory

from ...models import Review, ReviewForm, ReviewOpinion
from ...options import AGREE, DISAGREE, PRIVATE, REVIEWER,NO_RECOMMENDATIONS, YES_RECOMMENDATIONS, MAYBE_RECOMMENDATIONS
from . import blocks

__all__ = ['ReviewFactory', 'ReviewFormFactory', 'ReviewOpinionFactory']


class ReviewFormDataFactory(FormDataFactory):
    field_factory = blocks.ReviewFormFieldsFactory


class ReviewFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Review

    class Params:
        recommendation_yes = factory.Trait(recommendation=random.choice(YES_RECOMMENDATIONS))
        recommendation_maybe = factory.Trait(recommendation=random.choice(MAYBE_RECOMMENDATIONS))
        draft = factory.Trait(is_draft=True)
        visibility_private = factory.Trait(visibility=PRIVATE)
        visibility_reviewer = factory.Trait(visibility=REVIEWER)

    submission = factory.SubFactory(ApplicationSubmissionFactory)
    revision = factory.SelfAttribute('submission.live_revision')
    author = factory.SubFactory(AssignedReviewersFactory, submission=factory.SelfAttribute('..submission'))
    form_fields = factory.LazyAttribute(lambda o: o.submission.round.review_forms.first().fields)
    form_data = factory.SubFactory(
        ReviewFormDataFactory,
        form_fields=factory.SelfAttribute('..form_fields'),
    )
    is_draft = False
    recommendation = random.choice(NO_RECOMMENDATIONS)
    score = 0


class ReviewOpinionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ReviewOpinion

    class Params:
        opinion_agree = factory.Trait(opinion=AGREE)
        opinion_disagree = factory.Trait(opinion=DISAGREE)

    review = factory.SubFactory(ReviewFactory)
    author = factory.SubFactory(AssignedReviewersFactory, staff=True, submission=factory.SelfAttribute('..review.submission'))
    opinion = DISAGREE


class ReviewFormFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ReviewForm

    name = factory.Faker('word')
    form_fields = blocks.ReviewFormFieldsFactory
