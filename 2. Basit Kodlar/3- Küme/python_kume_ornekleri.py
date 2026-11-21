# -*- coding: utf-8 -*-
"""
PYTHON'DA KÜME (SET) KULLANIMI VE KÜME METOTLARI
=================================================
Küme (set): BENZERSİZ elemanları SIRASIZ şekilde tutan,
DEĞİŞTİRİLEBİLİR (mutable) veri yapısıdır. Süslü parantez {} ile yazılır.

- Aynı eleman iki kez bulunamaz (tekrarlar otomatik silinir).
- Elemanlar sırasızdır, İNDEKS YOKTUR (kume[0] çalışmaz).
- Elemanlar değiştirilemez tipte olmalıdır (int, str, float, tuple...).
  Liste, sözlük veya küme ELEMAN olamaz.
- Matematikteki kümeler gibi birleşim, kesişim, fark işlemleri yapılır.
- Eleman arama (in) listeye göre ÇOK daha hızlıdır.

Not: Küme sırasız olduğu için yazdırılan eleman sırası farklı görünebilir.
     Bu dosyada okunabilirlik için bazı çıktılar sorted() ile sıralanmıştır.

Bu dosyayı çalıştırmak için:  python python_kume_ornekleri.py
"""


def baslik(metin):
    print("\n" + "=" * 60)
    print(metin)
    print("=" * 60)


# ============================================================
# BÖLÜM 1: TEMEL KÜME KULLANIMI
# ============================================================

baslik("1. KÜME OLUŞTURMA")

# Örnek 1: Farklı yollarla küme oluşturma
sayilar = {1, 2, 3, 4, 5}
karisik = {"Ali", 25, 3.14, (1, 2)}
listeden = set([1, 2, 2, 3, 3, 3])      # tekrarlar silinir
stringden = set("merhaba")              # benzersiz harfler
aralik = set(range(1, 6))
print("Sayılar        :", sayilar)
print("Karışık tipler :", karisik)
print("Listeden       :", listeden)
print("String'den     :", sorted(stringden))
print("range ile      :", aralik)

# Örnek 2 (DİKKAT): Boş küme {} ile DEĞİL, set() ile oluşturulur
bos1 = {}
bos2 = set()
print("{} tipi        :", type(bos1), "-> bu SÖZLÜK!")
print("set() tipi     :", type(bos2))

# Örnek 3: Liste eleman olamaz
try:
    hatali = {1, [2, 3]}
except TypeError as hata:
    print("Liste eleman   :", hata)


baslik("2. TEKRARLARI SİLME (KÜMENİN EN YAYGIN KULLANIMI)")

# Örnek 1: Listedeki tekrar eden elemanları silme
ziyaretciler = ["ali", "buse", "ali", "cem", "buse", "ali"]
benzersiz = set(ziyaretciler)
print("Tüm girişler   :", len(ziyaretciler))
print("Tekil ziyaretçi:", len(benzersiz), sorted(benzersiz))

# Örnek 2: Tekrarları silip tekrar listeye çevirme
notlar = [70, 85, 70, 90, 85, 100]
tekil_notlar = sorted(set(notlar))
print("Tekil notlar   :", tekil_notlar)

# Örnek 3: Listede tekrar var mı kontrolü
liste = [1, 2, 3, 4, 2]
print("Tekrar var mı? :", len(liste) != len(set(liste)))


baslik("3. ERİŞİM: İNDEKS YOK -> in VE DÖNGÜ")

# Örnek 1: İndeks ile erişim çalışmaz
meyveler = {"elma", "armut", "muz"}
try:
    print(meyveler[0])
except TypeError as hata:
    print("İndeks hatası  :", hata)

# Örnek 2: in ile üyelik kontrolü
print("'elma' var mı? :", "elma" in meyveler)
print("'kiraz' yok mu?:", "kiraz" not in meyveler)

# Örnek 3: for ile gezme
for meyve in sorted(meyveler):
    print("Meyve:", meyve)


baslik("4. TEMEL FONKSİYONLAR")

