Cointrack
=========


Crypto rates tracker for Goingecko, Coins.ph, Moneybees.ph


## Installation

```
pip install -r requirements.txt
```

## Usage

```
./get_rates
```

Output:  

```
Getting Bitcoin market rates as of: 2022-03-08 15:36:53.711127

====================
CoinGecko Rates
====================
{'buy_price': Decimal('2006145'),
 'name': 'Bitcoin',
 'sell_price': Decimal('0'),
 'source': 'coingecko',
 'symbol': 'BTC'}
====================
Coins.ph Rates
====================
{'buy_price': Decimal('2056035.24'),
 'name': 'Bitcoin',
 'sell_price': Decimal('1974690.56'),
 'source': 'coins.ph',
 'symbol': 'BTC'}
====================
Moneybees Rates
====================
{'buy_price': Decimal('2042989.22'),
 'name': 'Bitcoin',
 'sell_price': Decimal('1957812.39'),
 'source': 'moneybees',
 'symbol': 'BTC'}
```
