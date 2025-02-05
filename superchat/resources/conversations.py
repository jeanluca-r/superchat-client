# superchat/resources/conversations.py

class ConversationsMixin:
    def create_conversation(self, **data):
        """
        Create a new conversation.
        """
        endpoint = "conversations"
        return self._request("POST", endpoint, json=data)

    def list_conversations(self, **params):
        """
        List conversations.
        """
        endpoint = "conversations"
        return self._request("GET", endpoint, params=params)

    def get_conversation(self, conversation_id, **params):
        """
        Get a specific conversation by its ID.
        """
        endpoint = f"conversations/{conversation_id}"
        return self._request("GET", endpoint, params=params)

    def patch_conversation(self, conversation_id, **data):
        """
        Update (patch) an existing conversation.
        """
        endpoint = f"conversations/{conversation_id}"
        return self._request("PATCH", endpoint, json=data)

    def delete_conversation(self, conversation_id, **params):
        """
        Delete a conversation.
        """
        endpoint = f"conversations/{conversation_id}"
        return self._request("DELETE", endpoint, params=params)

    def create_conversation_export(self, **data):
        """
        Create an export for a conversation.
        """
        endpoint = "conversation-exports"
        return self._request("POST", endpoint, json=data)

    def get_conversation_export(self, export_id, **params):
        """
        Retrieve a conversation export by its ID.
        """
        endpoint = f"conversation-exports/{export_id}"
        return self._request("GET", endpoint, params=params)
