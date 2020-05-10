from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import chat.routing
import feed.routing

application = ProtocolTypeRouter({
    #WebSocket chat handler
    'websocket': AuthMiddlewareStack(
        URLRouter(
            chat.routing.websocket_urlpatterns,
            #feed.routing.websocket_urlpatterns
        )
    ),
})