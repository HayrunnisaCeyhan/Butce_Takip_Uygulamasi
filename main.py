from models import Islem

Islem.verileri_yukle()

print("Bütçe Takip Uygulamasına hoş geldiniz.\n")

def menu():
    print("--------------------------------")
    print("|*********    MENÜ    *********|")
    print("|------------------------------|")
    print("|1.Yeni İşlem Ekle             |")
    print("|2.İşlem Sil                   |")
    print("|3.İşlemleri Listele           |")
    print("|4.Durum Özeti                 |")
    print("|5.Kategoriye göre durum özeti |")
    print("|6.Kategoriye göre Listele     |")
    print("|7.Dosyaya Kaydet              |")
    print("|8.Bütçe Limiti Belirle        |")
    print("|9.Harcama Grafiği Oluştur     |")
    print("|10.Çıkış                      |")
    print("-------------------------------- \n")
 
    

while True :
    menu()
    try:
        secim= int(input("Yapmak istediğiniz işlemi seçiniz:"))
        if secim == 1:
            Islem.yeni_islem()
            Islem.dosyaya_kaydet()
        elif secim == 2:
            Islem.islem_sil()
            Islem.dosyaya_kaydet()
        elif secim == 3:
            Islem.islem_listele()
        elif secim == 4:
            Islem.durum_ozeti()
        elif secim == 5:
            Islem.kategoriye_gore()
        elif secim == 6:
            Islem.kategoriye_gore_listele()
        elif secim == 7:
            Islem.dosyaya_kaydet()
        elif secim == 8:
            Islem.limit_belirle()
        elif secim == 9:
            Islem.harcama_grafigi_goster()
        elif secim == 10:
            print("Çıkış yapılıyor...")
            break
        else:
            print("Lütfen 1 ile 10 arasında değer giriniz!")
    except ValueError:
        print("Hata: Sadece sayısal değer girişi yapınız!")
        

