# superchat/exceptions.py

class SuperchatAPIError(Exception):
    """General exception for Superchat API errors."""
    def __init__(self, status_code, message):
        super().__init__(f"HTTP {status_code}: {message}")
        self.status_code = status_code
        self.message = message

class RateLimitError(SuperchatAPIError):
    """Exception raised when the API returns a rate limit error (HTTP 429)."""
    pass
