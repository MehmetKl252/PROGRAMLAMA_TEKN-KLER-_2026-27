# -*- coding: utf-8 -*-
# =====================================================
# PYTHON - print() VE STRING UYGULAMALARI
# Seviyeler: ORTA (6) | İLERİ (6)
# =====================================================

import time  # İlerleme çubuğu için bekleme

# =====================================================
# ORTA SEVİYE
# =====================================================

# --- O1: print() parametreleri: sep ve end ---
def o1_sep_end():
    print("Python", "Java", "C++", sep=" | ")      # Öğeler arasına " | " koy
    print("Tarih:", end=" ")                       # Satır sonu yerine boşluk
    print("02", "11", "2026", sep=".")             # 02.11.2026
    print("A", "B", "C", sep="")                   # Bitişik: ABC

# --- O2: f-string ile biçimlendirme ---
def o2_fstring():
    ad, not_, oran, tutar = "Ayşe", 87.456, 0.8537, 1234567.891
    print(f"Öğrenci: {ad}")
    print(f"Not (2 basamak): {not_:.2f}")          # 87.46
    print(f"Başarı oranı: {oran:.1%}")             # 85.4%
    print(f"Tutar: {tutar:,.2f} TL")               # Binlik ayraçlı
    print(f"Sayı (8 hane, sıfırlı): {42:08d}")     # 00000042

# --- O3: Kaçış karakterleri, ham string, çok satırlı metin ---
def o3_kacis():
    print("Ad\tSoyad\tYaş")                        # \t = sekme
    print("Satır 1\nSatır 2")                      # \n = alt satır
    print("Ali \"merhaba\" dedi")                  # \" = tırnak
    print(r"C:\yeni\test")                         # r"" = ham string, \ olduğu gibi
    print("""Bu çok satırlı
bir metindir.""")                                  # Üç tırnak = çok satır

# --- O4: Hizalı tablo (ljust, rjust, center) ---
def o4_tablo():
    print("TABLO".center(30, "="))                 # Ortala, kenarları = ile doldur
    veriler = [("Elma", 12.5), ("Armut", 8.75), ("Muz", 30)]
    for ad, fiyat in veriler:
        print(ad.ljust(10, ".") + f"{fiyat:>8.2f}")  # Sola yasla + sağa yasla
    print("=" * 30)

# --- O5: Dilimleme (slicing) ile string oynamaları ---
def o5_dilimleme():
    s = "Programlama"
    print(s[0], s[-1])                             # İlk ve son harf: P a
    print(s[0:4])                                  # İlk 4 harf: Prog
    print(s[::-1])                                 # Ters: amalmargorP
    print(s[::2])                                  # 2'şer atla: Pormlm
    print(len(s), "harf")                          # Uzunluk

# --- O6: Sık kullanılan string metotları ---
def o6_metotlar():
    m = "  Python Öğreniyorum  "
    print(f"[{m.strip()}]")                        # Baştaki/sondaki boşluğu sil
    print(m.strip().upper())                       # Büyük harf
    print(m.replace("Python", "Java"))             # Değiştir
    print(m.split())                               # Kelimelere böl -> liste
    print("-".join(["a", "b", "c"]))               # Listeyi birleştir: a-b-c
    print(m.count("o"), "tane 'o'")                # Harf say
    print(m.strip().startswith("Py"))              # True

# =====================================================
# İLERİ SEVİYE
# =====================================================

# --- I1: Makbuz/fatura çıktısı (hizalama + toplam) ---
def i1_makbuz():
    urunler = [("Kalem", 3, 12.5), ("Defter", 2, 45.0), ("Silgi", 5, 4.75)]
    print("MAKBUZ".center(40, "*"))
    print(f"{'Ürün':<12}{'Adet':>5}{'Fiyat':>10}{'Tutar':>10}")  # Başlık
    print("-" * 40)
    genel = 0
    for ad, adet, fiyat in urunler:
        tutar = adet * fiyat
        genel += tutar
        print(f"{ad:<12}{adet:>5}{fiyat:>10.2f}{tutar:>10.2f}")
    print("-" * 40)
    print(f"{'GENEL TOPLAM':<27}{genel:>13.2f}")

