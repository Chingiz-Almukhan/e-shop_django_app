import stripe
from django.conf import settings
from django.http import JsonResponse
from django.urls import reverse
from django.views import View

from app.models import Item

stripe.api_key = settings.STRIPE_SECRET_KEY


class BuyItemView(View):
    def get(self, request, *args, **kwargs):
        item = Item.objects.get(pk=self.kwargs["pk"])

        success_url = request.build_absolute_uri(reverse('success'))
        cancel_url = request.build_absolute_uri(reverse('cancel'))

        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': 'usd',
                        'unit_amount': item.price,
                        'product_data': {
                            'name': item.name,
                        },
                    },
                    'quantity': 1,
                },
            ],
            metadata={
                "product_id": item.id
            },
            mode='payment',
            success_url=success_url,
            cancel_url=cancel_url,
        )
        return JsonResponse({
            'session_id': checkout_session.id,
            'stripe_public_key': settings.STRIPE_PUBLISHABLE_KEY
        })
