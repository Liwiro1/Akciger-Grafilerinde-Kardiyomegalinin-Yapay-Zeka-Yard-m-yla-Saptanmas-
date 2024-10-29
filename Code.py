import os
import numpy as np

# İşlem yapılacak dosya yolunu belirle
dosya_yolu = "labels"

# Dosyaları dolaşmak için bir döngü oluştur
for dosya in os.listdir(dosya_yolu):
    if dosya.endswith(".txt"):
        # Dosyayı aç ve içeriğini oku
        with open(os.path.join(dosya_yolu, dosya), "r") as f:
            icerik = f.readlines()
        
        # Her bir satırı kontrol edin ve gerekli koordinatları toplayın
        gogus_koordinatlari = []
        kalp_koordinatlari = []
        for satir in icerik:
            satir = satir.strip().split(" ")
            if satir[0].isdigit():
                if int(satir[0]) == 0:
                    gogus_koordinatlari = [float(x) for x in satir[1:]]
                elif int(satir[0]) == 1:
                    kalp_koordinatlari = [float(x) for x in satir[1:]]
        
        # Göğüs eni / kalp eni oranını hesaplayın
        if len(gogus_koordinatlari) > 0 and len(kalp_koordinatlari) > 0:
            oran = gogus_koordinatlari[2] / kalp_koordinatlari[2]
        
            # Kardiyomegali tanısı koyun veya koymayın
            if oran < 1.993:
                print(dosya, "Kardiyomegali tanısı koyuldu.", oran)
                with open(os.path.join(dosya_yolu, "kardiyomegali_hastalari.txt"), "a") as f:
                    f.write(dosya + "\n")
            else:
                print(dosya, "Kardiyomegali tanısı koyulmadı.")
