# -*- coding: utf-8 -*-
"""
PYTHON'DA TEMEL KAVRAMLAR VE VERİ TİPLERİ
==========================================
Değişken : Bir değeri bellekte saklamak için kullanılan İSİMLİ kutu.
           Python'da değişkenin tipi belirtilmez; atanan DEĞERE göre otomatik
           belirlenir (dinamik tipleme).

Temel veri tipleri:
  int   : Tam sayılar               -> 5, -12, 0, 1_000_000
  float : Ondalıklı sayılar         -> 3.14, -0.5, 2.0, 1e6
  str   : Metin (karakter dizisi)   -> "Merhaba", 'Python', "123"
  bool  : Mantıksal değer           -> True, False
  (None : "Değer yok" anlamına gelen özel değer -> NoneType)

Temel operatörler:
  Aritmetik    : +  -  *  /  //  %  **
  Atama        : =  +=  -=  *=  /=  //=  %=  **=
  Karşılaştırma: ==  !=  >  <  >=  <=
  Mantıksal    : and  or  not
  Üyelik       : in  not in
  Kimlik       : is  is not

Bu dosyayı çalıştırmak için:  python python_temel_kavramlar.py
"""


def baslik(metin):
    print("\n" + "=" * 60)
    print(metin)
    print("=" * 60)


# ============================================================
# BÖLÜM 1: DEĞİŞKENLER
# ============================================================

baslik("1. DEĞİŞKEN OLUŞTURMA VE ATAMA")

# Örnek 1: Farklı tipte değişkenler
ad = "Ali"              # str
yas = 20                # int
boy = 1.78              # float
ogrenci_mi = True       # bool
print("Ad:", ad, "| Yaş:", yas, "| Boy:", boy, "| Öğrenci mi:", ogrenci_mi)

# Örnek 2: Değişkenin değeri sonradan değiştirilebilir
bakiye = 1000
print("İlk bakiye     :", bakiye)
bakiye = 1500
print("Yeni bakiye    :", bakiye)

# Örnek 3: Dinamik tipleme - aynı değişkene farklı tipte değer atanabilir
x = 10
print("x =", x, "->", type(x).__name__)
x = "on"
print("x =", x, "->", type(x).__name__)

# Örnek 4: Değişkeni başka değişkenden türetme
fiyat = 250
adet = 4
toplam = fiyat * adet
print("Toplam tutar   :", toplam)


baslik("2. ÇOKLU ATAMA VE DEĞER DEĞİŞTİRME")

# Örnek 1: Tek satırda birden fazla değişkene atama
a, b, c = 1, 2, 3
print("a, b, c        :", a, b, c)

# Örnek 2: Aynı değeri birden fazla değişkene atama
x = y = z = 0
print("x, y, z        :", x, y, z)

# Örnek 3: İki değişkenin değerini yer değiştirme (swap)
sol, sag = "elma", "armut"
sol, sag = sag, sol
print("Swap sonrası   :", sol, sag)

# Örnek 4: Geçici değişkenle swap (diğer dillerdeki yöntem)
p, q = 5, 9
gecici = p
p = q
q = gecici
print("Geçici ile     :", p, q)


baslik("3. DEĞİŞKEN ADLANDIRMA KURALLARI")

# Örnek 1: Geçerli isimler
ogrenci_adi = "Buse"          # snake_case (Python'da önerilen)
ogrenciAdi = "Buse"           # camelCase (çalışır ama Python geleneği değil)
_gizli = 42                   # alt çizgiyle başlayabilir
sayi2 = 7                     # sonda rakam olabilir
MAKS_DENEME = 3               # SABİTLER büyük harfle yazılır (gelenek)
print("Geçerli isimler tanımlandı:", ogrenci_adi, _gizli, sayi2, MAKS_DENEME)

# Örnek 2: Geçersiz isimler -> SyntaxError
for kod in ["2sayi = 5", "ogrenci adi = 'x'", "class = 1", "fiyat-tl = 10"]:
    try:
        exec(kod)
    except SyntaxError:
        print(f"Geçersiz: {kod!r}")

# Örnek 3: Büyük/küçük harf duyarlılığı
Sehir = "Ankara"
sehir = "İzmir"
print("Sehir ve sehir FARKLI değişkenlerdir:", Sehir, "/", sehir)

# Örnek 4: Python'un ayrılmış kelimeleri (değişken adı olamaz)
import keyword
print("Ayrılmış kelime sayısı:", len(keyword.kwlist))
print("Bazıları       :", keyword.kwlist[:10])


