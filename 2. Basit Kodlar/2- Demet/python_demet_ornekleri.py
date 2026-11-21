# -*- coding: utf-8 -*-
"""
PYTHON'DA DEMET (TUPLE) KULLANIMI VE DEMET METOTLARI
=====================================================
Demet (tuple): Birden fazla değeri tek bir değişkende, SIRALI şekilde tutan,
DEĞİŞTİRİLEMEZ (immutable) veri yapısıdır. Normal parantez () ile yazılır.

- Elemanlar sıralıdır, her elemanın bir indeksi vardır (0'dan başlar).
- Farklı veri tiplerini bir arada tutabilir.
- Aynı değer birden fazla kez bulunabilir.
- Oluşturulduktan sonra eleman EKLENEMEZ, SİLİNEMEZ, DEĞİŞTİRİLEMEZ.

Listeden farkı: Liste [] -> değiştirilebilir | Demet () -> değiştirilemez

Bu dosyayı çalıştırmak için:  python python_demet_ornekleri.py
"""

import sys


def baslik(metin):
    print("\n" + "=" * 60)
    print(metin)
    print("=" * 60)


# ============================================================
# BÖLÜM 1: TEMEL DEMET KULLANIMI
# ============================================================

baslik("1. DEMET OLUŞTURMA")

# Örnek 1: Farklı yollarla demet oluşturma
bos_demet = ()
bos_demet2 = tuple()
sayilar = (10, 20, 30, 40, 50)
karisik = ("Ali", 25, 3.14, True)
parantezsiz = 1, 2, 3               # Parantez olmadan da demet olur
harfler = tuple("PYTHON")           # String'den demet
listeden = tuple([1, 2, 3])         # Listeden demet
print("Boş demet      :", bos_demet, bos_demet2)
print("Sayılar        :", sayilar)
print("Karışık tipler :", karisik)
print("Parantezsiz    :", parantezsiz, type(parantezsiz))
print("Harfler        :", harfler)
print("Listeden       :", listeden)

# Örnek 2 (DİKKAT): Tek elemanlı demette VİRGÜL şarttır!
yanlis = (5)       # Bu bir int'tir, demet DEĞİL
dogru = (5,)       # Bu tek elemanlı demettir
print("(5)  tipi      :", type(yanlis))
print("(5,) tipi      :", type(dogru))

# Örnek 3: İç içe demet
koordinatlar = ((41.0, 28.9), (39.9, 32.8), (38.4, 27.1))
print("İç içe demet   :", koordinatlar)
print("2. şehrin enlemi:", koordinatlar[1][0])   # 39.9


baslik("2. İNDEKSLEME (ELEMANA ERİŞİM)")

gunler = ("Pzt", "Sal", "Çar", "Per", "Cum", "Cmt", "Paz")
#  indeks:   0      1      2      3      4      5      6
#  negatif: -7     -6     -5     -4     -3     -2     -1

# Örnek 1: Pozitif indeks
print("İlk gün        :", gunler[0])
print("Dördüncü gün   :", gunler[3])

# Örnek 2: Negatif indeks (sondan sayma)
print("Son gün        :", gunler[-1])
print("Sondan ikinci  :", gunler[-2])


baslik("3. DİLİMLEME (SLICING)  ->  demet[başlangıç:bitiş:adım]")

sayilar = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

# Örnek 1: Temel dilimleme (bitiş indeksi DAHİL DEĞİLDİR) -> sonuç yine demettir
print("[2:5]   :", sayilar[2:5])
print("[:4]    :", sayilar[:4])
print("[6:]    :", sayilar[6:])

# Örnek 2: Adımlı ve ters dilimleme
print("[::2]   :", sayilar[::2])
print("[::-1]  :", sayilar[::-1])
print("Hafta içi:", gunler[:5], "| Hafta sonu:", gunler[5:])


baslik("4. DEĞİŞTİRİLEMEZLİK (IMMUTABILITY)")

