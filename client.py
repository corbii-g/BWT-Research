import socket as soc

def client(string):
    server_address = ('127.0.0.1',6700)
        
    with soc.socket(soc.AF_INET, soc.SOCK_STREAM) as client_soc:
        client_soc.connect(server_address)
        
        

if __name__ == "__main__":
    client(input("Stringa: "))