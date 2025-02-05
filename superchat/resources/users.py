# superchat/resources/users.py

class UsersMixin:
    def get_me(self, **params):
        """
        Retrieve details about the authenticated user.
        """
        endpoint = "users/me"
        return self._request("GET", endpoint, params=params)

    def list_users(self, **params):
        """
        List users.
        """
        endpoint = "users"
        return self._request("GET", endpoint, params=params)

    def get_user(self, user_id, **params):
        """
        Retrieve a specific user by ID.
        """
        endpoint = f"users/{user_id}"
        return self._request("GET", endpoint, params=params)
