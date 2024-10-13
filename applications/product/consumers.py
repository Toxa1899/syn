# applications/product/consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer


class ProductConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("notifications", self.channel_name)
        await self.accept()
        await self.send(
            text_data=json.dumps({"message": "Соединение установлено"})
        )

    async def disconnect(self, close_code):
        # Удаляем клиента из группы
        await self.channel_layer.group_discard(
            "notifications", self.channel_name
        )
        print(f"Соединение закрыто с кодом: {close_code}")

    async def receive(self, text_data):
        data = json.loads(text_data)
        print(f"Получено сообщение: {data}")

    async def send_notification(self, event):
        message = event["message"]["text"]
        await self.send(text_data=json.dumps({"message": message}))
