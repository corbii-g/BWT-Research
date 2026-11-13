import socket as soc

def client(string):
    server_address = ('127.0.0.1',6700)
        
    with soc.socket(soc.AF_INET, soc.SOCK_STREAM) as client_soc:
        client_soc.connect(server_address)
        client_soc.sendall(string.encode('utf-8'))
        
        data = client_soc.recv(1024)

        return data.decode('utf-8')
        

if __name__ == "__main__":
    client(input("Stringa: "))