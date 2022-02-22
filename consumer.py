# amqps://gomriutw:z5EbOXeymZUDKa1MHZSUc_RTUoJljKYF@puffin.rmq2.cloudamqp.com/gomriutw
import pika, json, os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "micro_services_admin.settings")
django.setup()

from products import models


params      = pika.URLParameters('amqps://gomriutw:z5EbOXeymZUDKa1MHZSUc_RTUoJljKYF@puffin.rmq2.cloudamqp.com/gomriutw')

connection  = pika.BlockingConnection(params)
channel     = connection.channel()

channel.queue_declare(queue='admin')

def callback(ch, method, properties, body):
  print('Received in admin')
  id = json.loads(body)
  print(id)

  product = models.Product.objects.get(id=id)
  product.likes += 1
  product.save()
  print('Product Like Increased')

channel.basic_consume(queue='admin', on_message_callback=callback)

print('Start Consuming ADMIN')

channel.start_consuming()
channel.close()