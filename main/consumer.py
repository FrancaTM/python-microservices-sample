import pika

params = pika.URLParameters(
    'amqps://przjgusj:mPscfno6Oon2NPFTf_L3l8HdRNfatRau@jackal.rmq.cloudamqp.com/przjgusj')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='main')


def callback(ch, method, properties, body):
    print('Received in main')
    print(body)


channel.basic_consume(queue='main', on_message_callback=callback)

print('Started consuming...')
channel.start_consuming()

channel.close()