# Örnek 1: Eleman değiştirmeye çalışmak -> TypeError
renkler = ("kırmızı", "yeşil", "mavi")
try:
    renkler[1] = "sarı"
except TypeError as hata:
    print("Hata           :", hata)

# Örnek 2: Değiştirmek gerekirse -> listeye çevir, değiştir, geri demete çevir
gecici = list(renkler)
gecici[1] = "sarı"
renkler = tuple(gecici)
print("Yeni demet     :", renkler)

# Örnek 3: Yeni eleman "eklemek" aslında YENİ bir demet oluşturmaktır
renkler = renkler + ("mor",)
print("Eklenmiş hali  :", renkler)

# Örnek 4 (DİKKAT): Demetin içindeki LİSTE değiştirilebilir
ogrenci = ("Ali", [70, 80])
ogrenci[1].append(90)
print("İçteki liste   :", ogrenci)   # ('Ali', [70, 80, 90])


baslik("5. TEMEL FONKSİYONLAR VE OPERATÖRLER")

# Örnek 1: len, sum, min, max, sorted
puanlar = (85, 92, 78, 95, 60)
print("Eleman sayısı  :", len(puanlar))
print("Toplam         :", sum(puanlar))
print("En küçük       :", min(puanlar))
print("En büyük       :", max(puanlar))
print("sorted()       :", sorted(puanlar), "-> LİSTE döndürür")
print("Sıralı demet   :", tuple(sorted(puanlar)))

# Örnek 2: in / not in, + ve * operatörleri
izinli_roller = ("admin", "editor", "yazar")
print("'admin' var mı?:", "admin" in izinli_roller)
print("'misafir' yok mu?:", "misafir" not in izinli_roller)
print("Birleştirme +  :", (1, 2) + (3, 4))
print("Tekrarlama *   :", ("-",) * 5)


baslik("6. DEMET ÜZERİNDE DÖNGÜ")

# Örnek 1: for ile elemanları gezme
aylar = ("Ocak", "Şubat", "Mart")
for ay in aylar:
    print("Ay:", ay)

# Örnek 2: enumerate ile indeks + eleman
for sira, ay in enumerate(aylar, start=1):
    print(f"{sira}. ay: {ay}")


baslik("7. PAKETLEME VE PAKETTEN ÇIKARMA (PACKING / UNPACKING)")

# Örnek 1: Paketleme ve açma
kisi = "Ayşe", 22, "İstanbul"     # paketleme
isim, yas, sehir = kisi           # paketten çıkarma
print(f"İsim: {isim}, Yaş: {yas}, Şehir: {sehir}")

# Örnek 2: Değişkenlerin yerini değiştirme (swap)
a, b = 5, 10
a, b = b, a
print("Swap sonrası   : a =", a, ", b =", b)

# Örnek 3: Yıldız (*) ile kalan elemanları toplama
ilk, *ortadakiler, son = (1, 2, 3, 4, 5)
print("İlk            :", ilk)
print("Ortadakiler    :", ortadakiler, "(liste olarak gelir)")
print("Son            :", son)

# Örnek 4: Fonksiyondan birden fazla değer döndürme (aslında demet döner)
def istatistik(sayilar):
    return min(sayilar), max(sayilar), sum(sayilar) / len(sayilar)

sonuc = istatistik([4, 8, 15, 16, 23, 42])
print("Dönen değer    :", sonuc, type(sonuc))
en_kucuk, en_buyuk, ortalama = sonuc
print(f"Min: {en_kucuk}, Max: {en_buyuk}, Ort: {ortalama:.2f}")

# Örnek 5: Döngüde demet açma
urunler = (("Kalem", 15), ("Defter", 40), ("Silgi", 10))
for ad, fiyat in urunler:
    print(f"{ad:<8}: {fiyat} TL")


baslik("8. TUPLE COMPREHENSION? -> tuple() + generator")

