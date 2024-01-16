from time import sleep
import websocket
import json
import pandas as pd


assets = ['BTCUSDT','ETHUSDT','BNBUSDT'] #Lista de monedas
assets = [coin.lower() + '@kline_1m' for coin in assets] # Devuelve la lista en low + @...
assets = '/'.join(assets) 

def manipulation_coin(source):
    rel_data = source['data']['k']['c']
    evt_time = pd.to_datetime(source['data']['E'], unit='ms') #Convert datetime.
    
    df = pd.DataFrame(rel_data, columns = [source['data']['s']], index=[evt_time]) #Convierte en dataframe
    
    df['High Price'] = source['data']['k']['h']
    df['Low Price'] = source['data']['k']['l']
    
    df.index.name = 'timestamp'
    df = df.astype(float)
    df = df.reset_index()
    
    print(df)
    return df

""" 
Mensaje que envia websocket
"""

def on_message(ws, message):

    message = json.loads(message)
    manipulation_coin(message)
    
""" 
INICIA EL PROGRAMA
"""
def init_ws(on_message):
    socket = f'wss://stream.binance.com:9443/stream?streams='+assets #API
    ws = websocket.WebSocketApp(socket, on_message=on_message)
        
    ws.run_forever()
    
init_ws(on_message)


