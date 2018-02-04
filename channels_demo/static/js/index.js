ws = new channels.WebSocketBridge()
ws.connect('/bids/')

ws.listen((action, stream) => {
  console.log(action, stream)
})

ws.socket.addEventListener('open', () => {
  document.getElementById('status').innerHTML += 'websocket connected\n'
})

ws.socket.addEventListener('close', () => {
  document.getElementById('status').innerHTML += 'websocket disconnected\n'
})
