import json
import uvicorn

from external_api_handler import ExternalApiHandler
from fastapi import FastAPI
from requests_and_responses import *


app = FastAPI()
ExternalApiHandler = ExternalApiHandler()

@app.get("/home")
async def get_home():
    print("home")
    return "HI"

@app.post("/swe_sentiment/", response_model=SvSentimentResponse)
async def get_sv_sentiment(request_data: Request):
    print("get_sv_sentiment")
    result = await ExternalApiHandler.get_sv_sentiment(request_data)
    return result


def main():
    with open("Config/app_config.json") as f:
        config = json.load(f)
    HOST = config.get("HOST")
    PORT = config.get("PORT")
    f.close()
    print(f"Hosting: {HOST}:{PORT}")
    uvicorn.run(app, host=HOST, port=PORT)


if __name__ == "__main__":
    main()
    #uvicorn.run(app, host=HOST, port=PORT)