# Not: (x for x in ...) demet DEĞİL, generator üretir. Demet için tuple() ile sar.
# Örnek 1: Kareler
kareler = tuple(x ** 2 for x in range(1, 6))
print("Kareler        :", kareler)

# Örnek 2: Koşullu - sadece çift sayılar
ciftler = tuple(x for x in range(1, 11) if x % 2 == 0)
print("Çiftler        :", ciftler)

gen = (x for x in range(3))
print("Parantez tek başına:", type(gen))


# ============================================================
# BÖLÜM 2: DEMET METOTLARI
# ============================================================
# Demetler değiştirilemediği için sadece 2 metodu vardır:
# count() ve index()
# (append, remove, sort gibi metotlar demette YOKTUR.)

baslik("METOT 1: count(değer)  ->  Değerin demette kaç kez geçtiğini döndürür")

# Örnek 1: Anket sonuçlarını sayma
cevaplar = ("Evet", "Hayır", "Evet", "Evet", "Kararsız", "Hayır")
print("Evet           :", cevaplar.count("Evet"))
print("Hayır          :", cevaplar.count("Hayır"))
print("Belki          :", cevaplar.count("Belki"))   # yoksa 0, hata vermez

# Örnek 2: Zar atışlarında her sayının frekansı
zarlar = (6, 2, 6, 4, 1, 6, 3, 2)
for yuz in range(1, 7):
    print(f"{yuz} geldi: {zarlar.count(yuz)} kez")

# Örnek 3: Tekrar eden elemanları bulma
demet = (1, 2, 2, 3, 3, 3, 4)
tekrar_edenler = tuple(x for x in sorted(set(demet)) if demet.count(x) > 1)
print("Tekrar edenler :", tekrar_edenler)

# Örnek 4 (DİKKAT): Sadece birinci seviyedeki elemanları sayar
ic_ice = (1, (1, 2), 1, [1])
print("1 sayısı       :", ic_ice.count(1))   # 2 -> içteki 1'leri saymaz


baslik("METOT 2: index(değer, başlangıç, bitiş)  ->  Değerin İLK indeksini döndürür")

# Örnek 1: Elemanın konumunu bulma
gezegenler = ("Merkür", "Venüs", "Dünya", "Mars", "Jüpiter")
print("Mars'ın indeksi:", gezegenler.index("Mars"))
print("Gezegen sırası :", gezegenler.index("Dünya") + 1)

# Örnek 2: Başlangıç parametresi ile sonraki tekrarları bulma
notlar = (70, 85, 70, 90, 70)
konumlar = []
baslangic = 0
while True:
    try:
        konum = notlar.index(70, baslangic)
        konumlar.append(konum)
        baslangic = konum + 1
    except ValueError:
        break
print("70'in tüm konumları:", konumlar)

# Örnek 3: Başlangıç ve bitiş aralığında arama
harfler = ("a", "b", "c", "a", "b", "c")
print("3-6 arasında 'b':", harfler.index("b", 3, 6))

# Örnek 4: Olmayan değer -> ValueError, güvenli kullanım
aranan = "Pluto"
if aranan in gezegenler:
    print(gezegenler.index(aranan))
else:
    print(f"'{aranan}' demette bulunamadı.")


# ============================================================
# BÖLÜM 3: DEMET NE ZAMAN KULLANILIR? (LİSTE vs DEMET)
# ============================================================

baslik("9. DEMETİN AVANTAJLARI")

# Örnek 1: Daha az bellek kullanır
liste_hali = [1, 2, 3, 4, 5]
demet_hali = (1, 2, 3, 4, 5)
print("Liste boyutu   :", sys.getsizeof(liste_hali), "byte")
print("Demet boyutu   :", sys.getsizeof(demet_hali), "byte")

# Örnek 2: Sözlükte ANAHTAR olabilir (liste olamaz)
konum_bilgisi = {
    (41.01, 28.97): "İstanbul",
    (39.93, 32.85): "Ankara",
}
print("Konumdaki şehir:", konum_bilgisi[(39.93, 32.85)])
try:
    {[1, 2]: "deneme"}