# Örnek 1: len, sum, min, max, sorted
puanlar = {85, 92, 78, 95, 60}
print("Eleman sayısı  :", len(puanlar))
print("Toplam         :", sum(puanlar))
print("En küçük       :", min(puanlar))
print("En büyük       :", max(puanlar))
print("sorted()       :", sorted(puanlar), "-> LİSTE döndürür")

# Örnek 2: Eşitlik sıraya bakmaz
print("{1,2,3} == {3,2,1}:", {1, 2, 3} == {3, 2, 1})
print("[1,2,3] == [3,2,1]:", [1, 2, 3] == [3, 2, 1])


baslik("5. SET COMPREHENSION")

# Örnek 1: Kareler
kareler = {x ** 2 for x in range(-3, 4)}
print("Kareler        :", sorted(kareler))   # -3 ve 3'ün karesi tek sefer

# Örnek 2: Koşullu - cümledeki 3 harften uzun benzersiz kelimeler
cumle = "bir gün bir yatırımcı bir hisse aldı ve hisse yükseldi"
uzunlar = {k for k in cumle.split() if len(k) > 3}
print("Uzun kelimeler :", sorted(uzunlar))

# Örnek 3: E-postalardan benzersiz alan adları
mailler = ["a@gmail.com", "b@hotmail.com", "c@gmail.com", "d@okul.edu.tr"]
alanlar = {m.split("@")[1] for m in mailler}
print("Alan adları    :", sorted(alanlar))


# ============================================================
# BÖLÜM 2: KÜME METOTLARI
# ============================================================
# A) Ekleme / silme   : add, update, remove, discard, pop, clear, copy
# B) Küme işlemleri   : union, intersection, difference, symmetric_difference
# C) Yerinde işlemler : intersection_update, difference_update,
#                       symmetric_difference_update
# D) Karşılaştırma    : issubset, issuperset, isdisjoint

# ----------------- A) EKLEME / SİLME METOTLARI ----------------

baslik("METOT 1: add(eleman)  ->  Kümeye TEK eleman ekler")

# Örnek 1: Eleman ekleme
renkler = {"kırmızı", "mavi"}
renkler.add("yeşil")
print("Eklendi        :", sorted(renkler))

# Örnek 2: Var olan eleman eklenirse bir şey değişmez (hata da vermez)
renkler.add("mavi")
print("Tekrar eklendi :", sorted(renkler), "| uzunluk:", len(renkler))

# Örnek 3: Döngüde benzersiz değerleri toplama
islemler = ["THYAO", "ASELS", "THYAO", "BIMAS", "ASELS"]
islem_yapilan = set()
for hisse in islemler:
    islem_yapilan.add(hisse)
print("İşlem görenler :", sorted(islem_yapilan))

# Örnek 4: Demet eklenebilir, liste eklenemez
koordinat = set()
koordinat.add((41, 29))
print("Demet eklendi  :", koordinat)


baslik("METOT 2: update(yinelenebilir)  ->  Birden fazla eleman ekler")

# Örnek 1: Liste ile birden fazla eleman ekleme
diller = {"Python"}
diller.update(["Java", "C#", "Python"])
print("Diller         :", sorted(diller))

# Örnek 2: Aynı anda birden fazla kaynak
etiketler = {"finans"}
etiketler.update({"borsa", "yatırım"}, ("finans", "ekonomi"), ["kripto"])
print("Etiketler      :", sorted(etiketler))

# Örnek 3 (DİKKAT): String verilirse harflere ayrılır
k = {"a"}
k.update("python")
print("update('python'):", sorted(k))
k2 = {"a"}
k2.add("python")
print("add('python')  :", sorted(k2))


baslik("METOT 3: remove(eleman)  ->  Elemanı siler, YOKSA HATA verir")

# Örnek 1: Eleman silme
sehirler = {"İstanbul", "Ankara", "İzmir"}
sehirler.remove("Ankara")
print("Ankara silindi :", sorted(sehirler))

# Örnek 2: Olmayan eleman -> KeyError
try:
    sehirler.remove("Bursa")
except KeyError as hata:
    print("KeyError       :", hata, "kümede yok")

# Örnek 3: Güvenli silme
silinecek = "Bursa"
if silinecek in sehirler:
    sehirler.remove(silinecek)
