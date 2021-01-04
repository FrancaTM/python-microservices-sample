import pika

params = pika.URLParameters(
    'amqps://przjgusj:mPscfno6Oon2NPFTf_L3l8HdRNfatRau@jackal.rmq.cloudamqp.com/przjgusj')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish():
    channel.basic_publish(exchange='', routing_key='admin', body='hello')
