import json


class AppConfig:
    def __init__(self):
        with open("app_config.json") as f:
            config = json.load(f)
        self.HOST = config.get("HOST")
        self.PORT = config.get("PORT")
        config.close()
