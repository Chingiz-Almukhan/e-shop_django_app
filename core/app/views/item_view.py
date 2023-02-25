from django.views.generic import DetailView

from app.models import Item


class ItemView(DetailView):
    template_name = 'item_view.html'
    model = Item
    context_object_name = 'item'
