# -*- coding: utf-8 -*-
"""
PYTHON'DA LİSTE KULLANIMI VE LİSTE METOTLARI
=============================================
Liste (list): Birden fazla değeri tek bir değişkende, SIRALI şekilde tutan,
DEĞİŞTİRİLEBİLİR (mutable) veri yapısıdır. Köşeli parantez [] ile yazılır.

- Elemanlar sıralıdır, her elemanın bir indeksi vardır (0'dan başlar).
- Farklı veri tiplerini bir arada tutabilir.
- Aynı değer birden fazla kez bulunabilir.

Bu dosyayı çalıştırmak için:  python python_liste_ornekleri.py
"""


def baslik(metin):
    print("\n" + "=" * 60)
    print(metin)
    print("=" * 60)


# ============================================================
# BÖLÜM 1: TEMEL LİSTE KULLANIMI
# ============================================================

baslik("1. LİSTE OLUŞTURMA")

# Örnek 1: Farklı yollarla liste oluşturma
bos_liste = []
bos_liste2 = list()
sayilar = [10, 20, 30, 40, 50]
karisik = ["Ali", 25, 3.14, True]
harfler = list("PYTHON")          # String'den liste
aralik = list(range(1, 6))        # range'den liste
print("Boş liste      :", bos_liste, bos_liste2)
print("Sayılar        :", sayilar)
print("Karışık tipler :", karisik)
print("Harfler        :", harfler)
print("range ile      :", aralik)

# Örnek 2: İç içe liste (matris)
matris = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
print("Matris         :", matris)
print("2. satır 3. sütun:", matris[1][2])   # 6


baslik("2. İNDEKSLEME (ELEMANA ERİŞİM)")

meyveler = ["elma", "armut", "muz", "kiraz", "çilek"]
#  indeks:     0        1       2       3        4
#  negatif:   -5       -4      -3      -2       -1

# Örnek 1: Pozitif indeks
print("İlk eleman     :", meyveler[0])
print("Üçüncü eleman  :", meyveler[2])

# Örnek 2: Negatif indeks (sondan sayma)
print("Son eleman     :", meyveler[-1])
print("Sondan ikinci  :", meyveler[-2])


baslik("3. DİLİMLEME (SLICING)  ->  liste[başlangıç:bitiş:adım]")

sayilar = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Örnek 1: Temel dilimleme (bitiş indeksi DAHİL DEĞİLDİR)
print("[2:5]   :", sayilar[2:5])     # [2, 3, 4]
print("[:4]    :", sayilar[:4])      # baştan 4. indekse kadar
print("[6:]    :", sayilar[6:])      # 6. indeksten sona kadar

# Örnek 2: Adımlı ve ters dilimleme
print("[::2]   :", sayilar[::2])     # çift indeksler
print("[1::2]  :", sayilar[1::2])    # tek indeksler
print("[::-1]  :", sayilar[::-1])    # listeyi ters çevirir (yeni liste)


baslik("4. ELEMAN DEĞİŞTİRME")

# Örnek 1: Tek eleman değiştirme
renkler = ["kırmızı", "yeşil", "mavi"]
renkler[1] = "sarı"
print("Tek eleman     :", renkler)

# Örnek 2: Dilim ile birden fazla eleman değiştirme
notlar = [50, 60, 70, 80, 90]
notlar[1:3] = [65, 75]
print("Dilimle        :", notlar)


baslik("5. TEMEL FONKSİYONLAR VE OPERATÖRLER")

# Örnek 1: len, sum, min, max
puanlar = [85, 92, 78, 95, 60]
print("Eleman sayısı  :", len(puanlar))
print("Toplam         :", sum(puanlar))
print("En küçük       :", min(puanlar))
print("En büyük       :", max(puanlar))
print("Ortalama       :", sum(puanlar) / len(puanlar))

# Örnek 2: in / not in, + ve * operatörleri
sepet = ["ekmek", "süt", "yumurta"]
print("'süt' var mı?  :", "süt" in sepet)
print("'çay' yok mu?  :", "çay" not in sepet)
print("Birleştirme +  :", [1, 2] + [3, 4])
print("Tekrarlama *   :", ["-"] * 5)


baslik("6. LİSTE ÜZERİNDE DÖNGÜ")

# Örnek 1: for ile elemanları gezme
sehirler = ["İstanbul", "Ankara", "İzmir"]
for sehir in sehirler:
    print("Şehir:", sehir)

