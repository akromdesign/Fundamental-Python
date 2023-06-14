# List (Daftar)
fruits = ["apel", "jeruk", "pisang"]

# Mengakses elemen dalam list
print(fruits[0])  # Output: apel
print(fruits[1])  # Output: jeruk

# Mengubah elemen dalam list
fruits[2] = "anggur"
print(fruits)  # Output: ["apel", "jeruk", "anggur"]

# Menambahkan elemen ke dalam list
fruits.append("mangga")
print(fruits)  # Output: ["apel", "jeruk", "anggur", "mangga"]

# Menghapus elemen dari list
fruits.remove("jeruk")
print(fruits)  # Output: ["apel", "anggur", "mangga"]

# Tuple
person = ("John", 25, "New York")

# Mengakses elemen dalam tuple
print(person[0])  # Output: John
print(person[1])  # Output: 25

# Mengubah nilai elemen dalam tuple tidak bisa dilakukan
# person[1] = 30  # Akan menghasilkan error

# Menampilkan semua nilai dalam tuple
for item in person:
    print(item)

# Set
numbers = {1, 2, 3, 4, 5}

# Menambahkan elemen ke dalam set
numbers.add(6)
print(numbers)  # Output: {1, 2, 3, 4, 5, 6}

# Menghapus elemen dari set
numbers.remove(4)
print(numbers)  # Output: {1, 2, 3, 5, 6}

# Operasi matematika pada set
set1 = {1, 2, 3}
set2 = {3, 4, 5}

union_set = set1.union(set2)
print(union_set)  # Output: {1, 2, 3, 4, 5}

intersection_set = set1.intersection(set2)
print(intersection_set)  # Output: {3}

difference_set = set1.difference(set2)
print(difference_set)  # Output: {1, 2}

# Dictionary
person = {"nama": "John", "usia": 25, "kota": "New York"}

# Mengakses nilai dalam dictionary
print(person["nama"])  # Output: John
print(person["usia"])  # Output: 25

# Mengubah nilai dalam dictionary
person["usia"] = 30
print(person)  # Output: {"nama": "John", "usia": 30, "kota": "New York"}

# Menambahkan pasangan kunci-nilai ke dalam dictionary
person["pekerjaan"] = "Insinyur"
print(person)  # Output: {"nama": "John", "usia": 30, "kota": "New York", "pekerjaan": "Insinyur"}

# Menghapus pasangan kunci-nilai dari dictionary
del person["kota"]
print(person)  # Output: {"nama": "John", "usia": 30, "pekerjaan": "Insinyur"}