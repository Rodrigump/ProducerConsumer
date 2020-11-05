from kafka import KafkaConsumer

consumer = KafkaConsumer('topico')

for msg in consumer:
    print(msg.value.decode("utf-8")) #converte as mensagens de byte para str e as imprime