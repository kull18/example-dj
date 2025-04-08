import json
from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer

class MyRole(AsyncWebsocketConsumer):
    async def receive(self, text_data=None, bytes_data=None):
        if text_data:
         print(text_data)
         data = json.loads(text_data)
        print(data)
        DATa = data.get("role", {})

        description = DATa.get("description")
        if not description:
            print("Error: Descripción vacía")
            await self.send(json.dumps({"error": "Description is required"}))
            return

        message = await self.createRole(description)
        print("Rol creado:", message.description)

        await self.send(json.dumps({
            "message": f"Role '{message.description}' created successfully"
        }))

    @database_sync_to_async
    def createRole(self, description):
        return Role.objects.create(description=description)

    @database_sync_to_async
    def get_roles(self):
        return list(Role.objects.all().values())  # Devuelve una lista de roles


