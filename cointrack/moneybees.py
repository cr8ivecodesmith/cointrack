__all__ = (
    'TARGET_URL',
    'get_rates',
    'validator',
)
from decimal import Decimal


SOURCE = 'moneybees'
TARGET_URL = 'https://hive.moneybees.ph/rates?ccy=php'


def parse_name(cell):
    return cell[0].text.strip()


def parse_price(cell):
    return Decimal(cell[-1].text.replace(',', ''))


def validator(html):
    """Returns True if html contains valid data"""
    prices = [
        i.text or None
        for i in html.find('span[class*="font-rubik tracked"]')
    ]
    return all(prices)


def get_rates(html):
    """Returns a list of all tracked currency rates"""
    # Columns: Coin name, Buy Price, Sell Price
    rates_table = html.find(
        'div#table-view>div>div>div[class*="flex-column"]')[0]
    rates_rows = rates_table.find('div.mb1px.justify-center')[1:]
    data = [{
        'source': SOURCE,
        'name': parse_name(i.find(
            'div.flex.items-center > div > span:nth-child(1)')),
        'symbol': parse_name(i.find(
            'div.flex.items-center > div > span:nth-child(3)')),
        'buy_price': parse_price(i.find('div:nth-child(2)')),
        'sell_price': parse_price(i.find('div:nth-child(3)')),
    } for i in rates_rows]
    return data
