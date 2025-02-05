# superchat/client.py

import requests
import time
from urllib.parse import urljoin

from .exceptions import SuperchatAPIError, RateLimitError
from .resources.channels import ChannelsMixin
from .resources.contacts import ContactsMixin
from .resources.conversations import ConversationsMixin
from .resources.files import FilesMixin
from .resources.inboxes import InboxesMixin
from .resources.labels import LabelsMixin
from .resources.messages import MessagesMixin
from .resources.notes import NotesMixin
from .resources.templates import TemplatesMixin
from .resources.users import UsersMixin


class SuperchatClient(
    ChannelsMixin,
    ContactsMixin,
    ConversationsMixin,
    FilesMixin,
    InboxesMixin,
    LabelsMixin,
    MessagesMixin,
    NotesMixin,
    TemplatesMixin,
    UsersMixin,
):
    def __init__(self, api_key: str, base_url: str = "https://api.superchat.com/v1.0/", api_version: str = "v1"):
        """
        Initialize the Superchat client.
        
        Args:
            api_key (str): Your API key.
            base_url (str): Base URL for the API.
            api_version (str): API version.
        """
        self.api_key = api_key
        self.base_url = base_url if base_url.endswith("/") else base_url + "/"
        self.api_version = api_version

        self.session = requests.Session()
        self.session.headers.update({
            "X-API-KEY": self.api_key,
            "Content-Type": "application/json",
            "Accept": "application/json",
        })

    def _handle_response(self, response: requests.Response):
        """
        Check the response for errors and return parsed JSON if successful.
        """
        if response.status_code == 429:
            raise RateLimitError(response.status_code, "Rate limit exceeded. Please try again later.")

        if not response.ok:
            try:
                error_info = response.json()
                error_message = error_info.get("error", response.text)
            except Exception:
                error_message = response.text
            raise SuperchatAPIError(response.status_code, error_message)

        try:
            return response.json()
        except ValueError:
            return response.text

    def _request(self, method, endpoint, params=None, data=None, json=None, max_retries=3, **kwargs):
        """
        Helper to perform HTTP requests with a basic retry strategy for rate limiting.
        """
        url = urljoin(self.base_url, endpoint)
        retries = 0

        while True:
            response = self.session.request(method, url, params=params, data=data, json=json, **kwargs)
            if response.status_code == 429:
                retry_after = int(response.headers.get("Retry-After", "1"))
                retries += 1
                if retries > max_retries:
                    return self._handle_response(response)
                print(f"Rate limited. Retrying after {retry_after} second(s)...")
                time.sleep(retry_after)
                continue
            return self._handle_response(response)
