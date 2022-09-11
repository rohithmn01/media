import socket

s=socket.socket()
s.connect((socket.gethostname(), 3337))

file = open("/Users/i346327/media/reverseShell/config_mgt/client/temp_file.json", 'wb')
data = s.recv(1024)
print("Hi")
print(data)
while data:
    file.write(data)
    data = s.recv(1024)

file.close()
with open("/Users/i346327/media/reverseShell/config_mgt/client/temp_file.json", 'rb') as f:
    server_data = f.readlines()

with open("/Users/i346327/media/reverseShell/config_mgt/client/file1.json", 'rb') as f:
    client_data = f.readlines()

if server_data != client_data:
    client_data = server_data
    print(client_data)
    with open("/Users/i346327/media/reverseShell/config_mgt/client/file1.json", 'wb') as f:
        for line in client_data:
            f.write(line)

s.close()