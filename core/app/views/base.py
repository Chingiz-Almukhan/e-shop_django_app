from django.views.generic import ListView

from app.models import Item


class IndexView(ListView):
    template_name = 'main_page.html'
    model = Item
    context_object_name = 'items'
    paginate_by = 10
    paginate_orphans = 1
