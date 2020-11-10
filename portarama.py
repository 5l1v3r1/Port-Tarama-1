import socket
from datetime import datetime

rServer = input("IP Adresini Giriniz: ")
zamanAsımı = 3 #Saniye başına bağlantı(tarama)

try:
    for port in range(20,1001): # Aralağında port taramsı yapar.
        baglantı = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        baglantı.settimeout(zamanAsımı)
        sonuc = baglantı.connect_ex((rServer, port))

        if sonuc == 0:
            print("Port", str(port), "'Açık'")
        else:
            print("Port", str(port), "'Kapalı'")

except Exception as hata:
    print(str(hata))
