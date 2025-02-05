# superchat/resources/channels.py

class ChannelsMixin:
    def get_channel(self, channel_id, **params):
        """
        Retrieve details for a specific channel.
        """
        endpoint = f"channels/{channel_id}"
        return self._request("GET", endpoint, params=params)

    def list_channels(self, **params):
        """
        List channels.
        """
        endpoint = "channels"
        return self._request("GET", endpoint, params=params)
