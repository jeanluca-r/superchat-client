# superchat/resources/labels.py

class LabelsMixin:
    def list_labels(self, **params):
        """
        List labels.
        """
        endpoint = "labels"
        return self._request("GET", endpoint, params=params)

    def get_label(self, label_id, **params):
        """
        Retrieve a single label.
        """
        endpoint = f"labels/{label_id}"
        return self._request("GET", endpoint, params=params)
