# --- print: ekrana yazdırma ---
x = 5
y = 2
print("v=", 3, "cm :", x, ",", y + 4)   # değer, değişken ve ifade birlikte yazılır

# --- print seçenekleri ---
print("a", "b", "c", sep="-")           # ayırıcı: a-b-c (varsayılan boşluk)
print("Merhaba", end=" ")               # satır sonu yerine boşluk koyar
print("Dünya")                          # aynı satırda devam eder

# --- input: klavyeden okuma ---
s = input("Bir sayı girin: ")           # input HER ZAMAN string döndürür
sayi = int(s)                           # kullanmadan önce sayıya çevir
print("Sayının 2 katı:", sayi * 2)

# --- format: biçimlendirme (kağıttaki örnekler) ---
print("{:+2.3f}".format(45.72793))      # +45.728  (işaretli, 3 ondalık)
print("{1:>10s}".format(8, "toto"))     # '      toto' (sağa yaslı, 10 karakter)
print("{x!r}".format(x="I'm"))          # "I'm" (r = olduğu gibi gösterim)
print("modele{} {} {}".format(x, y, 7)) # {} yerlerine sırayla değer girer