# Örnek 2: enumerate ile indeks + eleman
for sira, sehir in enumerate(sehirler, start=1):
    print(f"{sira}. {sehir}")


baslik("7. LIST COMPREHENSION (TEK SATIRDA LİSTE ÜRETME)")

# Örnek 1: 1-10 arası sayıların kareleri
kareler = [x ** 2 for x in range(1, 11)]
print("Kareler        :", kareler)

# Örnek 2: Koşullu comprehension - sadece çift sayılar
ciftler = [x for x in range(1, 21) if x % 2 == 0]
print("Çift sayılar   :", ciftler)


# ============================================================
# BÖLÜM 2: LİSTE METOTLARI
# ============================================================
# Python listelerinin 11 metodu vardır:
# append, extend, insert, remove, pop, clear,
# index, count, sort, reverse, copy

baslik("METOT 1: append()  ->  Listenin SONUNA tek bir eleman ekler")

# Örnek 1: Alışveriş listesine ürün ekleme
alisveris = ["ekmek", "süt"]
alisveris.append("peynir")
alisveris.append("zeytin")
print("Alışveriş      :", alisveris)

# Örnek 2: Kullanıcıdan alınan notları döngüyle listeye ekleme (simülasyon)
gelen_notlar = [70, 85, 90]
not_listesi = []
for n in gelen_notlar:
    not_listesi.append(n)
print("Not listesi    :", not_listesi)

# Örnek 3 (DİKKAT): append listeyi TEK eleman olarak ekler
a = [1, 2, 3]
a.append([4, 5])
print("append([4,5])  :", a, "-> eleman sayısı:", len(a))   # [1, 2, 3, [4, 5]]


baslik("METOT 2: extend()  ->  Başka bir yinelenebilirin TÜM elemanlarını sona ekler")

# Örnek 1: İki listeyi birleştirme
sinif_a = ["Ayşe", "Mehmet"]
sinif_b = ["Zeynep", "Can"]
sinif_a.extend(sinif_b)
print("Birleşik sınıf :", sinif_a)

# Örnek 2: append ile farkı
x = [1, 2, 3]
x.extend([4, 5])
print("extend([4,5])  :", x, "-> eleman sayısı:", len(x))   # [1, 2, 3, 4, 5]

# Örnek 3: String, tuple, range ile extend
harf_listesi = ["a"]
harf_listesi.extend("bc")          # string karakterlerine ayrılır
harf_listesi.extend(("d", "e"))    # tuple
print("String+tuple   :", harf_listesi)


baslik("METOT 3: insert(indeks, eleman)  ->  Belirtilen konuma eleman ekler")

# Örnek 1: Sıra listesinin başına ekleme
kuyruk = ["Ali", "Veli", "Ayşe"]
kuyruk.insert(0, "Yaşlı Teyze")    # öncelikli
print("Başa ekleme    :", kuyruk)

# Örnek 2: Araya ekleme
gunler = ["Pazartesi", "Çarşamba", "Perşembe"]
gunler.insert(1, "Salı")
print("Araya ekleme   :", gunler)

# Örnek 3: Liste uzunluğundan büyük indeks -> sona ekler (hata vermez)
k = [1, 2, 3]
k.insert(100, 99)
print("insert(100,99) :", k)


baslik("METOT 4: remove(değer)  ->  Değeri verilen İLK elemanı siler")

# Örnek 1: Değere göre silme
hayvanlar = ["kedi", "köpek", "kuş", "balık"]
hayvanlar.remove("kuş")
print("kuş silindi    :", hayvanlar)

# Örnek 2: Sadece İLK eşleşme silinir
tekrarli = [1, 2, 3, 2, 4, 2]
tekrarli.remove(2)
print("İlk 2 silindi  :", tekrarli)    # [1, 3, 2, 4, 2]

# Örnek 3: Olmayan eleman -> ValueError. Güvenli silme:
urunler = ["kalem", "silgi"]
silinecek = "defter"
if silinecek in urunler:
    urunler.remove(silinecek)
else:
    print(f"'{silinecek}' listede yok, silinemedi.")

# Örnek 4: Tüm tekrarları silmek için
liste = [1, 2, 3, 2, 4, 2]
while 2 in liste:
    liste.remove(2)
print("Tüm 2'ler silindi:", liste)


baslik("METOT 5: pop(indeks)  ->  Elemanı siler ve SİLİNEN elemanı döndürür")