else:
    print(f"'{silinecek}' bulunamadı, silinmedi.")


baslik("METOT 4: discard(eleman)  ->  Elemanı siler, YOKSA HATA VERMEZ")

# Örnek 1: Eleman silme
aktif = {"ali", "buse", "cem"}
aktif.discard("buse")
print("buse çıkış yaptı:", sorted(aktif))

# Örnek 2: Olmayan eleman -> sessizce geçer
aktif.discard("zeynep")
print("Olmayanı silme :", sorted(aktif), "-> hata yok")

# Örnek 3: Kara listedekileri temizleme
kullanicilar = {"u1", "u2", "u3", "u4"}
kara_liste = ["u2", "u9", "u4"]
for u in kara_liste:
    kullanicilar.discard(u)
print("Temiz liste    :", sorted(kullanicilar))


baslik("METOT 5: pop()  ->  RASTGELE bir elemanı siler ve döndürür")

# Örnek 1: Eleman çekme (hangi elemanın geleceği garanti değildir)
torba = {"kırmızı top", "mavi top", "yeşil top"}
cekilen = torba.pop()
print("Çekilen        :", cekilen)
print("Kalan          :", len(torba), "top")

# Örnek 2: Küme boşalana kadar işleme
gorevler = {"rapor", "mail", "toplantı"}
while gorevler:
    print("İşlendi:", gorevler.pop())

# Örnek 3: Boş kümede pop() -> KeyError
try:
    set().pop()
except KeyError:
    print("Boş kümede pop() -> KeyError")


baslik("METOT 6: clear()  ->  Kümenin TÜM elemanlarını siler")

# Örnek 1: Kümeyi boşaltma
secilenler = {"A", "B", "C"}
secilenler.clear()
print("Boşaltıldı     :", secilenler, "| uzunluk:", len(secilenler))

# Örnek 2: Günlük tekil ziyaretçileri her gün sıfırlama
gunluk_ziyaretci = {"ip1", "ip2", "ip3"}
print("Gün sonu       :", len(gunluk_ziyaretci), "tekil ziyaretçi")
gunluk_ziyaretci.clear()
gunluk_ziyaretci.add("ip7")
print("Yeni gün       :", gunluk_ziyaretci)


baslik("METOT 7: copy()  ->  Kümenin kopyasını döndürür")

# Örnek 1: Atama (=) ile copy() farkı
orijinal = {1, 2, 3}
ayni = orijinal
kopya = orijinal.copy()
orijinal.add(4)
print("Orijinal       :", orijinal)
print("= ile atanan   :", ayni)     # değişti
print("copy() ile     :", kopya)    # değişmedi

# Örnek 2: Orijinali bozmadan deneme yapma
portfoy = {"THYAO", "ASELS", "BIMAS"}
senaryo = portfoy.copy()
senaryo.discard("ASELS")
senaryo.add("GARAN")
print("Gerçek portföy :", sorted(portfoy))
print("Senaryo        :", sorted(senaryo))


# ----------------- B) KÜME İŞLEMLERİ (YENİ KÜME DÖNDÜRÜR) -----

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

baslik("METOT 8: union()  ->  BİRLEŞİM (A ∪ B) - operatör: |")

# Örnek 1: İki kümenin birleşimi
print("A              :", A)
print("B              :", B)
print("A.union(B)     :", A.union(B))
print("A | B          :", A | B)

# Örnek 2: İki dersin tüm öğrencileri
python_dersi = {"Ali", "Buse", "Cem"}
finans_dersi = {"Cem", "Derya", "Ece"}
print("Tüm öğrenciler :", sorted(python_dersi.union(finans_dersi)))

# Örnek 3: Birden fazla küme ve liste ile birleşim
# (metot liste de kabul eder, | operatörü sadece küme kabul eder)
ocak = {"THYAO", "ASELS"}
subat = {"BIMAS"}
mart = ["THYAO", "KCHOL"]
print("3 aylık hisseler:", sorted(ocak.union(subat, mart)))


baslik("METOT 9: intersection()  ->  KESİŞİM (A ∩ B) - operatör: &")

