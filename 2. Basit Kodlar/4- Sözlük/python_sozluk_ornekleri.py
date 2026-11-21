# -*- coding: utf-8 -*-
"""
PYTHON'DA SÖZLÜK (DICT) KULLANIMI VE SÖZLÜK METOTLARI
======================================================
Sözlük (dict): Verileri ANAHTAR : DEĞER (key : value) çiftleri halinde tutan,
DEĞİŞTİRİLEBİLİR (mutable) veri yapısıdır. Süslü parantez {} ile yazılır.

- Elemanlara indeks ile değil, ANAHTAR ile erişilir.
- Anahtarlar BENZERSİZDİR (aynı anahtar iki kez olamaz).
- Anahtarlar değiştirilemez tipte olmalıdır (str, int, float, tuple...).
  Liste veya sözlük ANAHTAR olamaz.
- Değerler her tipte olabilir ve tekrar edebilir.
- Python 3.7'den itibaren ekleme SIRASI korunur.

Bu dosyayı çalıştırmak için:  python python_sozluk_ornekleri.py
"""


def baslik(metin):
    print("\n" + "=" * 60)
    print(metin)
    print("=" * 60)


# ============================================================
# BÖLÜM 1: TEMEL SÖZLÜK KULLANIMI
# ============================================================

baslik("1. SÖZLÜK OLUŞTURMA")

# Örnek 1: Farklı yollarla sözlük oluşturma
bos_sozluk = {}
bos_sozluk2 = dict()
ogrenci = {"ad": "Ali", "yas": 20, "bolum": "Bilgisayar"}
dict_ile = dict(ad="Ayşe", yas=22)                     # anahtar=değer
ciftlerden = dict([("elma", 30), ("armut", 45)])       # demet listesinden
zip_ile = dict(zip(["a", "b", "c"], [1, 2, 3]))        # iki listeden
print("Boş sözlük     :", bos_sozluk, bos_sozluk2)
print("Öğrenci        :", ogrenci)
print("dict() ile     :", dict_ile)
print("Çiftlerden     :", ciftlerden)
print("zip() ile      :", zip_ile)

# Örnek 2: Farklı anahtar tipleri
cesitli = {1: "bir", "iki": 2, (3, 4): "demet anahtar", 5.5: [1, 2]}
print("Çeşitli anahtar:", cesitli)

# Örnek 3 (DİKKAT): Aynı anahtar tekrar yazılırsa SON değer geçerli olur
tekrar = {"a": 1, "b": 2, "a": 100}
print("Tekrarlı anahtar:", tekrar)

# Örnek 4: Liste anahtar olamaz
try:
    hatali = {[1, 2]: "deneme"}
except TypeError as hata:
    print("Liste anahtar  :", hata)


baslik("2. DEĞERE ERİŞİM")

urun = {"ad": "Laptop", "marka": "X", "fiyat": 25000, "stok": 12}

# Örnek 1: Köşeli parantez [] ile erişim
print("Ürün adı       :", urun["ad"])
print("Fiyat          :", urun["fiyat"])

# Örnek 2: Olmayan anahtar -> KeyError
try:
    print(urun["renk"])
except KeyError as hata:
    print("KeyError       :", hata, "anahtarı yok")
# Güvenli erişim için get() metodu kullanılır (aşağıda METOT 4)


baslik("3. EKLEME, GÜNCELLEME VE SİLME")

telefon_rehberi = {"Ali": "0532 111 11 11", "Ayşe": "0533 222 22 22"}

# Örnek 1: Yeni anahtar ekleme ve mevcut değeri güncelleme
telefon_rehberi["Mehmet"] = "0534 333 33 33"   # yoksa EKLER
telefon_rehberi["Ali"] = "0535 999 99 99"      # varsa GÜNCELLER
print("Rehber         :", telefon_rehberi)

# Örnek 2: del ile silme
del telefon_rehberi["Ayşe"]
print("Ayşe silindi   :", telefon_rehberi)