baslik("4. type(), id() VE isinstance()")

# Örnek 1: type() ile tip öğrenme
for deger in [42, 3.14, "metin", True, None]:
    print(f"{deger!r:<8} -> {type(deger)}")

# Örnek 2: isinstance() ile tip kontrolü
puan = 85.5
print("puan float mı? :", isinstance(puan, float))
print("puan sayı mı?  :", isinstance(puan, (int, float)))

# Örnek 3: id() -> nesnenin bellekteki kimliği
a = 1000
b = a
print("a ve b aynı nesne mi?:", id(a) == id(b))


# ============================================================
# BÖLÜM 2: SAYISAL TİPLER (int, float)
# ============================================================

baslik("5. int (TAM SAYI)")

# Örnek 1: Pozitif, negatif ve sıfır
sicaklik = -5
nufus = 15_600_000           # _ okunabilirlik için, değeri etkilemez
sifir = 0
print("Sıcaklık       :", sicaklik)
print("Nüfus          :", nufus)

# Örnek 2: Python'da int'in sınırı yoktur (çok büyük sayılar)
buyuk = 2 ** 100
print("2^100          :", buyuk)

# Örnek 3: Farklı sayı tabanları
print("İkilik 0b1010  :", 0b1010)
print("Onaltılık 0xFF :", 0xFF)
print("bin(10)        :", bin(10), "| hex(255):", hex(255))


baslik("6. float (ONDALIKLI SAYI)")

# Örnek 1: Ondalık sayılar (ondalık ayırıcı NOKTA'dır, virgül değil!)
pi = 3.14159
fiyat = 305.75
print("pi             :", pi)
print("Fiyat          :", fiyat)

# Örnek 2: Bilimsel gösterim
avogadro = 6.022e23
cok_kucuk = 1.5e-4
print("6.022e23       :", avogadro)
print("1.5e-4         :", cok_kucuk)

# Örnek 3 (DİKKAT): Ondalık sayılarda hassasiyet sorunu
print("0.1 + 0.2      :", 0.1 + 0.2)
print("round ile      :", round(0.1 + 0.2, 2))
from decimal import Decimal
print("Decimal ile    :", Decimal("0.1") + Decimal("0.2"), "-> para hesaplarında tercih edilir")

# Örnek 4: Bölme her zaman float döndürür
print("10 / 2         :", 10 / 2, type(10 / 2).__name__)


baslik("7. SAYILARLA KULLANILAN HAZIR FONKSİYONLAR")

# Örnek 1: abs, round, pow, divmod
print("abs(-7.5)      :", abs(-7.5))
print("round(3.14159, 2):", round(3.14159, 2))
print("round(2.5), round(3.5):", round(2.5), round(3.5), "-> en yakın ÇİFT sayıya yuvarlar")
print("pow(2, 10)     :", pow(2, 10))
print("divmod(17, 5)  :", divmod(17, 5), "-> (bölüm, kalan)")

# Örnek 2: max, min, sum
notlar = [72, 95, 58, 81]
print("max / min / sum:", max(notlar), min(notlar), sum(notlar))

# Örnek 3: math modülü
import math
print("math.sqrt(16)  :", math.sqrt(16))
print("math.ceil(4.1) :", math.ceil(4.1), "| math.floor(4.9):", math.floor(4.9))
print("math.pi        :", round(math.pi, 5))


# ============================================================
# BÖLÜM 3: METİN TİPİ (str)
# ============================================================

baslik("8. str OLUŞTURMA")

# Örnek 1: Tek, çift ve üç tırnak
s1 = 'Tek tırnak'
s2 = "Çift tırnak"
s3 = """Üç tırnak
birden fazla satır
yazmayı sağlar."""
print(s1, "|", s2)
print(s3)

# Örnek 2: Tırnak içinde tırnak ve kaçış karakterleri
print("Ali'nin kitabı")
print('O "Merhaba" dedi.')
print("Satır 1\nSatır 2")          # \n: yeni satır
print("Ad:\tAli")                  # \t: tab
print("Yol: C:\\Kullanicilar")     # \\: ters eğik çizgi
print(r"Ham metin: C:\yeni\tablo") # r"...": kaçış karakterleri işlenmez

# Örnek 3: Rakamlardan oluşan metin sayı DEĞİLDİR
print('"5" + "3"      :', "5" + "3")
print("5 + 3          :", 5 + 3)


baslik("9. str İNDEKSLEME VE DİLİMLEME")