# Örnek 1: İki kümenin kesişimi
print("A.intersection(B):", A.intersection(B))
print("A & B          :", A & B)

# Örnek 2: Her iki dersi de alan öğrenciler
print("İki dersi alan :", python_dersi.intersection(finans_dersi))

# Örnek 3: Ortak ilgi alanları
ali_ilgi = {"borsa", "futbol", "kitap", "kripto"}
buse_ilgi = {"kitap", "sinema", "borsa"}
cem_ilgi = {"borsa", "kitap", "müzik"}
print("Üçünün ortağı  :", sorted(ali_ilgi.intersection(buse_ilgi, cem_ilgi)))


baslik("METOT 10: difference()  ->  FARK (A - B) - operatör: -")

# Örnek 1: A'da olup B'de olmayanlar (sıra önemlidir!)
print("A - B          :", A.difference(B))
print("B - A          :", B - A)

# Örnek 2: Sadece Python dersini alanlar
print("Sadece Python  :", sorted(python_dersi.difference(finans_dersi)))

# Örnek 3: Eksik belgeler
gerekli = {"kimlik", "diploma", "fotoğraf", "transkript"}
teslim_edilen = {"kimlik", "fotoğraf"}
print("Eksik belgeler :", sorted(gerekli - teslim_edilen))


baslik("METOT 11: symmetric_difference()  ->  SİMETRİK FARK (A Δ B) - operatör: ^")

# Örnek 1: Sadece birinde olanlar (ortaklar hariç)
print("A ^ B          :", A.symmetric_difference(B))
print("A ^ B          :", A ^ B)

# Örnek 2: Tek bir dersi alanlar
print("Tek ders alan  :", sorted(python_dersi ^ finans_dersi))

# Örnek 3: İki dosya sürümü arasında değişen satırlar
eski_surum = {"satır1", "satır2", "satır3"}
yeni_surum = {"satır1", "satır3", "satır4"}
print("Değişen satırlar:", sorted(eski_surum ^ yeni_surum))


# ----------------- C) YERİNDE (UPDATE) İŞLEMLERİ ---------------
# Bu metotlar yeni küme döndürmez, kümenin KENDİSİNİ değiştirir (None döner).

baslik("METOT 12: intersection_update()  ->  Kümeyi KESİŞİMLE günceller (&=)")

# Örnek 1: Sadece ortak elemanları bırakma
x = {1, 2, 3, 4}
x.intersection_update({3, 4, 5})
print("x              :", x)

# Örnek 2: Stokta olan ürünlerle sepeti filtreleme
sepet = {"laptop", "mouse", "kulaklık", "kamera"}
stokta = {"mouse", "kamera", "klavye"}
sepet &= stokta
print("Satın alınabilir:", sorted(sepet))


baslik("METOT 13: difference_update()  ->  Kümeyi FARKLA günceller (-=)")

# Örnek 1: Diğer kümedeki elemanları çıkarma
y = {1, 2, 3, 4, 5}
y.difference_update({2, 4})
print("y              :", y)

# Örnek 2: Okunan mailleri gelen kutusundan çıkarma
okunmamis = {"mail1", "mail2", "mail3", "mail4"}
okunanlar = {"mail1", "mail3"}
okunmamis -= okunanlar
print("Okunmamış      :", sorted(okunmamis))


baslik("METOT 14: symmetric_difference_update()  ->  SİMETRİK FARKLA günceller (^=)")

# Örnek 1: Ortakları çıkar, farklıları ekle
z = {1, 2, 3}
z.symmetric_difference_update({3, 4, 5})
print("z              :", z)

# Örnek 2: Seçim değiştirme (seçiliyse kaldır, değilse ekle -> toggle)
secili = {"A", "B", "C"}
tiklananlar = {"B", "D"}
secili ^= tiklananlar
print("Yeni seçim     :", sorted(secili))


# ----------------- D) KARŞILAŞTIRMA METOTLARI (True/False) -----

baslik("METOT 15: issubset()  ->  ALT KÜME mi? (A ⊆ B) - operatör: <=")

# Örnek 1: Temel kullanım
kucuk = {1, 2}
buyuk = {1, 2, 3, 4}
print("{1,2} ⊆ {1,2,3,4}:", kucuk.issubset(buyuk))
print("{1,2,3,4} ⊆ {1,2}:", buyuk <= kucuk)

