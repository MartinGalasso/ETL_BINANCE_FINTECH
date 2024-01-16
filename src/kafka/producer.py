from confluent_kafka import Producer

# Configuración del productor
producer_config = {
    "bootstrap.servers": "localhost:9092"
}

# Crear una instancia del productor
producer = Producer(producer_config)

# Función para manejar la entrega de mensajes
def delivery_report(err, msg):
    if err is not None:
        print('Error al enviar mensaje: {}'.format(err))
    else:
        print('Mensaje enviado a {} [{}]'.format(msg.topic(), msg.partition()))

# Información de ejemplo para cada par de criptomonedas
usdt_data = "Datos para USDT"
btc_data = "Datos para BTC"
eth_data = "Datos para ETH"

# Enviar información a los topics correspondientes
producer.produce("binance_usdt_topic", key="usdt", value=usdt_data, callback=delivery_report)
producer.produce("binance_btc_topic", key="btc", value=btc_data, callback=delivery_report)
producer.produce("binance_eth_topic", key="eth", value=eth_data, callback=delivery_report)

# Esperar a que todos los mensajes se envíen
producer.flush()








