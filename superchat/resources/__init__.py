# superchat/resources/__init__.py

from .channels import ChannelsMixin
from .contacts import ContactsMixin
from .conversations import ConversationsMixin
from .files import FilesMixin
from .inboxes import InboxesMixin
from .labels import LabelsMixin
from .messages import MessagesMixin
from .notes import NotesMixin
from .templates import TemplatesMixin
from .users import UsersMixin

__all__ = [
    "ChannelsMixin",
    "ContactsMixin",
    "ConversationsMixin",
    "FilesMixin",
    "InboxesMixin",
    "LabelsMixin",
    "MessagesMixin",
    "NotesMixin",
    "TemplatesMixin",
    "UsersMixin",
]
