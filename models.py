import csv
import os 
import matplotlib.pyplot as plt

islem_list = []
limitler = {}

class Islem:
    def __init__(self,tarih,ad,tur,kategori,fiyat):
        self.tarih=tarih
        self.ad=ad
        self.tur= tur
        self.kategori= kategori
        self.fiyat = fiyat
    
    @staticmethod
    def kategori_secimi():
        print("Kategoriler")
        print("-----------------------------")
        print("1.Mutfak")
        print("2.Alışveriş")
        print("3.Kira")
        print("4.Eğlence")
        print("5.Maaş")
        print("6.Diğer")

        kategori_secim=int(input("Kategori seçiminizi yapınız:"))
        if kategori_secim == 1:
            kategori = "Mutfak"
        elif kategori_secim == 2:
            kategori = "Alışveris"
        elif kategori_secim == 3:
            kategori = "Kira"
        elif kategori_secim == 4:
            kategori = "Eğlence"
        elif kategori_secim == 5:
            kategori = "Maaş"
        elif kategori_secim == 6:
            kategori ="Diğer"
        else:
            print("Geçersiz seçim yaptınız")
            return
        return kategori
    
    def yeni_islem():
        tarih=input("Tarih (GG-AA-YYYY):")
        ad=input("İşlem Adı:")
        tur=input("Tür(Gelir,Gider):").capitalize()
        kategori = Islem.kategori_secimi()
        
        try:
             fiyat = input("Fiyat:")
             fiyat = float(fiyat.replace("," , "."))
        except ValueError:
            print("[!] HATA: Fiyat kısmına sadece sayı girmelisiniz.")
            return
        
        new=Islem(tarih,ad,tur,kategori,fiyat)
        islem_list.append(new)
        print("İşlem başarıyla eklendi.")
        print(f"İşlem: {tarih}, {ad}, {tur}, {kategori},{fiyat}")
        print(" ")     

        if tur == "Gider":
            Islem.limit_kontrol(kategori)   
    
    def islem_sil():
        islem_adi=input("Silmek istediğiniz işlemin adını giriniz:")

        bulunan_islem= None
        for i in islem_list:
            if i.ad == islem_adi:
                bulunan_islem= i
                break
        if bulunan_islem:
            islem_list.remove(bulunan_islem)
            print(f"{bulunan_islem.ad} işlem listesinden kaldırıldı.")

    def islem_listele():
        print("İŞLEM LİSTESİ")
        print("-------------")
        for i in islem_list:
            print(f"İşlem Adı:{i.ad}, Tarihi:{i.tarih}, Türü:{i.tur}, Kategori:{i.kategori}, Fiyat:{i.fiyat}")
    
    def durum_ozeti():
        print("Durum Özeti")
        print("-----------")
        toplam_gelir = 0
        toplam_gider = 0
        if not islem_list :
            print("Herhangi bir işlem girişi yapılmadı.")
        
        for i in islem_list:
            if i.tur == "Gelir":
                toplam_gelir += i.fiyat
            elif i.tur == "Gider":
                toplam_gider += i.fiyat
            
        print(f"Toplam Gelir: {toplam_gelir}")
        print(f"Toplam Gider: {toplam_gider}")


    def kategoriye_gore():
        istenen_kategori = input("Kategori seçiminizi yazınız:").capitalize()
        kategori_toplam_gelir = sum(i.fiyat for i in islem_list if i.kategori == istenen_kategori and i.tur == "Gelir")
        kategori_toplam_gider = sum(i.fiyat for i in islem_list if i.kategori == istenen_kategori and i.tur == "Gider")        
        print(f"Kategori: {istenen_kategori}")
        print("------------------------------")
        print(f"- Toplam Gelir: {kategori_toplam_gelir} ")
        print(f"- Toplam Gider: {kategori_toplam_gider} \n")
        
    def dosyaya_kaydet():
       # 'w' modu dosyayı her seferinde sıfırdan yazar (güncel listeyi kaydetmek için idealdir)
        with open("butce_verileri.csv", "w", encoding="utf-8", newline='') as dosya:
            yazici = csv.writer(dosya)
            # Sütun başlıklarını yazalım
            yazici.writerow(["Tarih", "Ad", "Tür", "Kategori", "Fiyat"])
        
        # Listedeki her nesneyi satır satır yazalım
            for i in islem_list:
                yazici.writerow([i.tarih, i.ad, i.tur, i.kategori, i.fiyat])
    print("\n[!] Veriler 'butce_verileri.csv' dosyasına kaydedildi.")
    
    def verileri_yukle():
           # Dosya var mı kontrol edelim, yoksa okumaya çalışmak hata verir
        if os.path.exists("butce_verileri.csv"):
            with open("butce_verileri.csv", "r", encoding="utf-8") as dosya:
                okuyucu = csv.reader(dosya)
                next(okuyucu)  # Başlık satırını (Tarih, Ad...) atla
            
                for satir in okuyucu:
                    # CSV'den gelen her satır bir listedir: [tarih, ad, tur, kategori, miktar]
                    # Bu verilerle yeni bir nesne oluşturup listeye ekliyoruz
                    yeni = Islem(
                        tarih= satir[0],
                        ad= satir[1],
                        tur= satir[2],
                        kategori= satir[3],
                        fiyat= float(satir[4]) 
                    )
                    islem_list.append(yeni)
            print(f"\n[v] {len(islem_list)} eski kayıt başarıyla yüklendi.")
        else:
            print("\n[!] Henüz kayıtlı veri bulunamadı, temiz bir liste ile başlanıyor.")
    
    def kategoriye_gore_listele():
    
        hedef_kategori = Islem.kategori_secimi() # Daha önce yazdığın seçim fonksiyonunu kullanıyoruz
      
        print(f"\n--- {hedef_kategori} Kategorisindeki İşlemler ---")
        print(f"{'TARİH':<15} | {'İŞLEM ADI':<15} | {'TÜR':<10} | {'MİKTAR'}")
        print("-" * 55)

        sayac = 0
        toplam = 0

        for i in islem_list:
            if hedef_kategori == i.kategori:
                print(f"{i.tarih:<15} | {i.ad:<15} | {i.tur:<10} | {i.fiyat:.2f} TL")
                sayac +=1
            
            if sayac == 0:
                print("Kategoriye ait veri bulunamadı.")
            else:
                print("-"*55)
                print(f"Toplam {sayac} işlem bulundu. Kategori Toplamı: {toplam:.2f} TL")
    
    def limit_belirle():
        kategori = Islem.kategori_secimi()
        try:
            limit = float(input(f"{kategori} Kategorisi için limiti giriniz:"))
            limitler[kategori] = limit
            print(f"Başarılı! {kategori} limiti {limit} TL olarak güncellendi.")
        except ValueError:
            print("Hata: Lütfen geçerli bir sayı girin.")
    
    def limit_kontrol(kategori):
        if kategori in limitler:
            toplam_harcama =sum(i.fiyat for i in islem_list if i.kategori == kategori and i.tur == "Gider")
            limit =limitler[kategori]

            yuzde = (toplam_harcama / limit) * 100

            if yuzde>=100:
                print(f"!!! KRİTİK UYARI: {kategori} limitinizi {toplam_harcama-limit} TL aştınız!")
            elif yuzde>=80:
                print(f"!! DİKKAT: {kategori} bütçenizin %{yuzde:.0f}'ine ulaştınız. Harcamalara dikkat !")

    def harcama_grafigi_goster():
        kategori_toplamlari = {}

        for i in islem_list:
            if i.tur == "Gider":
                if i.kategori not in kategori_toplamlari:
                    kategori_toplamlari[i.kategori] = 0
                kategori_toplamlari[i.kategori] += i.fiyat

        if not kategori_toplamlari:
            print("Grafik oluşturulacak harcama verisi bulunamadı!")
            return
        
        etiketler = list(kategori_toplamlari.keys())
        fiyatlar = list(kategori_toplamlari.values())

        plt.figure(figsize=(8, 6))
        plt.pie(fiyatlar, labels=etiketler, autopct='%1.1f%%', startangle=140, shadow=True)
        plt.title("Kategorilere Göre Harcama Dağılımı")
        plt.axis('equal')
        
        print("Grafik penceresi açılıyor...")
        plt.show()