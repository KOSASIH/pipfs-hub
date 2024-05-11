import pika

def create_message_queue(host, port, username, password, queue_name):
    # Create a message queue using RabbitMQ or Apache Kafka

    connection = pika.BlockingConnection(pika.ConnectionParameters(host=host, port=port, credentials=pika.PlainCredentials(username=username, password=password)))
    channel = connection.channel()
    channel.queue_declare(queue=queue_name)

    return channel

def send_message(channel, queue_name, message):
    # Send a message to a message queue

    channel.basic_publish(exchange='', routing_key=queue_name, body=message)

def receive_message(channel, queue_name):
    # Receive a message from a message queue

    method_frame, header_frame, body = channel.basic_consume(queue=queue_name)
    channel.basic_ack(delivery_tag=method_frame.delivery_tag)

    return body.decode()
