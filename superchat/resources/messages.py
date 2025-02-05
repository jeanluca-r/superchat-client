# superchat/resources/messages.py

class MessagesMixin:
    def create_message(self, **data):
        """
        Create (send) a message.
        """
        endpoint = "messages"
        return self._request("POST", endpoint, json=data)
