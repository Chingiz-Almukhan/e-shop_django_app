from django.urls import path

from app.views.base import IndexView
from app.views.buy_item_view import BuyItemView
from app.views.cart_add_view import create_order
from app.views.cart_view import ListCartItem
from app.views.item_view import ItemView

urlpatterns = [
    path('', IndexView.as_view(), name='main'),
    path('item/<int:pk>', ItemView.as_view(), name='item'),
    path('add/<int:pk>', create_order, name='add_to_cart'),
    path('cart', ListCartItem.as_view(), name='cart'),
    path('buy/<int:pk>', BuyItemView.as_view(), name='buy')

]
