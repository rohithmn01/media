import socket

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 3335))
print(socket.gethostname())
# full_msg = ""
# while True:
#     msg = s.recv(2048)
#     if len(msg) <= 0:
#         break
#     full_msg += msg.decode("utf-8")
#     #print(msg.decode("utf-8"))
# if full_msg == "ping":
#         print(f"pong")
# else:
#     print(full_msg)

s.send(bytes("pingg", "utf-8"))
print(s.recv(1024).decode("utf-8"))