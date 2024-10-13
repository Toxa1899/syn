from django.urls import path

from .consumers import ProductConsumer

websocket_urlpatterns = [
    path("ws/notifications/", ProductConsumer.as_asgi()),
]
