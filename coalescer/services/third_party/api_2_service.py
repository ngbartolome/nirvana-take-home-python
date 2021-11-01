import os

from coalescer.services.third_party_service import ThirdPartyService


class API2Service(ThirdPartyService):
    def __init__(self):
        ThirdPartyService.__init__(self, os.getenv('API_2_URL'))
