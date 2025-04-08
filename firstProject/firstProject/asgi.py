import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'firstProject.settings')
django.setup()



from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from .routing_socket import websocket_urlpatterns



django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter({
    "http": django_asgi_app,
    "websocket": URLRouter(websocket_urlpatterns)
})
