import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("vitima", 80, 440, 28, 88))
client.send("scan")

