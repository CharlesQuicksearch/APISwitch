import json
import uvicorn

from Endpoints_Handler.endpoints import Endpoints
from external_api_handler import ExternalApiHandler
from fastapi import FastAPI, HTTPException
from requests_and_responses import *

app = FastAPI()
ExternalApiHandler = ExternalApiHandler()


@app.get(Endpoints.HOME)
async def get_home():
    return "API Switch"


@app.post(Endpoints.SV_SENTIMENT, response_model=SvSentimentResponse)
async def get_sv_sentiment(request_data: Request):
    try:
        result = await ExternalApiHandler.get_sv_sentiment(request_data)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post(Endpoints.EN_SENTIMENT, response_model=EnSentimentResponse)
async def get_en_sentiment(request_data: Request):
    try:
        result = await ExternalApiHandler.get_en_sentiment(request_data)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post(Endpoints.TOPIC, response_model=TopicResponse)
async def get_en_sentiment(request_data: Request):
    try:
        result = await ExternalApiHandler.get_topic(request_data)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post(Endpoints.TRANSLATION, response_model=TranslationResponse)
async def get_translation(request_data: TranslationRequest):
    try:
        result = await ExternalApiHandler.get_translation(request_data)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post(Endpoints.SUMMARIZE_TEXT, response_model=SummarizeResponse)
async def get_summarization(request_data: Request):
    try:
        result = await ExternalApiHandler.get_summarization(request_data)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


def main():
    with open("Config/app_config.json") as f:
        config = json.load(f)

    host = config.get("HOST")
    port = config.get("PORT")

    uvicorn.run(app, host=host, port=port)


if __name__ == "__main__":
    main()