# Örnek 1: İndeks vermeden -> son elemanı siler
yigin = ["kitap1", "kitap2", "kitap3"]
ust = yigin.pop()
print("Alınan         :", ust)
print("Kalan yığın    :", yigin)

# Örnek 2: İndeks vererek silme
ogrenciler = ["Ali", "Buse", "Cem", "Derya"]
cikan = ogrenciler.pop(1)
print("Sınıftan çıkan :", cikan)
print("Kalanlar       :", ogrenciler)

# Örnek 3: Yığın (stack - LIFO) uygulaması
gecmis = []
gecmis.append("sayfa1")
gecmis.append("sayfa2")
gecmis.append("sayfa3")
print("Geri tuşu      :", gecmis.pop(), "-> şimdi:", gecmis[-1])


baslik("METOT 6: clear()  ->  Listenin TÜM elemanlarını siler (liste boş kalır)")

# Örnek 1: Sepeti boşaltma
sepet = ["elma", "armut", "muz"]
sepet.clear()
print("Boşaltılmış sepet:", sepet, "| uzunluk:", len(sepet))

# Örnek 2: Günlük kayıtları her gün sıfırlama
gunluk_log = ["giriş", "işlem", "çıkış"]
print("Gün sonu log   :", gunluk_log)
gunluk_log.clear()
gunluk_log.append("yeni gün başladı")
print("Yeni gün log   :", gunluk_log)


baslik("METOT 7: index(değer, başlangıç, bitiş)  ->  Değerin İLK indeksini döndürür")

# Örnek 1: Elemanın konumunu bulma
gezegenler = ["Merkür", "Venüs", "Dünya", "Mars"]
print("Dünya'nın indeksi:", gezegenler.index("Dünya"))

# Örnek 2: Başlangıç parametresi ile sonraki tekrarı bulma
sayilar = [5, 3, 7, 3, 9, 3]
ilk = sayilar.index(3)
ikinci = sayilar.index(3, ilk + 1)
print("İlk 3          :", ilk)
print("İkinci 3       :", ikinci)

# Örnek 3: Olmayan değer -> ValueError, try-except ile yakalama
try:
    gezegenler.index("Pluto")
except ValueError:
    print("Pluto listede bulunamadı.")


baslik("METOT 8: count(değer)  ->  Değerin listede kaç kez geçtiğini döndürür")

# Örnek 1: Oy sayma
oylar = ["A", "B", "A", "C", "A", "B"]
print("A aldı         :", oylar.count("A"))
print("B aldı         :", oylar.count("B"))
print("D aldı         :", oylar.count("D"))   # yoksa 0 döner, hata vermez

# Örnek 2: Zar atışlarında 6 sayısı
zarlar = [6, 2, 6, 4, 1, 6, 3]
print("6 gelme sayısı :", zarlar.count(6))

# Örnek 3: Tekrar eden elemanları bulma
liste = [1, 2, 2, 3, 3, 3]
tekrar_edenler = [x for x in set(liste) if liste.count(x) > 1]
print("Tekrar edenler :", sorted(tekrar_edenler))


baslik("METOT 9: sort(key=None, reverse=False)  ->  Listeyi YERİNDE sıralar")

# Örnek 1: Küçükten büyüğe ve büyükten küçüğe
notlar = [72, 95, 58, 81, 66]
notlar.sort()
print("Artan          :", notlar)
notlar.sort(reverse=True)
print("Azalan         :", notlar)

# Örnek 2: Alfabetik sıralama ve uzunluğa göre sıralama (key)
isimler = ["Zeynep", "Ali", "Mehmet", "Can"]
isimler.sort()
print("Alfabetik      :", isimler)
isimler.sort(key=len)
print("Uzunluğa göre  :", isimler)

# Örnek 3: İç içe listeyi belirli bir sütuna göre sıralama
ogrenci_notlari = [["Ali", 75], ["Buse", 92], ["Cem", 60]]
ogrenci_notlari.sort(key=lambda o: o[1], reverse=True)
print("Nota göre      :", ogrenci_notlari)

# DİKKAT: sort() None döndürür, orijinal listeyi değiştirir.
# Orijinali korumak istiyorsan sorted() fonksiyonunu kullan:
orijinal = [3, 1, 2]
yeni = sorted(orijinal)
print("sorted()       :", yeni, "| orijinal:", orijinal)


baslik("METOT 10: reverse()  ->  Listeyi YERİNDE ters çevirir")