# Örnek 3: Değeri mevcut değere göre güncelleme
stok = {"kalem": 10, "defter": 5}
stok["kalem"] += 20
stok["defter"] -= 2
print("Güncel stok    :", stok)


baslik("4. TEMEL FONKSİYONLAR VE OPERATÖRLER")

# Örnek 1: len, in, not in (in SADECE anahtarlarda arar!)
sehir_plaka = {"İstanbul": 34, "Ankara": 6, "İzmir": 35}
print("Eleman sayısı  :", len(sehir_plaka))
print("'Ankara' var mı?:", "Ankara" in sehir_plaka)
print("34 var mı?     :", 34 in sehir_plaka, "-> in değerlerde aramaz!")
print("34 değerlerde? :", 34 in sehir_plaka.values())

# Örnek 2: min, max, sum, sorted (varsayılan olarak ANAHTARLAR üzerinde çalışır)
satislar = {"Ocak": 120, "Şubat": 95, "Mart": 140}
print("sorted(anahtar):", sorted(satislar))
print("Toplam satış   :", sum(satislar.values()))
print("En çok satış ayı:", max(satislar, key=satislar.get))

# Örnek 3: | ve |= birleştirme operatörleri (Python 3.9+)
temel = {"renk": "beyaz", "boyut": "M"}
ozel = {"boyut": "L", "desen": "çizgili"}
print("temel | ozel   :", temel | ozel)     # sağdaki baskın
temel |= ozel
print("temel |= ozel  :", temel)


baslik("5. SÖZLÜK ÜZERİNDE DÖNGÜ")

notlar = {"Matematik": 85, "Fizik": 72, "Kimya": 90}

# Örnek 1: Doğrudan döngü -> ANAHTARLARI gezer
for ders in notlar:
    print("Ders:", ders, "| Not:", notlar[ders])

# Örnek 2: items() ile anahtar ve değeri birlikte gezme (en yaygın kullanım)
for ders, puan in notlar.items():
    durum = "Geçti" if puan >= 75 else "Kaldı"
    print(f"{ders:<10}: {puan} -> {durum}")


baslik("6. DICT COMPREHENSION (TEK SATIRDA SÖZLÜK ÜRETME)")

# Örnek 1: Sayıların kareleri
kareler = {x: x ** 2 for x in range(1, 6)}
print("Kareler        :", kareler)

# Örnek 2: Koşullu - sadece geçen dersler
gecenler = {d: p for d, p in notlar.items() if p >= 75}
print("Geçen dersler  :", gecenler)

# Örnek 3: Anahtar ve değerin yerini değiştirme
plaka_sehir = {v: k for k, v in sehir_plaka.items()}
print("Ters sözlük    :", plaka_sehir)

# Örnek 4: Fiyatlara %20 zam
fiyatlar = {"çay": 15, "kahve": 40}
zamli = {urun: round(f * 1.20, 2) for urun, f in fiyatlar.items()}
print("Zamlı fiyatlar :", zamli)


baslik("7. İÇ İÇE SÖZLÜKLER")

# Örnek 1: Sözlük içinde sözlük
sirket = {
    "E001": {"ad": "Ali", "departman": "IT", "maas": 45000},
    "E002": {"ad": "Buse", "departman": "Finans", "maas": 52000},
}
print("E002'nin adı   :", sirket["E002"]["ad"])
sirket["E001"]["maas"] = 48000
print("E001 yeni maaş :", sirket["E001"]["maas"])

# Örnek 2: Sözlük içinde liste
ogrenci = {"ad": "Cem", "notlar": [70, 85, 90]}
ogrenci["notlar"].append(95)
ort = sum(ogrenci["notlar"]) / len(ogrenci["notlar"])
print(f"{ogrenci['ad']} ortalaması: {ort:.2f}")

# Örnek 3: İç içe sözlükte döngü
for sicil, bilgi in sirket.items():
    print(f"{sicil}: {bilgi['ad']} ({bilgi['departman']}) - {bilgi['maas']} TL")


