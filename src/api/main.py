from time import sleep
import websocket
import json
import pandas as pd


assets = ['BTCUSDT','ETHUSDT','BNBUSDT']
assets = [coin.lower() + '@kline_1m' for coin in assets]
assets = '/'.join(assets)

def manipulation_coin(source):
    rel_data = source['data']['k']['c']
    evt_time = pd.to_datetime(source['data']['E'], unit='ms')
    
    df = pd.DataFrame(rel_data, columns = [source['data']['s']], index=[evt_time])
    
    df['High Price'] = source['data']['k']['h']
    df['Low Price'] = source['data']['k']['l']
    
    df.index.name = 'timestamp'
    df = df.astype(float)
    df = df.reset_index()
    
    print(df)
    return df

def on_message(ws, message):

    message = json.loads(message)
    manipulation_coin(message)
    
def init_ws(on_message):
    socket = f'wss://stream.binance.com:9443/stream?streams='+assets
    ws = websocket.WebSocketApp(socket, on_message=on_message)
        
    ws.run_forever()
    
init_ws(on_message)


