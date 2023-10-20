import json


class ExternalApiConfig:
    def __init__(self):
        with open("external_api_config.json") as f:
            config = json.load(f)
        self.BASE_URL = config.get("BASE_URL")
        self.HEADERS = config.get("HEADERS")
        config.close()
