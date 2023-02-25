from django.shortcuts import redirect

from app.models import Order, Item


def create_order(*args, **kwargs):
    item = Item.objects.get(pk=kwargs.get('pk'))
    order = Order.objects.create(item=item)
    order.save()
    return redirect('cart')
