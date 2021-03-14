import json
import pika

params = pika.URLParameters('amqps://gibeeuvk:uP6VPF2eXt9aulsp9WjALuW7twR9BEcJ@puffin.rmq2.cloudamqp.com/gibeeuvk')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='main', body=json.dumps(body), properties=properties)
