from channels.generic.websocket import AsyncWebsocketConsumer
import json


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        self.room_group_name = 'group_chat_gfg'
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        print(f'Успешное подключение: {self.channel_name}')

    async def disconnect(self, code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
        print(f'Клиент отключился: {self.channel_name}')

    async def receive(self, text_data=None, bytes_data=None):
        try:
            text_data_json = json.loads(text_data)
            message = text_data_json['message']
            username = text_data_json['username']
            await self.channel_layer.group_send(
                self.room_group_name, {
                    'type': 'send_message',
                    'message': message,
                    'username': username,
                }
            )
        except Exception as e:
            print(f'Ошибка: {e}')

    async def send_message(self, event):
        message = event['message']
        username = event['username']
        await self.send(text_data=json.dumps({'message': message, 'username': username}))
