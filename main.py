import os
import shutil

def dosyalari_duzenle():
    # Çalışılan dizini al
    klasor_yolu = os.getcwd()
    
    # Taşınacak klasör adı
    hedef_klasor = "Resimler"
    
    # Klasör yoksa oluştur
    if not os.path.exists(os.path.join(klasor_yolu, hedef_klasor)):
        os.makedirs(os.path.join(klasor_yolu, hedef_klasor))
        print(f"'{hedef_klasor}' klasörü oluşturuldu.")

    # Dosyaları tara
    for dosya in os.listdir(klasor_yolu):
        # Sadece resim dosyalarını seç
        if dosya.endswith(".png") or dosya.endswith(".jpg"):
            kaynak = os.path.join(klasor_yolu, dosya)
            hedef = os.path.join(klasor_yolu, hedef_klasor, dosya)
            
            shutil.move(kaynak, hedef)
            print(f"{dosya} taşındı -> {hedef_klasor}")

if __name__ == "__main__":
    dosyalari_duzenle()