# superchat/resources/notes.py

class NotesMixin:
    def create_note_in_conversation(self, conversation_id, **data):
        """
        Create a note in a conversation.
        """
        endpoint = f"conversations/{conversation_id}/notes"
        return self._request("POST", endpoint, json=data)

    def list_notes_in_conversation(self, conversation_id, **params):
        """
        List notes in a conversation.
        """
        endpoint = f"conversations/{conversation_id}/notes"
        return self._request("GET", endpoint, params=params)

    def get_note_in_conversation(self, conversation_id, note_id, **params):
        """
        Retrieve a specific note in a conversation.
        """
        endpoint = f"conversations/{conversation_id}/notes/{note_id}"
        return self._request("GET", endpoint, params=params)

    def update_note_in_conversation(self, conversation_id, note_id, **data):
        """
        Update a note in a conversation.
        """
        endpoint = f"conversations/{conversation_id}/notes/{note_id}"
        return self._request("PUT", endpoint, json=data)

    def delete_note_in_conversation(self, conversation_id, note_id, **params):
        """
        Delete a note from a conversation.
        """
        endpoint = f"conversations/{conversation_id}/notes/{note_id}"
        return self._request("DELETE", endpoint, params=params)
