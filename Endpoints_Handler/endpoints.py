from enum import Enum, StrEnum


class Endpoints(StrEnum):
    HOME = "/home"
    SV_SENTIMENT = "/swe_sentiment/",
    EN_SENTIMENT = "/eng_sentiment/",
    TOPIC = "/categorize/healthcare",
    SUMMARIZE_TEXT = "/summarize/",
    TRANSLATION = "/translate/"
