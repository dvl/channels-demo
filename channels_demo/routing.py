from django.urls import path

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter

from .consumers import BidConsumer


application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter([
            path('bids/', BidConsumer)
        ])
    ),
})
