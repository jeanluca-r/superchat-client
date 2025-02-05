# superchat/resources/templates.py

class TemplatesMixin:
    def list_templates(self, **params):
        """
        List message templates.
        """
        endpoint = "templates"
        return self._request("GET", endpoint, params=params)

    def create_template(self, **data):
        """
        Create a new message template.
        """
        endpoint = "templates"
        return self._request("POST", endpoint, json=data)

    def get_template(self, template_id, **params):
        """
        Retrieve a specific template.
        """
        endpoint = f"templates/{template_id}"
        return self._request("GET", endpoint, params=params)

    def delete_template(self, template_id, **params):
        """
        Delete a template.
        """
        endpoint = f"templates/{template_id}"
        return self._request("DELETE", endpoint, params=params)
