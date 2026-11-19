import socket as soc
from bwt import get_bwt_from_string as get_bwt

server_addr = ('127.0.0.1', 6700)

with soc.socket(soc.AF_INET, soc.SOCK_STREAM) as server_soc:
    server_soc.bind(server_addr)
    server_soc.listen()
    print("Server attivo...")

    while True:
        client_soc, client_addr = server_soc.accept()
    
        with client_soc:
                print("Connessione con:", client_addr)
                data = client_soc.recv(1024)

                string = data.decode("utf-8")
                print("Stringa ricevuta:", string)

                bwt_string = get_bwt(string)
                client_soc.sendall(bwt_string.encode("utf-8"))
                print("Stringa BWT inviata:", bwt_string)

                # segnala al client che hai finito di inviare
                client_soc.shutdown(soc.SHUT_WR)
        
                client_soc.close()