# Örnek 2: Kullanıcının yetkisi yeterli mi?
istenen_yetki = {"okuma", "yazma"}
kullanici_yetki = {"okuma", "yazma", "silme"}
print("Yetki yeterli  :", istenen_yetki.issubset(kullanici_yetki))

# Örnek 3: Ön koşul dersleri tamamlanmış mı?
on_kosul = {"Matematik 1", "Programlama 1"}
tamamlanan = {"Matematik 1", "Fizik"}
print("Derse kayıt olabilir mi?:", on_kosul <= tamamlanan)


baslik("METOT 16: issuperset()  ->  ÜST KÜME mi? (A ⊇ B) - operatör: >=")

# Örnek 1: Temel kullanım
print("{1,2,3,4} ⊇ {1,2}:", buyuk.issuperset(kucuk))

# Örnek 2: Paket tüm özellikleri içeriyor mu?
premium = {"reklamsız", "indirme", "4K", "çoklu cihaz"}
istenen = {"indirme", "4K"}
print("Premium yeterli:", premium.issuperset(istenen))

# Örnek 3: Şifre tüm karakter türlerini içeriyor mu?
sifre = "Abc123!x"
turler = set()
for ch in sifre:
    if ch.isupper():
        turler.add("büyük")
    elif ch.islower():
        turler.add("küçük")
    elif ch.isdigit():
        turler.add("rakam")
    else:
        turler.add("özel")
print("Güçlü şifre mi?:", turler >= {"büyük", "küçük", "rakam", "özel"})


baslik("METOT 17: isdisjoint()  ->  Hiç ORTAK eleman yok mu?")

# Örnek 1: Temel kullanım
print("{1,2} & {3,4} ayrık mı?:", {1, 2}.isdisjoint({3, 4}))
print("{1,2} & {2,3} ayrık mı?:", {1, 2}.isdisjoint({2, 3}))

# Örnek 2: Toplantı saatleri çakışıyor mu?
ali_dolu = {"09:00", "10:00", "14:00"}
buse_dolu = {"11:00", "15:00"}
if ali_dolu.isdisjoint(buse_dolu):
    print("Çakışma yok, ortak plan yapılabilir.")

# Örnek 3: Alerjen kontrolü
yemek_icerik = {"un", "yumurta", "süt", "şeker"}
alerjiler = {"fıstık", "susam"}
print("Yemek güvenli mi?:", yemek_icerik.isdisjoint(alerjiler))


# ============================================================
# BÖLÜM 3: FROZENSET (DEĞİŞTİRİLEMEZ KÜME)
# ============================================================

baslik("8. FROZENSET  ->  Değiştirilemez küme")

# Örnek 1: Oluşturma ve değiştirmeye çalışma
sabit = frozenset([1, 2, 3])
print("frozenset      :", sabit)
try:
    sabit.add(4)
except AttributeError as hata:
    print("Ekleme hatası  :", hata)

# Örnek 2: Sözlük anahtarı veya küme elemanı olabilir (normal set olamaz)
fiyat_paketleri = {
    frozenset({"internet", "tv"}): 450,
    frozenset({"internet", "tv", "telefon"}): 600,
}
print("İnternet+TV    :", fiyat_paketleri[frozenset({"tv", "internet"})], "TL")

# Örnek 3: Küme işlemleri frozenset ile de çalışır
print("Birleşim       :", sabit | {3, 4})


# ============================================================
# BÖLÜM 4: TÜM METOTLARI BİRLEŞTİREN UYGULAMA
# ============================================================

baslik("UYGULAMA: İki Yatırımcının Portföy Karşılaştırması")

batu = {"THYAO", "ASELS", "BIMAS"}
batu.add("KCHOL")                                   # add
batu.update(["GARAN", "THYAO"])                     # update
ayse = {"ASELS", "GARAN", "SISE", "TUPRS", "EREGL"}

print("Batu           :", sorted(batu))
print("Ayşe           :", sorted(ayse))

