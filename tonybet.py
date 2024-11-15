# list ? isTop_eq
# https://platform.tonybet.lv/api/event/list?isTopLive_eq=1&competitor2Id_neq=&competitor1Id_neq=&status_in[]=2&status_in[]=1&oddsExists_eq=1&main=1&limit=5&relations[]=odds&relations[]=league&relations[]=result&relations[]=competitors&relations[]=players&relations[]=sportCategories&relations[]=broadcasts&relations[]=statistics&relations[]=additionalInfo&relations[]=withMarketsCount&relations[]=tips&period=0&lang=en

# list ? isTop
# https://platform.tonybet.lv/api/event/list?isTop_eq=1&oddsExists_eq=1&competitor2Id_neq=&competitor1Id_neq=&main=1&status_in[]=0&period=0&limit=5&relations[]=league&relations[]=odds&relations[]=competitors&relations[]=sportCategories&relations[]=players&relations[]=withMarketsCount&relations[]=tips&lang=en

# https://platform.tonybet.lv/api/event/list?isTop_eq=1&oddsExists_eq=1&competitor2Id_neq=&competitor1Id_neq=&main=1&status_in[]=0&period=0&limit=5&relations[]=league&relations[]=odds&relations[]=competitors&relations[]=sportCategories&relations[]=players&relations[]=withMarketsCount&relations[]=tips&lang=en

# https://platform.tonybet.lv/api/v3/menu/leagues/top-live/en

# https://platform.tonybet.lv/api/variant/list?lang=en&variantId_in[]=262&variantId_in[]=261&variantId_in[]=260&variantId_in[]=263&variantId_in[]=264&variantId_in[]=265&variantId_in[]=195&variantId_in[]=197&variantId_in[]=196

# https://platform.tonybet.lv/api/variant/list?lang=en&variantId_in[]=266&variantId_in[]=267

#https://platform.tonybet.lv/api/event/list?isTopLive_eq=1&competitor2Id_neq=&competitor1Id_neq=&status_in[]=2&status_in[]=1&oddsExists_eq=1&main=1&limit=30&relations[]=odds&relations[]=league&relations[]=result&relations[]=competitors&relations[]=players&relations[]=sportCategories&relations[]=broadcasts&relations[]=statistics&relations[]=additionalInfo&relations[]=withMarketsCount&relations[]=tips&period=0&lang=en

#https://platform.tonybet.lv/api/v2/menu/leagues/top-live/en

# https://platform.tonybet.lv/api/event/list?isTopLive_eq=1&competitor2Id_neq=&competitor1Id_neq=&status_in[]=2&status_in[]=1&oddsExists_eq=1&main=1&limit=30&relations[]=odds&relations[]=league&relations[]=result&relations[]=competitors&relations[]=players&relations[]=sportCategories&relations[]=broadcasts&relations[]=statistics&relations[]=additionalInfo&relations[]=withMarketsCount&relations[]=tips&period=0&lang=en

# wss://centrifugo.tonybet.lv/connection/websocket 

import asyncio
import websockets

async def connect_to_websocket():
    uri = "wss://centrifugo.tonybet.lv/connection/websocket"  # Replace with the correct WebSocket URL if needed

    headers = {
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "en-US,en;q=0.9",
        "Cache-Control": "no-cache",
        "Connection": "Upgrade",
        "Host": "centrifugo.tonybet.lv",
        "Origin": "https://tonybet.lv",
        "Pragma": "no-cache",
        "Sec-WebSocket-Extensions": "permessage-deflate; client_max_window_bits",
        "Sec-WebSocket-Key": "fky6YwlHsDrfABKrFmTsxg==",  # This key is generated per connection; the server might regenerate it
        "Sec-WebSocket-Version": "13",
        "Upgrade": "websocket",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
    }

    async with websockets.connect(uri, extra_headers=headers) as websocket:
        print("Connected to WebSocket server")
        
        while True:
            try:
                message = await websocket.recv()
                print("Received message:", message)
            except websockets.ConnectionClosed:
                print("Connection closed")
                break

# Run the WebSocket connection
asyncio.run(connect_to_websocket())