kelime = "PORTFÖY"
#         0123456
# negatif -7....-1

# Örnek 1: İndeksleme
print("İlk harf       :", kelime[0])
print("Son harf       :", kelime[-1])
print("Uzunluk        :", len(kelime))

# Örnek 2: Dilimleme
print("[0:4]          :", kelime[0:4])
print("[4:]           :", kelime[4:])
print("[::-1] (ters)  :", kelime[::-1])

# Örnek 3 (DİKKAT): str DEĞİŞTİRİLEMEZ (immutable)
try:
    kelime[0] = "p"
except TypeError as h:
    print("TypeError      :", h)
yeni = "p" + kelime[1:]
print("Yeni metin     :", yeni)


baslik("10. str OPERATÖRLERİ")

# Örnek 1: + birleştirme, * tekrarlama
ad, soyad = "Ayşe", "Yılmaz"
print("Birleştirme    :", ad + " " + soyad)
print("Tekrarlama     :", "-" * 20)

# Örnek 2: in ile arama
cumle = "Python ile finans analizi"
print("'finans' var mı?:", "finans" in cumle)
print("'Java' yok mu?  :", "Java" not in cumle)

# Örnek 3 (DİKKAT): str ile sayı doğrudan birleştirilemez
yas = 20
try:
    print("Yaşım " + yas)
except TypeError as h:
    print("TypeError      :", h)
print("Doğru          :", "Yaşım " + str(yas))


baslik("11. SIK KULLANILAN str METOTLARI")

# upper / lower / title / capitalize
# Örnek 1
print("upper()        :", "python".upper())
print("lower()        :", "PYTHON".lower())
# Örnek 2
print("title()        :", "portföy yönetimi dersi".title())
print("capitalize()   :", "portföy yönetimi".capitalize())

# strip / lstrip / rstrip
# Örnek 1: Baştaki ve sondaki boşlukları silme
girdi = "   ali@mail.com   "
print("strip()        :", repr(girdi.strip()))
# Örnek 2: Belirli karakterleri silme
print("strip('*')     :", "***İndirim***".strip("*"))
print("rstrip('TL')   :", "250TL".rstrip("TL"))

# replace
# Örnek 1
print("replace()      :", "Merhaba Dünya".replace("Dünya", "Python"))
# Örnek 2: Türkçe fiyat biçimini sayıya çevirme
tr_fiyat = "1.250,75"
print("TR -> float    :", float(tr_fiyat.replace(".", "").replace(",", ".")))

# split / join
# Örnek 1: Metni parçalara ayırma
print("split()        :", "elma armut muz".split())
print("split(';')     :", "THYAO;305.75;100".split(";"))
# Örnek 2: Listeyi birleştirme
print("join()         :", " - ".join(["Ali", "Buse", "Cem"]))
print("join() boşluksuz:", "".join(["P", "y", "t", "h", "o", "n"]))

# find / index / count
# Örnek 1
metin = "borsa borsa borsa"
print("find('borsa')  :", metin.find("borsa"))
print("find('hisse')  :", metin.find("hisse"), "-> bulunamazsa -1")
# Örnek 2
print("count('borsa') :", metin.count("borsa"))
print("count('a')     :", "Ankara".lower().count("a"))

# startswith / endswith
# Örnek 1
dosya = "rapor_2026.pdf"
print("endswith('.pdf'):", dosya.endswith(".pdf"))
# Örnek 2
print("startswith('TR'):", "TR12 0006 4000".startswith("TR"))

# isdigit / isalpha / isalnum / isspace
# Örnek 1
for s in ["123", "abc", "abc123", "12.5", "   "]:
    print(f"{s!r:<9} digit={s.isdigit()!s:<5} alpha={s.isalpha()!s:<5} "
          f"alnum={s.isalnum()!s:<5} space={s.isspace()}")
# Örnek 2: Kullanıcı girişini kontrol etme
tc = "1234567890a"
print("Geçerli TC formatı mı?:", tc.isdigit() and len(tc) == 11)

# center / ljust / rjust / zfill
# Örnek 1
print("[" + "BAŞLIK".center(20) + "]")
print("[" + "sol".ljust(10) + "][" + "sağ".rjust(10) + "]")
# Örnek 2
print("zfill(5)       :", "42".zfill(5), "| sipariş no:", str(7).zfill(6))


baslik("12. f-string İLE BİÇİMLENDİRME")

ad, puan, fiyat, oran = "Ali", 87.456, 1250000, 0.0845

