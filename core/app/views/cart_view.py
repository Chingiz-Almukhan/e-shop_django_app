from django.views.generic import ListView

from app.models import Order


class ListCartItem(ListView):
    model = Order
    context_object_name = 'items'
    template_name = 'list_cart.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        cart = Order.objects.all()
        context['item'] = cart.count()
        total = 0
        for price in cart:
            total += price.item.price
        context['total'] = total
        return context
