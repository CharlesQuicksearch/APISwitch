import requests
import aiohttp
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

    async def get_sv_sentiment(self, request_data: Request):
        async with aiohttp.ClientSession() as session:
            try:
                api = self.APIS.get("SV_SENTIMENT")
                url = self.BASE_URL + api.get("PORT") + api.get("ENDPOINT")

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
                api = self.APIS.get("EN_SENTIMENT")
                url = self.BASE_URL + api.get("PORT") + api.get("ENDPOINT")
                async with session.post(
                    url,
                    json={"input": request_data.input},
                    headers=self.HEADERS
                ) as response:
                    response.raise_for_status()
                    response_data = await response.json()

                    return response_data

            except requests.RequestException as e:
                raise HTTPException(status_code=500, detail=str(e))

    async def get_topic(self, request_data: Request):
        async with aiohttp.ClientSession() as session:
            try:
                api = self.APIS.get("TOPIC")
                url = self.BASE_URL + api.get("PORT") + api.get("ENDPOINT")
                async with session.post(
                        url,
                        json={"input": request_data.input},
                        headers=self.HEADERS
                ) as response:
                    response.raise_for_status()
                    response_data = await response.json()

                    return response_data

            except requests.RequestException as e:
                raise HTTPException(status_code=500, detail=str(e))

    async def get_translation(self, request_data: TranslationRequest):
        async with aiohttp.ClientSession() as session:
            try:
                api = self.APIS.get("TRANSLATION")
                url = self.BASE_URL + api.get("PORT") + api.get("ENDPOINT")
                async with session.post(
                        url,
                        json={"input": request_data.input,
                              "src_lang": request_data.src_lang,
                              "tgt_lang": request_data.tgt_lang},
                        headers=self.HEADERS
                ) as response:
                    response.raise_for_status()
                    response_data = await response.json()

                    return response_data

            except requests.RequestException as e:
                raise HTTPException(status_code=500, detail=str(e))

    async def get_summarization(self, request_data: Request):
        async with aiohttp.ClientSession() as session:
            try:
                api = self.APIS.get("SUMMARIZE")
                url = self.BASE_URL + api.get("PORT") + api.get("ENDPOINT")
                async with session.post(
                        url,
                        json={"input": request_data.input},
                        headers=self.HEADERS
                ) as response:
                    response.raise_for_status()
                    response_data = await response.json()

                    return response_data

            except requests.RequestException as e:
                raise HTTPException(status_code=500, detail=str(e))
