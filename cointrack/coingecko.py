__all__ = (
    'TARGET_URL',
    'get_rates',
    'validator',
)
import json
from decimal import Decimal


SOURCE = 'coingecko'
TARGET_URL = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=php'


def validator(html):
    """Returns True if html contains valid data"""
    return 'bitcoin' in json.loads(html.text)


def get_rates(html):
    data = json.loads(html.text).get('bitcoin')
    return [{
        'source': SOURCE,
        'name': 'Bitcoin',
        'symbol': 'BTC',
        'buy_price': Decimal(data.get('php')),
        'sell_price': Decimal(0),
    }]