# ============================================================
# BÖLÜM 2: SÖZLÜK METOTLARI
# ============================================================
# Python sözlüklerinin 11 metodu vardır:
# keys, values, items, get, setdefault, update,
# pop, popitem, clear, copy, fromkeys

baslik("METOT 1: keys()  ->  Tüm ANAHTARLARI döndürür")

# Örnek 1: Anahtarları listeleme
kisi = {"ad": "Zeynep", "yas": 25, "meslek": "Analist"}
print("Anahtarlar     :", kisi.keys())
print("Liste olarak   :", list(kisi.keys()))

# Örnek 2: Anahtarlar üzerinden döngü ve kontrol
gerekli_alanlar = ["ad", "yas", "email"]
for alan in gerekli_alanlar:
    if alan not in kisi.keys():
        print(f"Eksik alan: {alan}")

# Örnek 3: keys() CANLI görünümdür (sözlük değişince o da değişir)
anahtarlar = kisi.keys()
kisi["sehir"] = "İzmir"
print("Güncel görünüm :", anahtarlar)

# Örnek 4: İki sözlüğün ortak anahtarları (küme işlemi)
a = {"x": 1, "y": 2, "z": 3}
b = {"y": 20, "z": 30, "w": 40}
print("Ortak anahtarlar:", a.keys() & b.keys())


baslik("METOT 2: values()  ->  Tüm DEĞERLERİ döndürür")

# Örnek 1: Değerleri listeleme ve hesaplama
maaslar = {"Ali": 30000, "Buse": 42000, "Cem": 35000}
print("Değerler       :", maaslar.values())
print("Toplam maaş    :", sum(maaslar.values()))
print("Ortalama maaş  :", sum(maaslar.values()) / len(maaslar))

# Örnek 2: Değerlerde arama ve sayma
renkler = {"elma": "kırmızı", "muz": "sarı", "çilek": "kırmızı"}
print("Kırmızı var mı?:", "kırmızı" in renkler.values())
print("Kırmızı sayısı :", list(renkler.values()).count("kırmızı"))

# Örnek 3: En yüksek ve en düşük değer
print("En yüksek maaş :", max(maaslar.values()))
print("En düşük maaş  :", min(maaslar.values()))


baslik("METOT 3: items()  ->  (anahtar, değer) çiftlerini döndürür")

# Örnek 1: Anahtar-değer çiftlerini gezme
fiyat_listesi = {"ekmek": 10, "süt": 35, "peynir": 180}
print("Çiftler        :", fiyat_listesi.items())
for urun, fiyat in fiyat_listesi.items():
    print(f"{urun:<8}: {fiyat:>5} TL")

# Örnek 2: Değere göre sıralama
siralı = sorted(fiyat_listesi.items(), key=lambda cift: cift[1], reverse=True)
print("Pahalıdan ucuza:", siralı)
print("Sıralı sözlük  :", dict(siralı))

# Örnek 3: Koşula uyan çiftleri bulma
pahali = [u for u, f in fiyat_listesi.items() if f > 30]
print("30 TL üstü     :", pahali)


baslik("METOT 4: get(anahtar, varsayılan)  ->  Değeri GÜVENLİ şekilde döndürür")

# Örnek 1: Olmayan anahtarda hata yerine None veya varsayılan döner
ayarlar = {"tema": "koyu", "dil": "tr"}
print("tema           :", ayarlar.get("tema"))
print("yazi_boyutu    :", ayarlar.get("yazi_boyutu"))          # None
print("yazi_boyutu    :", ayarlar.get("yazi_boyutu", 14))      # varsayılan

# Örnek 2: Kelime frekansı sayma (get'in en klasik kullanımı)
metin = "elma armut elma muz armut elma"
frekans = {}
for kelime in metin.split():
    frekans[kelime] = frekans.get(kelime, 0) + 1
print("Kelime frekansı:", frekans)

