# Blackbot.me | StockX tool

Small tool for [StockX](https://stockx.com/) to fetch product prices.
This tool has been made in 5 minutes. So it may not contains some necessary info, but you can easily add few lines to retrieve wanted info. 
## Installation

```sh
git clone https://github.com/IHateTomLrge/stockx-tool.git
```

## Requirements

```sh
pip install requests
```

## Usage

```py
product: dict = fetch_product('air-jordan-1-retro-high-og-patent-bred')

# output
{
   "name":"Jordan 1 Retro High OG",
   "colorway":"Black/White-Varsity Red",
   "retail":"170",
   "sizes":[
      {
         "size":"3.5",
         "asks_count":47,
         "lowest_ask":"237",
         "bids_count":21,
         "highest_bid":"214"
      },
      {
         "size":"4",
         "asks_count":41,
         "lowest_ask":"258",
         "bids_count":32,
         "highest_bid":"219"
      },
      {
         "size":"4.5",
         "asks_count":52,
         "lowest_ask":"302",
         "bids_count":41,
         "highest_bid":"236"
      },
      {
         "size":"5",
         "asks_count":65,
         "lowest_ask":"291",
         "bids_count":47,
         "highest_bid":"259"
      },
      {
         "size":"5.5",
         "asks_count":73,
         "lowest_ask":"314",
         "bids_count":48,
         "highest_bid":"260"
      },
      {
         "size":"6",
         "asks_count":82,
         "lowest_ask":"300",
         "bids_count":66,
         "highest_bid":"260"
      },
      {
         "size":"6.5",
         "asks_count":95,
         "lowest_ask":"312",
         "bids_count":65,
         "highest_bid":"270"
      },
      {
         "size":"7",
         "asks_count":245,
         "lowest_ask":"269",
         "bids_count":141,
         "highest_bid":"247"
      },
      {
         "size":"7.5",
         "asks_count":268,
         "lowest_ask":"256",
         "bids_count":172,
         "highest_bid":"243"
      },
      {
         "size":"8",
         "asks_count":503,
         "lowest_ask":"268",
         "bids_count":302,
         "highest_bid":"245"
      },
      {
         "size":"8.5",
         "asks_count":547,
         "lowest_ask":"273",
         "bids_count":446,
         "highest_bid":"240"
      },
      {
         "size":"9",
         "asks_count":826,
         "lowest_ask":"269",
         "bids_count":568,
         "highest_bid":"256"
      },
      {
         "size":"9.5",
         "asks_count":899,
         "lowest_ask":"273",
         "bids_count":597,
         "highest_bid":"247"
      },
      {
         "size":"10",
         "asks_count":937,
         "lowest_ask":"289",
         "bids_count":640,
         "highest_bid":"266"
      },
      {
         "size":"10.5",
         "asks_count":831,
         "lowest_ask":"284",
         "bids_count":555,
         "highest_bid":"261"
      },
      {
         "size":"11",
         "asks_count":738,
         "lowest_ask":"296",
         "bids_count":584,
         "highest_bid":"269"
      },
      {
         "size":"11.5",
         "asks_count":384,
         "lowest_ask":"330",
         "bids_count":250,
         "highest_bid":"293"
      },
      {
         "size":"12",
         "asks_count":581,
         "lowest_ask":"326",
         "bids_count":470,
         "highest_bid":"298"
      },
      {
         "size":"12.5",
         "asks_count":129,
         "lowest_ask":"326",
         "bids_count":74,
         "highest_bid":"290"
      },
      {
         "size":"13",
         "asks_count":351,
         "lowest_ask":"338",
         "bids_count":259,
         "highest_bid":"295"
      },
      {
         "size":"14",
         "asks_count":134,
         "lowest_ask":"362",
         "bids_count":93,
         "highest_bid":"310"
      },
      {
         "size":"15",
         "asks_count":53,
         "lowest_ask":"342",
         "bids_count":62,
         "highest_bid":"294"
      },
      {
         "size":"16",
         "asks_count":48,
         "lowest_ask":"294",
         "bids_count":22,
         "highest_bid":"257"
      },
      {
         "size":"17",
         "asks_count":9,
         "lowest_ask":"729",
         "bids_count":10,
         "highest_bid":"238"
      },
      {
         "size":"18",
         "asks_count":7,
         "lowest_ask":"345",
         "bids_count":9,
         "highest_bid":"192"
      }
   ]
}
```