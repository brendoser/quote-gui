# Python Packages
import json
import string
import requests
from enum import Enum


class FormEnum(Enum):
    @classmethod
    def from_formatted(cls, formatted):
        raise NotImplementedError()

    def formatted(self):
        return string.capwords(' '.join(self.name.split('_')))


class CATEGORIES(FormEnum):
    ANY_TOPIC = 'ANY_TOPIC'
    NONFICTION = 'NONFICTION'
    FICTION = 'FICTION'

    @classmethod
    def from_formatted(cls, formatted):
        return cls['_'.join(formatted.split(' ')).upper()]


class SUB_CATEGORIES(FormEnum):
    ANY_TOPIC = ''
    ANY_NONFICTION = 'nonfiction/'
    BIOGRAPHY = 'biography/'
    BIOLOGY = 'biology/'
    BUSINESS = 'business/'
    ECONOMICS = 'economics/'
    FOOD = 'food/'
    HISTORY = 'history/'
    MATHEMATICS = 'mathematics/'
    MEMOIR = 'memoir/'
    PHILOSOPHY = 'philosophy/'
    PHYSICS = 'physics/'
    POLITICS = 'politics/'
    PSYCHOLOGY = 'psychology/'
    SCIENCE = 'science/'
    SELF_HELP = 'self-help/'
    TECHNOLOGY = 'technology/'
    WRITING = 'writing/'
    ANY_FICTION = 'fiction/'
    FANTASY = 'fantasy/'
    HISTORICAL_FICTION = 'historical-fiction/'
    HUMOR = 'humor/'
    LITERATURE = 'literature/'
    MYSTERY = 'mystery/'
    SCIENCE_FICTION = 'science-fiction/'
    THRILLER = 'thriller/'

    @classmethod
    def from_formatted(cls, formatted):
        return cls['_'.join(formatted.split(' ')).upper()]


class LENGTHS(FormEnum):
    ANY_LENGTH = ''
    SHORT = 'short'
    MEDIUM = 'medium'
    LONG = 'long'

    @classmethod
    def from_formatted(cls, formatted):
        return cls['_'.join(formatted.split(' ')).upper()]


class Form:
    LENGTHS_LIST = [
        LENGTHS.ANY_LENGTH.formatted(),
        LENGTHS.SHORT.formatted(),
        LENGTHS.MEDIUM.formatted(),
        LENGTHS.LONG.formatted()
    ]
    CATEGORIES_LIST = [
        CATEGORIES.ANY_TOPIC.formatted(),
        CATEGORIES.FICTION.formatted(),
        CATEGORIES.NONFICTION.formatted()
    ]
    SUB_CATEGORY_MAP = {
        CATEGORIES.ANY_TOPIC.formatted(): [
            SUB_CATEGORIES.ANY_TOPIC.formatted()
        ],
        CATEGORIES.NONFICTION.formatted(): [
            SUB_CATEGORIES.ANY_NONFICTION.formatted(),
            SUB_CATEGORIES.BIOGRAPHY.formatted(),
            SUB_CATEGORIES.BIOLOGY.formatted(),
            SUB_CATEGORIES.BUSINESS.formatted(),
            SUB_CATEGORIES.ECONOMICS.formatted(),
            SUB_CATEGORIES.FOOD.formatted(),
            SUB_CATEGORIES.HISTORY.formatted(),
            SUB_CATEGORIES.MATHEMATICS.formatted(),
            SUB_CATEGORIES.MEMOIR.formatted(),
            SUB_CATEGORIES.PHILOSOPHY.formatted(),
            SUB_CATEGORIES.PHYSICS.formatted(),
            SUB_CATEGORIES.POLITICS.formatted(),
            SUB_CATEGORIES.PSYCHOLOGY.formatted(),
            SUB_CATEGORIES.SCIENCE.formatted(),
            SUB_CATEGORIES.SELF_HELP.formatted(),
            SUB_CATEGORIES.TECHNOLOGY.formatted(),
            SUB_CATEGORIES.WRITING.formatted()
        ],
        CATEGORIES.FICTION.formatted(): [
            SUB_CATEGORIES.ANY_FICTION.formatted(),
            SUB_CATEGORIES.FANTASY.formatted(),
            SUB_CATEGORIES.HISTORICAL_FICTION.formatted(),
            SUB_CATEGORIES.HUMOR.formatted(),
            SUB_CATEGORIES.LITERATURE.formatted(),
            SUB_CATEGORIES.MYSTERY.formatted(),
            SUB_CATEGORIES.SCIENCE_FICTION.formatted(),
            SUB_CATEGORIES.THRILLER.formatted()
        ]
    }

    def __init__(self, category: FormEnum = CATEGORIES.ANY_TOPIC, sub_category: FormEnum = SUB_CATEGORIES.ANY_TOPIC,
                 length: FormEnum = LENGTHS.ANY_LENGTH):
        self._url = r'https://www.how-to-type.com/typing-practice/quote/json/'
        self.category = category
        self.sub_category = sub_category
        self.length = length

    def _get_formatted_url(self):
        return f'{self._url}{self.sub_category.value}?length={self.length.value}'

    def get_quote_data(self):
        url = self._get_formatted_url()
        try:
            sauce = requests.get(url, timeout=5).text
            data = json.loads(sauce)
        except Exception as e:
            print(e)
            data = None
        return QuoteData.from_json(data) if data else None


class QuoteData:

    def __init__(self, text, title, author, link, img_link):
        self.text = text
        self.title = title
        self.author = author
        self.link = link
        self.img_link = img_link

    @classmethod
    def from_json(cls, json_formatted):
        return cls(
            json_formatted['text'],
            json_formatted['source']['title'],
            json_formatted['source']['creator'],
            json_formatted['source']['link'],
            json_formatted['source']['img_link']
        )
