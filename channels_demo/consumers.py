from channels.generic.websocket import JsonWebsocketConsumer


class BidConsumer(JsonWebsocketConsumer):

    def receive_json(self, content):
        user = self.scope['user']

        print(user)
