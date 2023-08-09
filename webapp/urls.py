from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path("make_order/", views.make_order, name="make_order"),
    path("confirm_order/", views.confirm_order, name="confirm_order"),
    path("edit_order/", views.edit_order, name="edit_order"),
    path("order_history/", views.order_history, name="order_history"),
    path("request_history/", views.request_history, name="request_history"),
    path("catalog/", views.catalog, name="catalog"),
    path("shopping_cart/", views.shopping_cart, name="shopping_cart"),
    path("discard_item_from_card", views.discard_item_from_card, name="discard_item_from_card"),
    path("add_item_to_cart", views.add_item_to_cart, name="add_item_to_cart"),
    path("set_cart_amount", views.set_cart_amount, name="set_cart_amount"),
    path("", views.catalog, name="catalog"),
] + static('catalog/', document_root=settings.MEDIA_ROOT) + static('shopping_cart/', document_root=settings.MEDIA_ROOT)
