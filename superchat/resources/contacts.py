# superchat/resources/contacts.py

class ContactsMixin:
    def create_contact(self, **data):
        """
        Create a new contact.
        """
        endpoint = "contacts"
        return self._request("POST", endpoint, json=data)

    def list_contacts(self, **params):
        """
        List contacts.
        """
        endpoint = "contacts"
        return self._request("GET", endpoint, params=params)

    def get_contact(self, contact_id, **params):
        """
        Retrieve a single contact by ID.
        """
        endpoint = f"contacts/{contact_id}"
        return self._request("GET", endpoint, params=params)

    def update_contact(self, contact_id, **data):
        """
        Update an existing contact.
        """
        endpoint = f"contacts/{contact_id}"
        return self._request("PUT", endpoint, json=data)

    def delete_contact(self, contact_id, **params):
        """
        Delete a contact.
        """
        endpoint = f"contacts/{contact_id}"
        return self._request("DELETE", endpoint, params=params)

    def search_contact(self, **params):
        """
        Search for contacts.
        """
        endpoint = "contacts/search"
        return self._request("GET", endpoint, params=params)

    def get_contact_lists_from_contact(self, contact_id, **params):
        """
        Retrieve contact lists associated with a contact.
        """
        endpoint = f"contacts/{contact_id}/lists"
        return self._request("GET", endpoint, params=params)

    def create_contact_list_for_contact(self, contact_id, **data):
        """
        Create a contact list for a given contact.
        """
        endpoint = f"contacts/{contact_id}/lists"
        return self._request("POST", endpoint, json=data)

    def delete_contact_from_list(self, contact_id, list_id, **params):
        """
        Delete a contact from a specific list.
        """
        endpoint = f"contacts/{contact_id}/lists/{list_id}"
        return self._request("DELETE", endpoint, params=params)

    def get_contact_list(self, list_id, **params):
        """
        Retrieve a single contact list by its ID.
        """
        endpoint = f"contactlists/{list_id}"
        return self._request("GET", endpoint, params=params)

    def list_contact_lists(self, **params):
        """
        List all contact lists.
        """
        endpoint = "contactlists"
        return self._request("GET", endpoint, params=params)

    def get_conversation_for_contact(self, contact_id, **params):
        """
        Retrieve conversations associated with a contact.
        """
        endpoint = f"contacts/{contact_id}/conversations"
        return self._request("GET", endpoint, params=params)
