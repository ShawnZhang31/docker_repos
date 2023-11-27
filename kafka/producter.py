from kafka import KafkaProducer
import json

producer = KafkaProducer(bootstrap_servers='localhost:9092',
                        value_serializer=lambda m: json.dumps(m).encode('ascii'))

# 定义异步推送回调

def on_send_success(record_metadata):
    print(record_metadata.topic)
    print(record_metadata.partition)
    print(record_metadata.offset)

def on_send_error(excp):
    print('I am an errback', exc_info=excp)


for _ in range(1000):
    producer.send('foo', {"key":f"test{_}"}).add_callback(on_send_success).add_errback(on_send_error)
    print(f"senf no.{_+1}")