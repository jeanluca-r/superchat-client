# superchat/resources/files.py

class FilesMixin:
    def create_file(self, files, **data):
        """
        Upload a file.

        Args:
            files: A dictionary of file field names to file objects,
                   e.g. {'file': open('path/to/file', 'rb')}
            data: Additional data fields if required.
        """
        endpoint = "files"
        return self._request("POST", endpoint, data=data, files=files)

    def list_files(self, **params):
        """
        List uploaded files.
        """
        endpoint = "files"
        return self._request("GET", endpoint, params=params)

    def get_file(self, file_id, **params):
        """
        Retrieve file details or content.
        """
        endpoint = f"files/{file_id}"
        return self._request("GET", endpoint, params=params)

    def delete_file(self, file_id, **params):
        """
        Delete a file.
        """
        endpoint = f"files/{file_id}"
        return self._request("DELETE", endpoint, params=params)
