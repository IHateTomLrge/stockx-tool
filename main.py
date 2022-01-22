import requests as req
import os
import platform
os.system('clear' if platform.system() != 'Windows' else 'cls')


def fetch_product(product: str) -> dict:
  print('Fetching product...')
  res = req.get(f'https://stockx.com/api/products/{product}?includes=market,360&currency=EUR&country=FR',
    headers={
      "accept"          : "*/*",
      "accept-encoding" : "gzip, deflate",
      "accept-language" : "en-GB,en;q=0.5",
      "alt-used"        : "stockx.com",
      "appos"           : "web",
      "appversion"      : "0.1",
      "authorization"   : "",
      "connection"      : "keep-alive",
      "host"            : "stockx.com",
      "referer"         : "https://stockx.com/fr-fr/buy/air-jordan-1-retro-high-og-patent-bred",
      "sec-fetch-dest"  : "empty",
      "sec-fetch-mode"  : "cors",
      "sec-fetch-site"  : "same-origin",
      "te"              : "trailers",
      "user-agent"      : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
      "x-requested-with": "XMLHttpRequest",
    }
  )
  
  if res.status_code != 200:
    print('Error fetching product. Status code:', str(res.status_code))
    return ''

  product: dict = res.json().get('Product')
  if product is None:
    print('Error fetching product. Product is None.')
    return ''

  product_obj: dict = {}

  name: str = product.get('shoe')
  colorway: str = product.get('colorway')
  retail: str = str(product.get('retailPrice'))

  product_obj['name'] = name
  product_obj['colorway'] = colorway
  product_obj['retail'] = retail
  product_obj['sizes'] = []

  print(f'\n- Product: {name}\n- Colorway: {colorway}\n- Retail: {retail}€\n')

  childrens: dict = product.get('children')
  if childrens is None:
    print('Error fetching product. No childrens.')
    return ''

  child: dict
  for uuid, child in childrens.items():
    size: str = child.get('shoeSize')
    market: dict = child.get('market')
    asks_count: int = market.get('numberOfAsks')
    lowest_ask: str = str(market.get('lowestAsk'))
    bids_count: int = market.get('numberOfBids')
    highest_bid: str = str(market.get('highestBid'))
    product_obj['sizes'].append({
      'size': size,
      'asks_count': asks_count,
      'lowest_ask': lowest_ask,
      'bids_count': bids_count,
      'highest_bid': highest_bid,
    })
    print(f'---------- SIZE US {size} ----------')
    print(f'Asks: {asks_count}')
    print(f'Lowest ask: {lowest_ask}€')
    print(f'Bids: {bids_count}')
    print(f'Highest bid: {highest_bid}€')
    print('\n')

  return product_obj

product: dict = fetch_product('air-jordan-1-retro-high-og-patent-bred')
# print(product)