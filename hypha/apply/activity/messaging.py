import logging
import re

import requests
from django.conf import settings
from django.contrib.auth import get_user_model

from .adapters import ActivityAdapter, DjangoMessagesAdapter, EmailAdapter, SlackAdapter

logger = logging.getLogger(__name__)
User = get_user_model()

from .options import MESSAGES  # noqa


class MessengerBackend:
    def __init__(self, *adapters):
        self.adapters = adapters

    def __call__(self, *args, related=None, **kwargs):
        return self.send(*args, related=related, **kwargs)

    def send(
        self,
        message_type,
        request,
        user,
        related,
        source=None,
        sources=list(),
        **kwargs
    ):
        from .models import Event

        if source:
            event = Event.objects.create(type=message_type.name, by=user, source=source)
            for adapter in self.adapters:
                adapter.process(
                    message_type,
                    event,
                    request=request,
                    user=user,
                    source=source,
                    related=related,
                    **kwargs
                )

        elif sources:
            events = Event.objects.bulk_create(
                Event(type=message_type.name, by=user, source=source)
                for source in sources
            )
            for adapter in self.adapters:
                adapter.process_batch(
                    message_type,
                    events,
                    request=request,
                    user=user,
                    sources=sources,
                    related=related,
                    **kwargs
                )

class ZulipAdapter(SlackAdapter):
    adapter_type = "Zulip"

    def __init__(self):
        super().__init__()
        self.destination = settings.ZULIP_DESTINATION_URL
        self.target_room = settings.ZULIP_DESTINATION_STREAM
        self.topic = settings.ZULIP_DESTINATION_TOPIC
        self.user = settings.ZULIP_BOT_EMAIL
        self.api_key = settings.ZULIP_API_KEY

    def zulip_links(self, links, sources):
        return ', '.join(
            f'[{source.title}]({links[source.id]})'
            for source in sources
        )

    def rewrite_slack_links(self, message):
        return re.sub("<([^\\|]+)\\|([^>]+)>", r"[\2](\1)", message)

    def slack_links(self, links, sources):
        return self.zulip_links(links, sources)

    def zulip_id(self, user):
        if user is None:
            return ''

        if not user.slack:
            return ''

        return f'@**{user.slack}**'

    def slack_id(self, user):
        return self.zulip_id(user)

    def zulip_streams(self, source, **kwargs):
        target_streams = self.slack_channels(source, **kwargs)

        # Make sure each stream name doesn't start with a "#".
        target_streams = [
            stream.replace('#','')
            for stream in target_streams
            if stream
        ]

        return target_streams

    def send_message(self, message, recipient, source, **kwargs):
        target_streams = self.zulip_streams(source, **kwargs)

        if not self.destination or not any(target_streams):
            errors = list()
            if not self.destination:
                errors.append('Destination URL')
            if not target_streams:
                errors.append('Stream ID')
            if not self.user:
                errors.append('Bot email')
            if not self.api_key:
                errors.append('API key')
            return 'Missing configuration: {}'.format(', '.join(errors))

        message = ' '.join([recipient, self.rewrite_slack_links(message)]).strip()

        data = {
            "type": "stream",
            "to": target_streams,
            "topic": self.topic,
            "content": message,
        }
        auth = (
            self.user,
            self.api_key
        )
        response = requests.post(self.destination, data=data, auth=auth)

        return str(response.status_code) + ': ' + response.content.decode()

adapters = [
    ActivityAdapter(),
    SlackAdapter(),
    ZulipAdapter(),
    EmailAdapter(),
    DjangoMessagesAdapter(),
]

messenger = MessengerBackend(*adapters)
