from channels.consumer import SyncConsumer
from channels.consumer import AsyncConsumer
from channels.exceptions import StopConsumer


class MyAsyncConsumer(AsyncConsumer):
    
    async def websocket_connect(self, event):
        print("websocket connected..////")
        await self.send({
            "type": "websocket.accept",
 })
        
    async def websocket_receive(self, event):
        print("message received from client")
        print("websocket receive..////")
        print(event['text'])
        await self.send({
            "type": "websocket.send",
            "text": event["text"],
            "text":'message send to client',
        })
        
    async def disconnect(self, close_code):
        print("disconnect ..////")   
        raise StopConsumer()    
