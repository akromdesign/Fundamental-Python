# Strings

# Contoh penggunaan string
s1 = "Halo, dunia!"
s2 = 'Ini adalah contoh string.'
s3 = """Ini adalah string
dengan beberapa baris."""

# Menampilkan string
print(s1)  # Output: Halo, dunia!
print(s2)  # Output: Ini adalah contoh string.
print(s3)  # Output:
            # Ini adalah string
            # dengan beberapa baris.

# Menggabungkan string
nama_depan = "John"
nama_belakang = "Doe"
nama_lengkap = nama_depan + " " + nama_belakang
print(nama_lengkap)  # Output: John Doe

# Mengakses karakter dalam string
s = "Python"
print(s[0])  # Output: P
print(s[2])  # Output: t

# Mengganti karakter dalam string
s = "Hello, World!"
s = s[:5] + "Python"
print(s)  # Output: HelloPython

# Menghitung panjang string
s = "Ini adalah contoh string."
panjang = len(s)
print(panjang)  # Output: 24

# Memeriksa keanggotaan karakter dalam string
s = "Python"
print('y' in s)  # Output: True
print('z' in s)  # Output: False

# Memisahkan string menjadi list
s = "Halo, dunia!"
kata = s.split(",")
print(kata)  # Output: ['Halo', ' dunia!']

# Menggabungkan list menjadi string
kata = ['Halo', 'dunia!']
s = " ".join(kata)
print(s)  # Output: Halo dunia!

# Mengubah string menjadi huruf besar atau kecil
s = "Ini Adalah Contoh String."
s_upper = s.upper()
s_lower = s.lower()
print(s_upper)  # Output: INI ADALAH CONTOH STRING.
print(s_lower)  # Output: ini adalah contoh string.

# Memformat string
nama = "John"
usia = 25
pesan = "Halo, nama saya {} dan saya berusia {} tahun.".format(nama, usia)
print(pesan)  # Output: Halo, nama saya John dan saya berusia 25 tahun.