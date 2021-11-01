import requests


class ThirdPartyService():
    def __init__(self, url: str):
        self.url = url

    """Avoids instantiating this class"""
    def __new__(cls, *args, **kwargs):
        if cls is ThirdPartyService:
            raise TypeError(
                f"Only children of '{cls.__name__}' may be instantiated")
        return object.__new__(cls, *args, **kwargs)

    """Returns a dict according to the member_id parameter"""
    async def get_patient(self, member_id: int) -> dict:
        response = requests.get(self.url, params={
            'member_id': member_id})
        return response.json()
