import os
import websocket_server

clients = []


def on_client_connect(client, server):
    clients.append(client)
    print("new connection established")
    print("The custom ID for this client is: %s" % client['id'])


def on_client_disconnect(client, server):
    clients.remove(client)


def on_message(client, server, message):
    print(f'Received message from {client["id"]}: {message}')
    for recipient in clients:
        if recipient != client:
            server.send_message(recipient, f'{client["id"]}: {message}')


port_to_use = int(os.environ.get("PORT", 8080))

server = websocket_server.WebsocketServer(port=port_to_use, host='0.0.0.0')
server.set_fn_new_client(on_client_connect)
server.set_fn_client_left(on_client_disconnect)
server.set_fn_message_received(on_message)
server.run_forever()
