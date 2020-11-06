from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='localhost:9092')

list_msg = ['Olá', 'Este é um exemplo', 'De produtor e consumidor'] #lista de mensagens a serem enviadas

for msg in list_msg:
    future = producer.send('topico', str.encode(msg)) #converte a mensagem para bytes
    result = future.get(timeout=60) #bloqueia ate o envio da mensagem
