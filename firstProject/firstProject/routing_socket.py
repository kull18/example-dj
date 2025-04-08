from django.urls import path, re_path
from .consumers import MyRole  # Asegúrate de importar un Consumer válido
from .consumerApp import ChatConsumer

websocket_urlpatterns = [
    path('ws/somepath/', MyRole.as_asgi()),  
]