# Örnek 1: Değişken yerleştirme ve ifade hesaplama
print(f"Merhaba {ad}, puanın {puan}")
print(f"5 x 4 = {5 * 4}")
print(f"Büyük harf: {ad.upper()}")

# Örnek 2: Sayı biçimlendirme
print(f"2 ondalık     : {puan:.2f}")
print(f"Binlik ayırıcı: {fiyat:,}")
print(f"Binlik + ondalık: {fiyat:,.2f} TL")
print(f"Yüzde         : {oran:.2%}")

# Örnek 3: Hizalama (tablo yapmak için)
for h, f in [("THYAO", 305.75), ("ASELS", 61.4), ("BIMAS", 455)]:
    print(f"|{h:<8}|{f:>10.2f}|")

# Örnek 4: Hata ayıklama için = (Python 3.8+)
x = 42
print(f"{x = }")

# Örnek 5: Eski yöntemler (karşılaşırsan tanı)
print("format()       : {} {} yaşında".format("Buse", 22))
print("%% operatörü    : %s %d yaşında" % ("Cem", 25))


# ============================================================
# BÖLÜM 4: MANTIKSAL TİP (bool) VE None
# ============================================================

baslik("13. bool (True / False)")

# Örnek 1: Karşılaştırmalar bool üretir
yas = 20
resit = yas >= 18
print("resit          :", resit, type(resit).__name__)

# Örnek 2: bool aslında int'in alt türüdür (True=1, False=0)
print("True + True    :", True + True)
print("sum([True, False, True]):", sum([True, False, True]), "-> True'ları sayar")

# Örnek 3: Truthy / Falsy - bool() dönüşümü
for d in [0, 1, -3, 0.0, "", "a", " ", None, [], [0]]:
    print(f"bool({d!r:<5}) -> {bool(d)}")


baslik("14. None  ->  'Değer yok'")

# Örnek 1: Henüz değeri belli olmayan değişken
sonuc = None
print("sonuc          :", sonuc, type(sonuc).__name__)

# Örnek 2: None kontrolü 'is' ile yapılır
if sonuc is None:
    print("Henüz hesaplanmadı.")

# Örnek 3: return içermeyen fonksiyon None döndürür
def selam():
    print("  Selam!")
print("Dönüş          :", selam())


# ============================================================
# BÖLÜM 5: TİP DÖNÜŞÜMLERİ
# ============================================================

baslik("15. TİP DÖNÜŞÜMÜ (TYPE CASTING)")

# Örnek 1: str -> int / float
print('int("42")      :', int("42") + 8)
print('float("3.5")   :', float("3.5") * 2)
print('int(" 7 ")     :', int(" 7 "), "-> boşluklar sorun değil")

# Örnek 2: int / float -> str
print("str(100) + 'TL':", str(100) + " TL")
print("str(3.14)      :", repr(str(3.14)))

# Örnek 3: float -> int (aşağı doğru keser, yuvarlamaz!)
print("int(9.99)      :", int(9.99))
print("int(-9.99)     :", int(-9.99))
print("round(9.99)    :", round(9.99))

# Örnek 4: bool dönüşümleri
print("int(True)      :", int(True), "| bool(0):", bool(0), "| bool('False'):", bool("False"))

# Örnek 5: Hatalı dönüşümler -> ValueError
for deger in ["12.5", "abc", "1,5"]:
    try:
        print(f"int({deger!r}) ->", int(deger))
    except ValueError:
        print(f"int({deger!r}) -> ValueError")

# Örnek 6: Örtük (otomatik) dönüşüm: int + float = float
print("5 + 2.0        :", 5 + 2.0, type(5 + 2.0).__name__)

# Örnek 7: input() her zaman str döndürür
girdi = "25"                    # input("Yaşınız: ") ile gelmiş gibi
print("input tipi     :", type(girdi).__name__)
print("10 yıl sonra   :", int(girdi) + 10)


# ============================================================
# BÖLÜM 6: TEMEL OPERATÖRLER
# ============================================================

baslik("16. ARİTMETİK OPERATÖRLER")

a, b = 17, 5

