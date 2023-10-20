import requests
import aiohttp, asyncio
from requests_and_responses import *
from fastapi import HTTPException
import json


class ExternalApiHandler:
    def __init__(self):
        with open("Config/external_api_config.json") as f:
            config = json.load(f)
        self.BASE_URL = config.get("BASE_URL")
        self.HEADERS = config.get("HEADERS")
        self.APIS = config.get("APIS")
        f.close()

    async def get_sv_sentiment(self, request_data: Request):
        async with aiohttp.ClientSession() as session:
            try:
                api = self.APIS.get("SV_SENTIMENT")
                url = "http://"+self.BASE_URL + api.get("PORT") + api.get("ENDPOINT")

                print(f"{self.BASE_URL + api.get('PORT') + api.get('ENDPOINT')}")
                async with session.post(
                    url,
                    json={"input": request_data.input},
                    headers=self.HEADERS
                ) as response:
                    response.raise_for_status()
                    response_data = await response.json()

                    return response_data

            except aiohttp.ClientError as e:
                raise HTTPException(status_code=500, detail=str(e))

    async def get_en_sentiment(self, request_data: Request):
        async with aiohttp.ClientSession() as session:
            try:
                async with session.post(
                    self.BASE_URL + self.APIS.EN_SENTIMENT.PORT + self.APIS.EN_SENTIMENT.ENDPOINT,
                    json={"input": request_data.input},
                    headers=self.HEADERS
                ) as response:
                    response.raise_for_status()
                    response_data = response.json()

                    return {"output": response_data}

            except requests.RequestException as e:
                raise HTTPException(status_code=500, detail=str(e))
