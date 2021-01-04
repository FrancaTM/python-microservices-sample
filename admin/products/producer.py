import pika
import json

params = pika.URLParameters(
    'amqps://przjgusj:mPscfno6Oon2NPFTf_L3l8HdRNfatRau@jackal.rmq.cloudamqp.com/przjgusj')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='main',
                          body=json.dumps(body), properties=properties)
