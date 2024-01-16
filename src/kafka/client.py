from confluent_kafka.admin import AdminClient, NewTopic

def create_admin(name_topic):
    admin_client = AdminClient({
        "bootstrap.servers": "localhost:9092",  
    })

    topic_list = []
    topic_list.append(NewTopic("info_binance", 1, 1))
    
    # Asegúrate de que el topic no exista antes de intentar crearlo para evitar errores.
    existing_topics = admin_client.list_topics().topics
    if name_topic not in existing_topics:
        topic_create = admin_client.create_topics(topic_list)
        print(topic_create)
        return topic_create
    else:
        print("El tema {} ya existe.".format('name_topic'))
        return None
    
create_admin('info_binance')