# Örnek 3: Kullanıcı girişi kontrolü
kullanicilar = {"admin": "1234", "batu": "abcd"}
giris_adi, giris_sifre = "misafir", "0000"
if kullanicilar.get(giris_adi) == giris_sifre:
    print("Giriş başarılı")
else:
    print("Kullanıcı adı veya şifre hatalı")

# DİKKAT: get() sözlüğe eleman EKLEMEZ
print("Sözlük değişmedi:", ayarlar)


baslik("METOT 5: setdefault(anahtar, varsayılan)  ->  Anahtar yoksa EKLER, değeri döndürür")

# Örnek 1: Anahtar varsa mevcut değer, yoksa ekleyip varsayılanı döndürür
profil = {"ad": "Ece"}
print("Var olan       :", profil.setdefault("ad", "Bilinmiyor"))
print("Olmayan        :", profil.setdefault("sehir", "İstanbul"))
print("Profil         :", profil)     # sehir eklendi

# Örnek 2: Gruplama - öğrencileri bölümlerine göre toplama
kayitlar = [("Ali", "IT"), ("Buse", "Finans"), ("Cem", "IT"), ("Derya", "Finans")]
bolumler = {}
for ad, bolum in kayitlar:
    bolumler.setdefault(bolum, []).append(ad)
print("Bölümlere göre :", bolumler)

# Örnek 3: Harfleri ilk harfe göre gruplama
kelimeler = ["araba", "balık", "armut", "bulut", "çiçek"]
gruplar = {}
for k in kelimeler:
    gruplar.setdefault(k[0], []).append(k)
print("İlk harfe göre :", gruplar)


baslik("METOT 6: update(diğer)  ->  Başka bir sözlükle GÜNCELLER / EKLER")

# Örnek 1: Birden fazla değeri tek seferde güncelleme
hesap = {"sahip": "Ali", "bakiye": 1000, "tip": "vadesiz"}
hesap.update({"bakiye": 1500, "para_birimi": "TL"})
print("Güncel hesap   :", hesap)

# Örnek 2: Farklı biçimlerde update
ayar = {"ses": 50}
ayar.update(parlaklik=80, ses=70)                 # anahtar=değer
ayar.update([("dil", "tr"), ("bildirim", True)])  # çift listesi
print("Ayarlar        :", ayar)

# Örnek 3: Varsayılan ayarları kullanıcı ayarlarıyla birleştirme
varsayilan = {"tema": "açık", "dil": "en", "bildirim": True}
kullanici = {"tema": "koyu", "dil": "tr"}
son_ayar = varsayilan.copy()
son_ayar.update(kullanici)
print("Birleşik ayar  :", son_ayar)


baslik("METOT 7: pop(anahtar, varsayılan)  ->  Anahtarı siler ve DEĞERİNİ döndürür")

# Örnek 1: Silinen değeri kullanma
sepet = {"elma": 3, "armut": 2, "muz": 5}
alinan = sepet.pop("armut")
print("Silinen adet   :", alinan)
print("Kalan sepet    :", sepet)

# Örnek 2: Olmayan anahtar -> varsayılan değer (hata vermez)
sonuc = sepet.pop("kiraz", 0)
print("Kiraz          :", sonuc)

# Örnek 3: Varsayılan verilmezse -> KeyError
try:
    sepet.pop("kiraz")
except KeyError:
    print("KeyError: 'kiraz' sepette yok")

# Örnek 4: Hassas bilgiyi ayırma
kullanici = {"ad": "Batu", "email": "x@y.com", "sifre": "gizli123"}
kullanici.pop("sifre")
print("Paylaşılabilir :", kullanici)


baslik("METOT 8: popitem()  ->  SON eklenen çifti siler ve (anahtar, değer) döndürür")

# Örnek 1: Son eklenen elemanı silme
islemler = {"1": "giriş", "2": "transfer", "3": "çıkış"}
son = islemler.popitem()
print("Silinen çift   :", son)
print("Kalanlar       :", islemler)