# Örnek 1: Tüm aritmetik operatörler
print(f"{a} + {b}  =", a + b)
print(f"{a} - {b}  =", a - b)
print(f"{a} * {b}  =", a * b)
print(f"{a} / {b}  =", a / b, "  (bölme, her zaman float)")
print(f"{a} // {b} =", a // b, "    (tam bölme)")
print(f"{a} % {b}  =", a % b, "    (mod, kalan)")
print(f"{a} ** {b} =", a ** b, "(üs alma)")

# Örnek 2: % ve // ile pratik işlemler
sayi = 47
print("47 çift mi?    :", sayi % 2 == 0)
saniye = 3725
print(f"{saniye} sn = {saniye // 3600} sa {(saniye % 3600) // 60} dk {saniye % 60} sn")
print("1234'ün son basamağı:", 1234 % 10)

# Örnek 3: Negatif sayılarda // ve %
print("-17 // 5       :", -17 // 5, "-> aşağı (eksi sonsuza) yuvarlar")
print("-17 % 5        :", -17 % 5)

# Örnek 4: Sıfıra bölme
try:
    10 / 0
except ZeroDivisionError as h:
    print("ZeroDivisionError:", h)

# Örnek 5: Finansal hesaplama
anapara, faiz, yil = 10000, 0.40, 3
print(f"Basit faiz    : {anapara * faiz * yil:,.2f} TL")
print(f"Bileşik faiz  : {anapara * (1 + faiz) ** yil - anapara:,.2f} TL")


baslik("17. ATAMA OPERATÖRLERİ")

# Örnek 1: Kısaltılmış atamalar
x = 10
x += 5;  print("x += 5   ->", x)
x -= 3;  print("x -= 3   ->", x)
x *= 2;  print("x *= 2   ->", x)
x /= 4;  print("x /= 4   ->", x)
x //= 2; print("x //= 2  ->", x)
x **= 3; print("x **= 3  ->", x)
x %= 5;  print("x %= 5   ->", x)

# Örnek 2: Sayaç ve birikim
sayac, toplam = 0, 0
for fiyat in [120, 80, 45]:
    sayac += 1
    toplam += fiyat
print(f"{sayac} ürün, toplam {toplam} TL")

# Örnek 3: Metinde += ve *=
mesaj = "Merhaba"
mesaj += " Dünya"
print("str +=         :", mesaj)
cizgi = "="
cizgi *= 15
print("str *=         :", cizgi)


baslik("18. KARŞILAŞTIRMA OPERATÖRLERİ")

# Örnek 1: Sayılar
print("5 == 5.0       :", 5 == 5.0)
print("5 != 3         :", 5 != 3)
print("10 >= 10       :", 10 >= 10)

# Örnek 2: Metinler (alfabetik / Unicode sırası, büyük-küçük harf duyarlı)
print("'a' < 'b'      :", "a" < "b")
print("'Z' < 'a'      :", "Z" < "a", "-> büyük harfler önce gelir")
print("'Ali' == 'ali' :", "Ali" == "ali")

# Örnek 3: Zincirleme karşılaştırma
puan = 75
print("50 <= 75 < 85  :", 50 <= puan < 85)


baslik("19. MANTIKSAL OPERATÖRLER")

# Örnek 1: Doğruluk tablosu
print(f"{'A':<7}{'B':<7}{'A and B':<9}{'A or B':<8}{'not A'}")
for A in [True, False]:
    for B in [True, False]:
        print(f"{A!s:<7}{B!s:<7}{(A and B)!s:<9}{(A or B)!s:<8}{not A}")

# Örnek 2: Gerçek hayat koşulları
yas, gelir, borc_var = 25, 30000, False
print("Kredi uygun mu?:", yas >= 18 and gelir >= 20000 and not borc_var)

# Örnek 3: Kısa devre (short-circuit) - and/or değer döndürür
kullanici = ""
gosterilecek = kullanici or "Misafir"
print("or ile varsayılan:", gosterilecek)
liste = []
print("and ile güvenli erişim:", liste and liste[0])


baslik("20. ÜYELİK VE KİMLİK OPERATÖRLERİ")

# Örnek 1: in / not in
print("'a' in 'kalem' :", "a" in "kalem")
print("3 in [1, 2, 3] :", 3 in [1, 2, 3])
print("'x' not in 'abc':", "x" not in "abc")

# Örnek 2: is vs ==
liste1 = [1, 2, 3]
liste2 = [1, 2, 3]
liste3 = liste1
print("liste1 == liste2:", liste1 == liste2, "-> değerleri eşit")
print("liste1 is liste2:", liste1 is liste2, "-> farklı nesneler")
print("liste1 is liste3:", liste1 is liste3, "-> aynı nesne")


baslik("21. OPERATÖR ÖNCELİĞİ")

# Örnek 1: Matematikteki gibi: ** > * / // % > + -
print("2 + 3 * 4      :", 2 + 3 * 4)
print("(2 + 3) * 4    :", (2 + 3) * 4)
print("2 ** 3 ** 2    :", 2 ** 3 ** 2, "-> ** sağdan sola: 2**(3**2)")
print("-2 ** 2        :", -2 ** 2, "-> -(2**2)")

# Örnek 2: Karışık ifade
sonuc = 10 + 20 / 5 * 2 - 3 ** 2
print("10 + 20 / 5 * 2 - 3 ** 2 =", sonuc)

# Örnek 3: not > and > or
print("True or False and False:", True or False and False)

print("""
Öncelik sırası (yüksekten düşüğe):
  1) ()                  Parantez
  2) **                  Üs
  3) +x, -x              İşaret
  4) *  /  //  %         Çarpma, bölme
  5) +  -                Toplama, çıkarma
  6) == != > < >= <= in is   Karşılaştırma
  7) not
  8) and
  9) or
  İpucu: Emin değilsen PARANTEZ kullan.
""")


# ============================================================
# UYGULAMA
# ============================================================

baslik("UYGULAMA: Hisse Alım Hesaplayıcı")
# NOT: Değerler örnek amaçlıdır. Gerçek programda input() ile alınabilir.

# Girdiler (input() ile gelmiş gibi STRING)
girdi_hisse = "  thyao "
girdi_fiyat = "305,75"         # Türkçe ondalık virgül
girdi_butce = "50.000"         # Türkçe binlik nokta
KOMISYON_ORANI = 0.002         # sabit: binde 2

# 1) str temizleme ve dönüştürme
hisse = girdi_hisse.strip().upper()
fiyat = float(girdi_fiyat.replace(",", "."))
butce = int(girdi_butce.replace(".", ""))

# 2) Aritmetik işlemler
alinabilir_adet = int(butce // (fiyat * (1 + KOMISYON_ORANI)))
tutar = alinabilir_adet * fiyat
komisyon = tutar * KOMISYON_ORANI
kalan = butce - tutar - komisyon

# 3) Karşılaştırma ve mantıksal operatörler
yeterli_mi = alinabilir_adet > 0
buyuk_islem = tutar >= 25000 and yeterli_mi

# 4) f-string ile rapor
print(f"{'Hisse':<16}: {hisse}")
print(f"{'Fiyat':<16}: {fiyat:,.2f} TL")
print(f"{'Bütçe':<16}: {butce:,} TL")
print("-" * 36)
print(f"{'Alınabilir adet':<16}: {alinabilir_adet}")
print(f"{'İşlem tutarı':<16}: {tutar:,.2f} TL")
print(f"{'Komisyon':<16}: {komisyon:,.2f} TL ({KOMISYON_ORANI:.1%})")
print(f"{'Kalan nakit':<16}: {kalan:,.2f} TL")
print(f"{'Büyük işlem mi?':<16}: {buyuk_islem}")

print("\nDeğişken tipleri:")
for isim, deger in [("hisse", hisse), ("fiyat", fiyat), ("butce", butce),
                    ("alinabilir_adet", alinabilir_adet), ("buyuk_islem", buyuk_islem)]:
    print(f"  {isim:<16} -> {type(deger).__name__}")


baslik("ÖZET")
tipler = [
    ("int",   "Tam sayı",          "42, -7, 1_000",   "int('42')"),
    ("float", "Ondalıklı sayı",    "3.14, 1e6",       "float('3.5')"),
    ("str",   "Metin",             "'abc', \"Ali\"",  "str(100)"),
    ("bool",  "Mantıksal",         "True, False",     "bool(1)"),
    ("None",  "Değer yok",         "None",            "-"),
]
print(f"{'Tip':<7}{'Anlamı':<17}{'Örnek':<17}{'Dönüşüm'}")
print("-" * 60)
for t in tipler:
    print(f"{t[0]:<7}{t[1]:<17}{t[2]:<17}{t[3]}")

print()
operatorler = [
    ("Aritmetik",     "+  -  *  /  //  %  **"),
    ("Atama",         "=  +=  -=  *=  /=  //=  %=  **="),
    ("Karşılaştırma", "==  !=  >  <  >=  <="),
    ("Mantıksal",     "and  or  not"),
    ("Üyelik",        "in  not in"),
    ("Kimlik",        "is  is not"),
]
print(f"{'Operatör':<15}{'Semboller'}")
print("-" * 60)
for o, s in operatorler:
    print(f"{o:<15}{s}")
