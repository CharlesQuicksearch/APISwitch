from typing import List

from pydantic import BaseModel


class Request(BaseModel):
    input: str


class TranslationRequest(BaseModel):
    input: str
    src_lang: str
    tgt_lang: str


class SvSentimentResponse(BaseModel):
    output: List[float]


class EnSentimentResponse(BaseModel):
    output: List[float]


class DetectLanguageResponse(BaseModel):
    output: List[str]


class TopicResponse(BaseModel):
    output: List[str]


class SummarizeResponse(BaseModel):
    output: str


class TranslationResponse(BaseModel):
    output: str
    score: float
