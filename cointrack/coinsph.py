__all__ = (
    'TARGET_URL',
    'get_rates',
    'validator',
)
import json
from decimal import Decimal


SOURCE = 'coins.ph'
TARGET_URL = 'https://quote.coins.ph/v1/markets/BTC-PHP'


def validator(html):
    """Returns True if html contains valid data"""
    return 'market' in json.loads(html.text)


def get_rates(html):
    data = json.loads(html.text).get('market')
    return [{
        'source': SOURCE,
        'name': 'Bitcoin',
        'symbol': data.get('product'),
        'buy_price': Decimal(data.get('ask')),
        'sell_price': Decimal(data.get('bid')),
    }]
