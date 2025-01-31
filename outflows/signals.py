import requests

from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Outflow


@receiver(post_save, sender=Outflow)
def update_product_quantity(sender, instance, created, **kwargs):
    if created:
        if instance.quantity > 0:
            product = instance.product
            product.quantity -= instance.quantity
            product.save()


        ### WEBHOOKS --
@receiver(post_save, sender=Outflow)
def send_outflows_event(sender, instance, **kwargs):
    data = {
        'produto': instance.product.title,
        'quantidade': instance.quantity,
        'descrição': instance.description,
    }
    requests.post(
        url='http://localhost:8001/api/v1/webhooks/',
        json=data,
    )
#https://webhook.site/2fe503ef-2559-4449-849a-4ea7dd647a70
    