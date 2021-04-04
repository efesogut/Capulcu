import time
import os

def bekle(a):
    time.sleep(a)

def temizle():
    os.system('cls' if os.name == 'nt' else 'clear')

ab = 1.4
gb = 3.2

Vites = "Boşta"
Durum = "Duruyor"
Vitesler = ["Geri","Boşta","1","2","3","4","5"]

temizle()
print("Anahtar Kontağa takılsın mı? (E/H):", end=" ")
if "E" == input():
    print("")
    print("Mobilizer anahtarı tanıyor")
    bekle(ab)
    print("Anahtar doğrulandı")
    bekle(gb)
else:
    print("")
    bekle(ab)
    print("Araba çalısmadı")
    bekle(gb)
    exit()

temizle()
print("Anahtar ilk kademeye çevirilsin mi? (E/H):", end=" ")
if "E" == input():
    print("")
    bekle(ab)
    print("Aküden Beyin Dışındaki Aksanlara Güç Gitti")
    bekle(2)
else:
    print("")
    bekle(ab)
    print("Araba çalışmadı:)")
    bekle(gb)
    exit()

temizle()
print("Anahtar ikinci kademeye çevirilsin mi? (E/H):", end=" ")
if "E" == input():
    print("")
    bekle(ab)
    print("Araba Beynine Elektrik Gitti")
    bekle(ab)
    print("Kontrol Kutusuna Elektrik Gitti")
    bekle(gb)
else:
    print("")
    bekle(ab)
    print("Araba Çalışmadı Ama Elektrik Var Teypten Müzik Dineleyebilirsiniz :)")
    bekle(gb)
    exit()

temizle()
print("Anahtar üçüncü kademeye çevrilsin mi? (E/H):", end=" ")
if "E" == input():
    print("")
    bekle(ab)
    print("Marş Motoru Devreye Girdi")
    bekle(ab)
    print("Motora Benzin Ve Hava Girişi Sağlandı")
    bekle(ab)
    print("Marş Motoru Motora İlk Hareketi Verdi")
    bekle(ab)
    print("MOTOR ÇALIŞTI!")
    bekle(gb)
else:
    print("")
    bekle(ab)
    print("Araba Çalışmadı Ama Beyinde Ve Temel Aksanlardaa Elektrik Var")
    bekle(gb)

