import socket
import json
import threading

def handle(conn, slave_conn, address):
    connected = True
    while connected:
        inp = conn.recv(4000).decode("utf-8")
        if inp == "quit":
            connected = False
        else:
            data = inp.split(" ")
            req = data[0]
            key = data[1]

            with open("data.json", 'r') as f:
                m = f.read()
                json_data = json.loads(m)
            if req == "/get":
                for k,v in json_data.items():
                    if k == key:
                        data = v
                        break
                conn.send(data.encode("utf-8"))
            elif req == "/set":
                value = data[2]
                json_data.update({key:value})
                print(json_data)
                with open("data.json", 'w') as f:
                    json.dump(json_data, f)
                mgs = f"{key}:{value}"
                conn.send(mgs.encode("utf-8"))
                slave_conn.send(json_data.encode("utf-8"))



            elif req == "/delete":
                if key not in json_data:
                    conn.send(f"key not present".encode("utf-8"))
                else:
                    del json_data[key]
                    with open("data.json", 'w') as f:
                        json.dump(json_data, f)
                    mgs = f"deleted {key}"
                    conn.send(mgs.encode("utf-8"))
                    slave_conn.sendall(bytes(json_data, encoding="utf-8"))


            print(json_data)
    conn.close()


def main():
    s=socket.socket()
    s.bind((socket.gethostname(),4436))
    s.listen()
    print("listening..>!")

    slave_ser = socket.socket()
    slave_ser.bind((socket.gethostname(),5555))
    slave_ser.listen()

    

    while True:
        conn, address = s.accept()
        slave_conn, add = slave_ser.accept()
        thread = threading.Thread(target=handle, args=(conn, slave_conn, address))
        thread.start()
    s.close()

if __name__ == "__main__":
    main()