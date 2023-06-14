# Loop Statements

# Contoh penggunaan perulangan dengan while
i = 1

while i <= 5:
    print(i)
    i += 1

# Contoh penggunaan perulangan dengan for
fruits = ["apel", "jeruk", "pisang"]

for fruit in fruits:
    print(fruit)

# Contoh penggunaan perulangan dengan range
for i in range(1, 6):
    print(i)

# Contoh penggunaan perulangan dengan range dan langkah
for i in range(0, 10, 2):
    print(i)

# Contoh penggunaan pernyataan break
for i in range(1, 6):
    if i == 4:
        break
    print(i)

# Contoh penggunaan pernyataan continue
for i in range(1, 6):
    if i == 3:
        continue
    print(i)

# Contoh penggunaan pernyataan else dalam perulangan
for i in range(1, 6):
    print(i)
else:
    print("Perulangan selesai.")

# Contoh penggunaan pernyataan nested loop
for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)

# Contoh penggunaan pernyataan pass
for i in range(1, 6):
    pass  # Tidak melakukan apa-apa

# Contoh penggunaan perulangan dengan while dan pernyataan else
i = 1

while i <= 5:
    print(i)
    i += 1
else:
    print("Perulangan selesai.")