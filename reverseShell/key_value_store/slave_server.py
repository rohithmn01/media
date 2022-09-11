import socket
import json

s=socket.socket()
s.connect((socket.gethostname(), 5555))
json_obj = s.recv(1024).decode("utf-8")
with open("slave_data.json", 'w') as f:
    json.dump(json_obj, f)