# Örnek 1: Basit ters çevirme
sayilar = [1, 2, 3, 4, 5]
sayilar.reverse()
print("Ters           :", sayilar)

# Örnek 2: En son eklenenden eskiye doğru gösterme
mesajlar = ["Merhaba", "Nasılsın?", "Görüşürüz"]
mesajlar.reverse()
print("Yeniden eskiye :", mesajlar)

# Not: reverse() sıralama YAPMAZ, sadece mevcut sırayı tersine çevirir.
k = [3, 1, 2]
k.reverse()
print("[3,1,2] ters   :", k)    # [2, 1, 3]


baslik("METOT 11: copy()  ->  Listenin YÜZEYSEL (shallow) kopyasını döndürür")

# Örnek 1: Atama (=) ile copy() farkı
orijinal = [1, 2, 3]
ayni = orijinal            # kopya DEĞİL, aynı listeyi gösterir
kopya = orijinal.copy()    # bağımsız yeni liste
orijinal.append(4)
print("Orijinal       :", orijinal)
print("= ile atanan   :", ayni)     # o da değişti!
print("copy() ile     :", kopya)    # değişmedi

# Örnek 2: Orijinali bozmadan kopya üzerinde işlem
fiyatlar = [100, 200, 300]
indirimli = fiyatlar.copy()
for i in range(len(indirimli)):
    indirimli[i] = indirimli[i] * 0.9
print("Normal fiyat   :", fiyatlar)
print("İndirimli      :", indirimli)

# Örnek 3 (DİKKAT): İç içe listelerde copy() yetmez -> deepcopy
import copy
ic_ice = [[1, 2], [3, 4]]
yuzeysel = ic_ice.copy()
derin = copy.deepcopy(ic_ice)
ic_ice[0][0] = 99
print("Yüzeysel kopya :", yuzeysel)   # [[99, 2], [3, 4]] -> etkilendi
print("Derin kopya    :", derin)      # [[1, 2], [3, 4]]  -> etkilenmedi


# ============================================================
# BÖLÜM 3: TÜM METOTLARI BİRLEŞTİREN UYGULAMA
# ============================================================

baslik("UYGULAMA: Sınıf Not Yönetim Sistemi")

notlar = []
notlar.append(78)                      # append
notlar.extend([92, 65, 88, 45, 92])    # extend
notlar.insert(0, 100)                  # insert
print("Tüm notlar     :", notlar)

notlar.remove(45)                      # remove (kalan öğrenci)
print("45 silindi     :", notlar)

son_not = notlar.pop()                 # pop
print("Son eklenen not geri alındı:", son_not)

print("92 alan sayısı :", notlar.count(92))       # count
print("88'in sırası   :", notlar.index(88))       # index

yedek = notlar.copy()                  # copy
notlar.sort(reverse=True)              # sort
print("Büyükten küçüğe:", notlar)

notlar.reverse()                       # reverse
print("Küçükten büyüğe:", notlar)
print("Yedek (sırasız):", yedek)

ortalama = sum(notlar) / len(notlar)
gecenler = [n for n in notlar if n >= 50]
print(f"Ortalama       : {ortalama:.2f}")
print("Geçenler       :", gecenler)

notlar.clear()                         # clear
print("Dönem sonu     :", notlar)


# ============================================================
# ÖZET TABLO
# ============================================================
baslik("ÖZET: LİSTE METOTLARI")
ozet = [
    ("append(x)",        "Sona tek eleman ekler",               "None"),
    ("extend(iter)",     "Sona birden çok eleman ekler",        "None"),
    ("insert(i, x)",     "i konumuna eleman ekler",             "None"),
    ("remove(x)",        "x değerinin ilkini siler",            "None"),
    ("pop(i)",           "i konumundakini siler (vars. son)",   "Silinen eleman"),
    ("clear()",          "Tüm elemanları siler",                "None"),
    ("index(x)",         "x'in ilk indeksini bulur",            "int"),
    ("count(x)",         "x'in kaç kez geçtiğini sayar",        "int"),
    ("sort()",           "Yerinde sıralar",                     "None"),
    ("reverse()",        "Yerinde ters çevirir",                "None"),
    ("copy()",           "Yüzeysel kopya oluşturur",            "Yeni liste"),
]
print(f"{'Metot':<16}{'Görevi':<38}{'Döndürdüğü'}")
print("-" * 70)
for metot, gorev, donus in ozet:
    print(f"{metot:<16}{gorev:<38}{donus}")
