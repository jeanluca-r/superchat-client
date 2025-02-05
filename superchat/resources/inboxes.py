# superchat/resources/inboxes.py

class InboxesMixin:
    def list_inboxes(self, **params):
        """
        List inboxes.
        """
        endpoint = "inboxes"
        return self._request("GET", endpoint, params=params)

    def get_inbox(self, inbox_id, **params):
        """
        Retrieve a specific inbox.
        """
        endpoint = f"inboxes/{inbox_id}"
        return self._request("GET", endpoint, params=params)
