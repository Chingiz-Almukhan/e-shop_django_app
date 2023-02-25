from django.views.generic import ListView

from app.models import Item, Order


class IndexView(ListView):
    template_name = 'main_page.html'
    model = Item
    context_object_name = 'items'
    paginate_by = 10
    paginate_orphans = 1

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        if 'success' in self.request.path:
            orders = Order.objects.all()
            orders.delete()
            context['extra_data'] = 'Заказ оформлен'
        elif 'cancel' in self.request.path:
            context['extra_data'] = 'Заказ отменен'
        return context
