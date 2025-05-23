from django.urls import re_path

from .consumers import *


websocket_urlpatterns = [
    re_path(r'ws/chat/room/(?P<course_id>\d+)/$', ChatConsumer.as_asgi()),
]