# Örnek 2: Geri alma (undo) mantığı - LIFO
degisiklikler = {}
degisiklikler["adim1"] = "başlık eklendi"
degisiklikler["adim2"] = "resim eklendi"
degisiklikler["adim3"] = "metin silindi"
anahtar, deger = degisiklikler.popitem()
print(f"Geri alındı    : {anahtar} -> {deger}")

# Örnek 3: Sözlük boşalana kadar işleme + boş sözlükte KeyError
gorevler = {"rapor": "yüksek", "mail": "düşük"}
while gorevler:
    g, oncelik = gorevler.popitem()
    print(f"İşlendi: {g} ({oncelik})")
try:
    gorevler.popitem()
except KeyError:
    print("Boş sözlükte popitem() -> KeyError")


baslik("METOT 9: clear()  ->  Sözlüğün TÜM elemanlarını siler")

# Örnek 1: Önbelleği temizleme
onbellek = {"sayfa1": "<html>...", "sayfa2": "<html>..."}
onbellek.clear()
print("Önbellek       :", onbellek, "| uzunluk:", len(onbellek))

# Örnek 2: Oturum verisini sıfırlama
oturum = {"kullanici": "batu", "giris_saati": "15:00", "sepet": 3}
print("Çıkış öncesi   :", oturum)
oturum.clear()
oturum["kullanici"] = "misafir"
print("Çıkış sonrası  :", oturum)

# Örnek 3 (DİKKAT): clear() ile = {} farkı
a = {"x": 1}
b = a              # aynı sözlüğü gösterir
a.clear()          # ortak sözlüğü boşaltır -> b de boşalır
print("clear() sonrası b:", b)
c = {"x": 1}
d = c
c = {}             # c yeni boş sözlüğe bağlanır -> d etkilenmez
print("= {} sonrası d :", d)


baslik("METOT 10: copy()  ->  Sözlüğün YÜZEYSEL (shallow) kopyasını döndürür")

# Örnek 1: Atama (=) ile copy() farkı
orijinal = {"a": 1, "b": 2}
ayni = orijinal
kopya = orijinal.copy()
orijinal["c"] = 3
print("Orijinal       :", orijinal)
print("= ile atanan   :", ayni)      # o da değişti
print("copy() ile     :", kopya)     # değişmedi

# Örnek 2: Şablondan yeni kayıt oluşturma
sablon = {"durum": "aktif", "rol": "üye", "puan": 0}
yeni_uye = sablon.copy()
yeni_uye["ad"] = "Can"
print("Şablon         :", sablon)
print("Yeni üye       :", yeni_uye)

# Örnek 3 (DİKKAT): İç içe yapılarda copy() yetmez -> deepcopy
import copy
veri = {"ad": "Ali", "notlar": [70, 80]}
yuzeysel = veri.copy()
derin = copy.deepcopy(veri)
veri["notlar"].append(100)
print("Yüzeysel kopya :", yuzeysel)   # etkilendi
print("Derin kopya    :", derin)      # etkilenmedi


baslik("METOT 11: dict.fromkeys(anahtarlar, değer)  ->  Anahtarlardan yeni sözlük oluşturur")

# Örnek 1: Tüm anahtarlara aynı başlangıç değeri
dersler = ["Matematik", "Fizik", "Kimya"]
not_tablosu = dict.fromkeys(dersler, 0)
print("Not tablosu    :", not_tablosu)

# Örnek 2: Değer verilmezse None
alanlar = dict.fromkeys(["ad", "soyad", "email"])
print("Boş form       :", alanlar)

# Örnek 3: Listeden tekrarları silip SIRAYI koruma
tekrarli = ["elma", "armut", "elma", "muz", "armut"]
benzersiz = list(dict.fromkeys(tekrarli))
print("Benzersiz      :", benzersiz)

# Örnek 4 (DİKKAT): Değiştirilebilir değer (liste) TÜM anahtarlarda ORTAK olur
hatali = dict.fromkeys(["a", "b"], [])
hatali["a"].append(1)
print("Hatalı kullanım:", hatali)    # {'a': [1], 'b': [1]}
dogru = {k: [] for k in ["a", "b"]}
dogru["a"].append(1)
print("Doğru kullanım :", dogru)     # {'a': [1], 'b': []}


