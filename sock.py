import sys
import socket

class Utama():
    def __init__(self):
        print("Masukan pilhan anda: ")
        print("(1) sebagai server")
        print("(2) sebagai client ")
        print("(3) keluar ")
        
        pilihan = input("Pilihan anda adalah: ")
        
        if pilihan == "1":
            lokasi = socket.gethostbyname("127.0.0.1")
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # 2120 nomor port diisi terserah
            s.bind((lokasi, 2120))
            # 5 adalah jumlah koneksi yang boleh menghubungi server
            s.listen(5)
            print("Server sudah aktif")
            
            client, alamat = s.accept()
            print("Menerima data dari: ", alamat)
            while True:
                # decode jika data dikirim
                data = client.recv(1024).decode()
                if not data:
                    break
                print("Pesan masuk: ", str(data))
                data = input(">")
                # encode data diterima
                client.send(data.encode())
        elif pilihan =="2":
            alamatServer = input("Masukan alamat server: ")
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((alamatServer, 2120))
            pesan = input(">")
            while pesan != "bye":
                s.send(pesan.encode())
                data = s.recv(1024).decode()
                print("Server: ", data)
                pesan(input(">"))
            s.close()      
        else:
            quit()
    
if __name__ == "__main__":
    Utama()
    sys.exit()