print("\nTüm hisseler   :", sorted(batu.union(ayse)))                    # union
print("Ortak hisseler :", sorted(batu.intersection(ayse)))               # intersection
print("Sadece Batu'da :", sorted(batu.difference(ayse)))                 # difference
print("Sadece birinde :", sorted(batu.symmetric_difference(ayse)))       # symmetric_difference

bist30_ornek = {"THYAO", "ASELS", "BIMAS", "KCHOL", "GARAN", "SISE", "TUPRS"}
print("\nBatu tamamen BIST30 mu?:", batu.issubset(bist30_ornek))       # issubset
print("Ayşe tamamen BIST30 mu?:", ayse <= bist30_ornek)
print("BIST30 Batu'yu kapsar mı?:", bist30_ornek.issuperset(batu))      # issuperset
print("Bankacılık yok mu? (Ayşe):", ayse.isdisjoint({"AKBNK", "YKBNK"}))  # isdisjoint

yedek = batu.copy()                                 # copy
batu.remove("BIMAS")                                # remove
batu.discard("XXXX")                                # discard (hata yok)
satilan = batu.pop()                                # pop
print("\nRastgele satılan:", satilan)
print("Güncel Batu    :", sorted(batu))
print("Yedek          :", sorted(yedek))

izlenen = set(yedek)
izlenen.intersection_update(bist30_ornek)          # intersection_update
izlenen.difference_update({"KCHOL"})               # difference_update
izlenen.symmetric_difference_update({"GARAN", "TUPRS"})  # symmetric_difference_update
print("İzleme listesi :", sorted(izlenen))

izlenen.clear()                                     # clear
print("Liste temizlendi:", izlenen)


# ============================================================
# ÖZET TABLO
# ============================================================
baslik("ÖZET: KÜME METOTLARI")
ozet = [
    ("add(x)",                        "",    "Tek eleman ekler"),
    ("update(...)",                   "|=",  "Birden çok eleman ekler"),
    ("remove(x)",                     "",    "Siler, yoksa HATA"),
    ("discard(x)",                    "",    "Siler, yoksa hata YOK"),
    ("pop()",                         "",    "Rastgele eleman siler, döndürür"),
    ("clear()",                       "",    "Tüm elemanları siler"),
    ("copy()",                        "",    "Kopya oluşturur"),
    ("union(...)",                    "|",   "Birleşim -> yeni küme"),
    ("intersection(...)",             "&",   "Kesişim -> yeni küme"),
    ("difference(...)",               "-",   "Fark -> yeni küme"),
    ("symmetric_difference(x)",       "^",   "Simetrik fark -> yeni küme"),
    ("intersection_update(...)",      "&=",  "Kesişimle yerinde günceller"),
    ("difference_update(...)",        "-=",  "Farkla yerinde günceller"),
    ("symmetric_difference_update(x)", "^=", "Simetrik farkla günceller"),
    ("issubset(x)",                   "<=",  "Alt küme mi? -> bool"),
    ("issuperset(x)",                 ">=",  "Üst küme mi? -> bool"),
    ("isdisjoint(x)",                 "",    "Ortak eleman yok mu? -> bool"),
]
print(f"{'Metot':<32}{'Op.':<5}{'Görevi'}")
print("-" * 72)
for metot, op, gorev in ozet:
    print(f"{metot:<32}{op:<5}{gorev}")

print()
karsilastirma = (
    ("Özellik",          "Liste",    "Demet",    "Sözlük",     "Küme"),
    ("Yazım",            "[1, 2]",   "(1, 2)",   "{'a': 1}",   "{1, 2}"),
    ("Sıralı",           "Evet",     "Evet",     "Evet",       "Hayır"),
    ("Erişim",           "İndeks",   "İndeks",   "Anahtar",    "Yok (in)"),
    ("Değiştirilebilir", "Evet",     "Hayır",    "Evet",       "Evet"),
    ("Tekrar",           "Olabilir", "Olabilir", "Anahtar X",  "Olamaz"),
    ("Metot sayısı",     "11",       "2",        "11",         "17"),
)
for s in karsilastirma:
    print(f"{s[0]:<18}{s[1]:<10}{s[2]:<10}{s[3]:<12}{s[4]}")
