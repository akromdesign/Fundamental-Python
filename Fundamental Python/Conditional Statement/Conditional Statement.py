# Conditional Statement

# Contoh penggunaan pernyataan if
x = 5

if x > 0:
    print("x adalah bilangan positif.")

# Contoh penggunaan pernyataan if-else
x = -2

if x > 0:
    print("x adalah bilangan positif.")
else:
    print("x adalah bilangan negatif.")

# Contoh penggunaan pernyataan if-elif-else
x = 0

if x > 0:
    print("x adalah bilangan positif.")
elif x < 0:
    print("x adalah bilangan negatif.")
else:
    print("x adalah nol.")

# Contoh penggunaan pernyataan bersarang
x = 10
y = 5

if x > 0:
    if y > 0:
        print("x dan y adalah bilangan positif.")
    else:
        print("x adalah bilangan positif, tetapi y tidak.")
else:
    print("x bukan bilangan positif.")

# Contoh penggunaan operator logika dalam pernyataan kondisional
x = 15

if x > 0 and x % 2 == 0:
    print("x adalah bilangan positif genap.")

# Contoh penggunaan pernyataan kondisional bersarang dengan operator logika
x = 25

if x > 0:
    if x % 2 == 0:
        print("x adalah bilangan positif genap.")
    else:
        print("x adalah bilangan positif ganjil.")
else:
    print("x bukan bilangan positif.")

# Contoh penggunaan pernyataan kondisional dengan operator ternary
x = 10
keterangan = "Bilangan genap" if x % 2 == 0 else "Bilangan ganjil"
print(keterangan)