# ============================================================
# BÖLÜM 3: TÜM METOTLARI BİRLEŞTİREN UYGULAMA
# ============================================================

baslik("UYGULAMA: Mini Yatırım Portföyü Takibi")

portfoy = dict.fromkeys(["THYAO", "ASELS"], 0)            # fromkeys
print("Başlangıç      :", portfoy)

portfoy.update({"THYAO": 100, "ASELS": 50, "BIMAS": 30})  # update
portfoy["KCHOL"] = 40                                     # ekleme
print("Alımlar sonrası:", portfoy)

portfoy.setdefault("GARAN", 0)                            # setdefault
portfoy["GARAN"] += 25

fiyatlar = {"THYAO": 300, "ASELS": 60, "BIMAS": 500, "KCHOL": 180, "GARAN": 120}
print("\nHisse  Adet  Fiyat     Değer")
print("-" * 32)
toplam = 0
for hisse, adet in portfoy.items():                       # items
    fiyat = fiyatlar.get(hisse, 0)                        # get
    deger = adet * fiyat
    toplam += deger
    print(f"{hisse:<7}{adet:<6}{fiyat:<10}{deger:,} TL")
print(f"Toplam portföy değeri: {toplam:,} TL")

print("\nHisseler       :", list(portfoy.keys()))           # keys
print("Toplam adet    :", sum(portfoy.values()))           # values

yedek = portfoy.copy()                                     # copy
satilan = portfoy.pop("KCHOL")                             # pop
print(f"KCHOL satıldı  : {satilan} adet")

son_hisse = portfoy.popitem()                              # popitem
print("Son alım iptal :", son_hisse)
print("Güncel portföy :", portfoy)
print("Yedek          :", yedek)

portfoy.clear()                                            # clear
print("Portföy kapatıldı:", portfoy)


# ============================================================
# ÖZET TABLO
# ============================================================
baslik("ÖZET: SÖZLÜK METOTLARI")
ozet = [
    ("keys()",              "Tüm anahtarları verir",              "Görünüm (view)"),
    ("values()",            "Tüm değerleri verir",                "Görünüm (view)"),
    ("items()",             "(anahtar, değer) çiftlerini verir",  "Görünüm (view)"),
    ("get(k, v)",           "Değeri güvenli şekilde verir",       "Değer / v / None"),
    ("setdefault(k, v)",    "Yoksa ekler, değeri verir",          "Değer"),
    ("update(d)",           "Başka sözlükle günceller",           "None"),
    ("pop(k, v)",           "Anahtarı siler, değeri verir",       "Silinen değer"),
    ("popitem()",           "Son çifti siler",                    "(anahtar, değer)"),
    ("clear()",             "Tüm elemanları siler",               "None"),
    ("copy()",              "Yüzeysel kopya oluşturur",           "Yeni sözlük"),
    ("dict.fromkeys(a, v)", "Anahtarlardan sözlük oluşturur",     "Yeni sözlük"),
]
print(f"{'Metot':<21}{'Görevi':<36}{'Döndürdüğü'}")
print("-" * 75)
for metot, gorev, donus in ozet:
    print(f"{metot:<21}{gorev:<36}{donus}")

print()
karsilastirma = (
    ("Özellik",          "Liste",        "Demet",        "Sözlük"),
    ("Yazım",            "[1, 2]",       "(1, 2)",       "{'a': 1}"),
    ("Erişim",           "İndeks",       "İndeks",       "Anahtar"),
    ("Değiştirilebilir", "Evet",         "Hayır",        "Evet"),
    ("Tekrar",           "Olabilir",     "Olabilir",     "Anahtar olamaz"),
    ("Metot sayısı",     "11",           "2",            "11"),
)
for satir in karsilastirma:
    print(f"{satir[0]:<18}{satir[1]:<12}{satir[2]:<12}{satir[3]}")