temizle()
while True:
    print("---------------------------------------------------")
    print("              ARABA  KONTROL MENUSU                ")
    print("---------------------------------------------------")
    print("Araç Durumu: {}" .format(Durum))
    print("Vites Durumu: {}" .format(Vites))
    print("")
    print("Araba Çalışıyor Ne Yapmak İstersin:")
    print("1) Gaza Bas")
    print("2) Vites Değiştir")
    print("3) Frene Bas")
    print("4) Arabadan İn")
    print("")
    secim = input("Seçiniz: ")
    if "1" == secim:
        temizle()
        print("---------------------------------------------------")
        print("                  GAZA BASILDI                     ")
        print("---------------------------------------------------")
        print("")
        print("Motora Giden Hava Ve Benzin arttırıldı")
        bekle(ab)
        print("Yanma Odasındaki Patlamalar Arttı")
        bekle(ab)
        print("Pistonlar İleri Geri Hareket Etmeye Başladı")
        bekle(ab)
        print("Pistonlardaki Hareket Krank Miline Aktarıldı")
        bekle(ab)
        print("Krank Milindeki Hareket Difaransiyel Tarafından Tekreleklere Aktarıldı")
        bekle(ab)
        if Vites == "Boşta":
            print("Vites Boşta Olduğundan Dolayı Araba İlerlemiyecek")
        elif Vites == "Geri":
            print("Vites Geride Araba Geriye Doğru Gidiyor")
        else:
            print("Araba ilerlemeye Başladı")
            Durum = "İlerliyor"
        bekle(gb)
        temizle()
    elif "2" == secim:
        temizle()
        print("---------------------------------------------------")
        print("              VİTES DEĞİŞTİRİLİYOR                 ")
        print("---------------------------------------------------")
        print("Vites Durumu: {}" .format(Vites))
        
        if Vites == "Boşta":
            vs = input("Vites Seçimi (Arttır/Geri): ")
        elif Vites == "5":
            vs = input("Vites Seçimi (Azalt/Geri/Boş): ")
        elif Vites == "Geri":
            vs = input("Vites Seçimi (Arttır/Azalt/Boş): ")
        else:
            vs = input("Vites Seçimi (Arttır/Azalt/Geri/Boş): ")
        
        if vs == "Arttır":
            if Vites == 5:
                print("")
                print("Vites Daha Fazla Arttırılamaz")
                bekle(gb)
                temizle()
            elif Vites == "Boşta":
                print("")
                bekle(ab)
                if Durum == "İlerliyor":
                    print("Gaz Pedalı Bırakılıyor")
                else:
                    pass
                bekle(ab)
                print("Debriyaja Basılıyor")
                bekle(ab)
                print("Motor İle Şanzıman Ayrılıyor")
                bekle(ab)
                print("Şanzımandaki Vites Dişlileri Yer Değiştiriyor")
                bekle(ab)
                print("Vites Boşta olduğundan 1 e Alınıyor")
                bekle(ab)
                print("Şanzıman ile Motor Yeniden Birleşiyor")
                Vites = 1
                bekle(gb)
                temizle()
            elif Vites == "Geri":
                print("")
                bekle(ab)
                if Durum == "İlerliyor":
                    print("Gaz Pedalı Bırakılıyor")
                else:
                    pass
                bekle(ab)
                print("Debriyaja Basılıyor")
                bekle(ab)
                print("Motor İle Şanzıman Ayrılıyor")
                bekle(ab)
                print("Şanzımandaki Vites Dişlileri Yer Değiştiriyor")
                bekle(ab)
                print("Vites Geride olduğundan 1 e Alınıyor")
                bekle(ab)
                print("Şanzıman ile Motor Yeniden Birleşiyor")
                Vites = 1
                bekle(gb)
                temizle()
            else:
                print("")
                bekle(ab)
                if Durum == "İlerliyor":
                    print("Gaz Pedalı Bırakılıyor")
                else:
                    pass
                bekle(ab)
                print("Debriyaja Basılıyor")
                bekle(ab)
                print("Motor İle Şanzıman Ayrılıyor")
                bekle(ab)
                print("Şanzımandaki Vites Dişlileri Yer Değiştiriyor")
                bekle(ab)
                print("Vites Arttırılıyor")
                bekle(ab)
                print("Şanzıman ile Motor Yeniden Birleşiyor")
                Vites = Vites + 1
                bekle(gb)
                temizle()
        elif vs == "Azalt":
            if Vites == "Boşta":
                print("")
                bekle(ab)
                if Durum == "İlerliyor":
                    print("Gaz Pedalı Bırakılıyor")
                else:
                    pass
                bekle(ab)
                print("Debriyaja Basılıyor")
                bekle(ab)
                print("Motor İle Şanzıman Ayrılıyor")
                bekle(ab)
                print("Şanzımandaki Vites Dişlileri Yer Değiştiriyor")
                bekle(ab)
                print("Vites Boşta olduğundan 1 e Alınıyor")
                bekle(ab)
                print("Şanzıman ile Motor Yeniden Birleşiyor")
                Vites = 1
                bekle(gb)
                temizle()
            elif Vites == "Geri":
                print("")
                bekle(ab)
                if Durum == "İlerliyor":
                    print("Gaz Pedalı Bırakılıyor")
                else:
                    pass
                bekle(ab)
                print("Debriyaja Basılıyor")
                bekle(ab)
                print("Motor İle Şanzıman Ayrılıyor")
                bekle(ab)
                print("Şanzımandaki Vites Dişlileri Yer Değiştiriyor")
                bekle(ab)
                print("Vites Geride olduğundan 1 e Alınıyor")
                bekle(ab)
                print("Şanzıman ile Motor Yeniden Birleşiyor")
                Vites = 1
                bekle(gb)
                temizle()
            elif Vites == 1:
                print("")
                bekle(ab)
                if Durum == "İlerliyor":
                    print("Gaz Pedalı Bırakılıyor")
                else:
                    pass
                bekle(ab)
                print("Vites Daha Fazla Azaltılamaz")
                bekle(gb)
                temizle()
            else:
                print("")
                bekle(ab)
                if Durum == "İlerliyor":
                    print("Gaz Pedalı Bırakılıyor")
                else:
                    pass
                bekle(ab)
                print("Debriyaja Basılıyor")
                bekle(ab)
                print("Motor İle Şanzıman Ayrılıyor")
                bekle(ab)
                print("Şanzımandaki Vites Dişlileri Yer Değiştiriyor")
                bekle(ab)
                print("Vites Azaltılıyor")
                bekle(ab)
                print("Şanzıman ile Motor Yeniden Birleşiyor")
                Vites = Vites - 1
                bekle(gb)
                temizle()
        elif vs == "Boş":
            print("")
            bekle(ab)
            if Durum == "İlerliyor":
                    print("Gaz Pedalı Bırakılıyor")
            else:
                pass
            bekle(ab)
            print("Debriyaja Basılıyor")
            bekle(ab)
            print("Motor İle Şanzıman Ayrılıyor")
            bekle(ab)
            print("Şanzımandaki Vites Dişlileri Yer Değiştiriyor")
            bekle(ab)
            print("Vites Boşa Alınıyor")
            bekle(ab)
            print("Şanzıman ile Motor Yeniden Birleşiyor")
            Vites = "Boş"
            bekle(gb)
            temizle()
        elif vs == "Geri":
            print("")
            bekle(ab)
            if Durum == "İlerliyor":
                    print("Gaz Pedalı Bırakılıyor")
            else:
                pass
            bekle(ab)
            print("Debriyaja Basılıyor")
            bekle(ab)
            print("Motor İle Şanzıman Ayrılıyor")
            bekle(ab)
            print("Şanzımandaki Vites Dişlileri Yer Değiştiriyor")
            bekle(ab)
            print("Vites Geriye Alınıyor")
            bekle(ab)
            print("Şanzıman ile Motor Yeniden Birleşiyor")
            Vites = "Geri"
            bekle(gb)
            temizle()
        else:
            pass
    elif "3" == secim:
        temizle()
        print("---------------------------------------------------")
        print("                   FRENE BASILDI                   ")
        print("---------------------------------------------------")
        print("")
        bekle(ab)
        if Durum == "İlerliyor":
            print("Gaz Pedalı Bırakılıyor")
        else:
            pass
        bekle(ab)
        print("Fren Pedalına Basılıyor")
        bekle(ab)
        print("Fren Pedalına Yapılan Baskı Westinghouse A İletildi")
        bekle(ab)
        print("Westinghouse A İletilen Hidrolik Basınç Arttırılarak Fren Kutusuna İletildi")
        bekle(ab)
        print("Fren Kutusuna Gelen Hidrolik Basınç 4'e Bölünüp Tekerleklere İletildi")
        bekle(ab)
        print("Tekerleklere Ulaşan Hidrolik Basınç Balataları Sıkarak Fren Disklerine Sürtünme Uyguladı")
        bekle(ab)
        print("Sürtünme Uygulanan Fren Diskleri Tekerlekleri Yavaşlatarak Durdurdu")
        Durum = "Duruyor"
        bekle(gb+4)
        temizle()
    elif "4" == secim:
        temizle()
        print("---------------------------------------------------")
        print("                ARABADAN İNİLDİ                    ")
        print("---------------------------------------------------")
        print("")
        bekle(ab)
        print("Arabadan inildi")
        bekle(ab)
        print("Yolun Ortasında İndiğiniz İçin Ceza Yediniz H.O.")
        bekle(gb)
        exit()
    else:
        temizle()