# --- I2: İlerleme çubuğu (end="\r" ve flush) ---
def i2_ilerleme():
    toplam = 20
    for i in range(toplam + 1):
        dolu = "█" * i                              # Dolu kısım
        bos = "░" * (toplam - i)                    # Boş kısım
        # \r = satır başına dön, aynı satırın üstüne yaz
        print(f"\r[{dolu}{bos}] %{i * 100 // toplam}", end="", flush=True)
        time.sleep(0.03)
    print()                                         # Bitince alt satıra geç

# --- I3: Türkçe karakter sorunu: İ/I dönüşümü ---
def tr_kucuk(s):
    # Python'un lower()'ı "I" -> "i" yapar, Türkçede "I" -> "ı" olmalı
    return s.replace("I", "ı").replace("İ", "i").lower()

def tr_buyuk(s):
    return s.replace("i", "İ").replace("ı", "I").upper()

def i3_turkce():
    k = "ISPARTA İZMİR"
    print("Hatalı :", k.lower())                    # i̇ işaretli hatalı çıktı olabilir
    print("Doğru  :", tr_kucuk(k))                  # ısparta izmir
    print("Büyük  :", tr_buyuk("ışık iğne"))        # IŞIK İĞNE

# --- I4: Sezar şifreleme (Türk alfabesiyle) ---
def sezar(metin, kaydir):
    alfabe = "abcçdefgğhıijklmnoöprsştuüvyz"         # 29 harf
    sonuc = ""
    for h in tr_kucuk(metin):
        if h in alfabe:
            yeni = (alfabe.index(h) + kaydir) % len(alfabe)  # Dairesel kaydır
            sonuc += alfabe[yeni]
        else:
            sonuc += h                               # Harf değilse aynen bırak
    return sonuc

def i4_sezar():
    sifreli = sezar("merhaba dünya", 3)
    print("Şifreli :", sifreli)
    print("Çözülmüş:", sezar(sifreli, -3))           # Ters kaydırma = çözme

# --- I5: Metin analiz raporu ---
def i5_analiz():
    metin = "Python öğrenmek eğlencelidir. Python ile algoritma öğrenmek kolaydır."
    temiz = "".join(h if h.isalnum() or h == " " else "" for h in metin)  # Noktalamayı at
    kelimeler = tr_kucuk(temiz).split()
    sayac = {}
    for k in kelimeler:
        sayac[k] = sayac.get(k, 0) + 1               # Kelime frekansı
    en_uzun = max(kelimeler, key=len)
    en_sik = max(sayac, key=sayac.get)
    print("RAPOR".center(30, "-"))
    print(f"{'Karakter':<16}: {len(metin)}")
    print(f"{'Kelime':<16}: {len(kelimeler)}")
    print(f"{'Benzersiz kelime':<16}: {len(sayac)}")
    print(f"{'En uzun kelime':<16}: {en_uzun} ({len(en_uzun)} harf)")
    print(f"{'En sık kelime':<16}: {en_sik} ({sayac[en_sik]} kez)")

# --- I6: ASCII sanat: piramit ve elmas (string çarpımı + center) ---
def i6_sekiller():
    n = 5
    print("PİRAMİT")
    for i in range(1, n + 1):
        print(("*" * (2 * i - 1)).center(2 * n - 1))  # Tek sayıda yıldız, ortalı
    print("ELMAS")
    for i in list(range(1, n + 1)) + list(range(n - 1, 0, -1)):
        print(("*" * (2 * i - 1)).center(2 * n - 1))  # Önce büyür, sonra küçülür

# =====================================================
# ÇALIŞTIR
# =====================================================
if __name__ == "__main__":
    bolumler = [
        ("ORTA", [o1_sep_end, o2_fstring, o3_kacis,
                  o4_tablo, o5_dilimleme, o6_metotlar]),
        ("İLERİ", [i1_makbuz, i2_ilerleme, i3_turkce,
                   i4_sezar, i5_analiz, i6_sekiller]),
    ]
    for baslik, fonksiyonlar in bolumler:
        print(f"\n===== {baslik} SEVİYE =====")
        for f in fonksiyonlar:
            print(f"\n--- {f.__name__} ---")
            f()
