import socket
from datetime import datetime

rServer = input("IP Adresini Giriniz: ")
zamanAsimi = 3 #Saniye başına bağlantı(tarama)

try:
    for port in range(20,1001): # Aralağında port taraması yapar.
        baglanti = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        baglanti.settimeout(zamanAsimi)
        sonuc = baglanti.connect_ex((rServer, port))

        if sonuc == 0:
            print("Port", str(port), "'Açık'")
        else:
            print("Port", str(port), "'Kapalı'")

except Exception as hata:
    print(str(hata))