except TypeError as hata:
    print("Liste anahtar olamaz:", hata)

# Örnek 3: Değişmemesi gereken sabit veriler için güvenlidir
HAFTANIN_GUNLERI = ("Pazartesi", "Salı", "Çarşamba", "Perşembe",
                    "Cuma", "Cumartesi", "Pazar")
RGB_KIRMIZI = (255, 0, 0)
print("Sabit veri     :", RGB_KIRMIZI)

# Örnek 4: Kümede (set) eleman olabilir
ziyaret_edilen = {(0, 0), (1, 2), (0, 0)}
print("Benzersiz koordinatlar:", ziyaret_edilen)


# ============================================================
# BÖLÜM 4: TÜM KONULARI BİRLEŞTİREN UYGULAMA
# ============================================================

baslik("UYGULAMA: Öğrenci Kayıt Sistemi (değişmeyen kayıtlar)")

ogrenciler = (
    ("1001", "Ali", "Bilgisayar", 78),
    ("1002", "Buse", "Bankacılık", 92),
    ("1003", "Cem", "Bilgisayar", 65),
    ("1004", "Derya", "Muhasebe", 88),
    ("1005", "Ece", "Bilgisayar", 92),
)

# Döngü + unpacking
print(f"{'No':<6}{'Ad':<8}{'Bölüm':<12}{'Not'}")
print("-" * 32)
for no, ad, bolum, notu in ogrenciler:
    print(f"{no:<6}{ad:<8}{bolum:<12}{notu}")

# count
bolumler = tuple(o[2] for o in ogrenciler)
print("\nBilgisayar öğrenci sayısı:", bolumler.count("Bilgisayar"))

# index
numaralar = tuple(o[0] for o in ogrenciler)
aranan_no = "1004"
sira = numaralar.index(aranan_no)
print(f"{aranan_no} numaralı öğrenci:", ogrenciler[sira][1])

# Not istatistikleri
notlar = tuple(o[3] for o in ogrenciler)
print("Not demeti     :", notlar)
print("92 alan sayısı :", notlar.count(92))
print("En yüksek not  :", max(notlar),
      "->", ogrenciler[notlar.index(max(notlar))][1])
print(f"Ortalama       : {sum(notlar) / len(notlar):.2f}")

# Sıralama (sorted ile yeni demet)
siralı = tuple(sorted(ogrenciler, key=lambda o: o[3], reverse=True))
print("Nota göre sıra :", tuple(o[1] for o in siralı))

# Değiştirilemezlik: kayıt korunur
try:
    ogrenciler[0] = ("1001", "Ali", "Bilgisayar", 100)
except TypeError:
    print("Kayıtlar korumalı: not değiştirilemez!")


# ============================================================
# ÖZET TABLO
# ============================================================
baslik("ÖZET: DEMET METOTLARI VE LİSTE KARŞILAŞTIRMASI")
print(f"{'Metot':<20}{'Görevi':<38}{'Döndürdüğü'}")
print("-" * 70)
print(f"{'count(x)':<20}{'x değerinin kaç kez geçtiğini sayar':<38}{'int'}")
print(f"{'index(x, i, j)':<20}{'x değerinin ilk indeksini bulur':<38}{'int'}")

print()
karsilastirma = (
    ("Özellik",            "Liste",          "Demet"),
    ("Yazım",              "[1, 2, 3]",      "(1, 2, 3)"),
    ("Değiştirilebilir",   "Evet",           "Hayır"),
    ("Metot sayısı",       "11",             "2"),
    ("Bellek",             "Daha fazla",     "Daha az"),
    ("Sözlük anahtarı",    "Olamaz",         "Olabilir"),
    ("Kullanım alanı",     "Değişen veri",   "Sabit veri"),
)
for ozellik, liste, demet in karsilastirma:
    print(f"{ozellik:<20}{liste:<16}{demet}")
