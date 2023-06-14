# Function

# Contoh fungsi sederhana
def say_hello():
    print("Hello, world!")

# Memanggil fungsi
say_hello()  # Output: Hello, world!

# Contoh fungsi dengan parameter
def greet(name):
    print("Hello, " + name + "!")

# Memanggil fungsi dengan argumen
greet("John")  # Output: Hello, John!

# Contoh fungsi dengan nilai kembalian
def add_numbers(a, b):
    return a + b

# Memanggil fungsi dan menyimpan nilai kembalian
result = add_numbers(5, 3)
print(result)  # Output: 8

# Contoh fungsi dengan nilai kembalian multiple
def square_and_cube(x):
    square = x ** 2
    cube = x ** 3
    return square, cube

# Memanggil fungsi dan menyimpan nilai kembalian
squared, cubed = square_and_cube(4)
print(squared)  # Output: 16
print(cubed)  # Output: 64

# Contoh fungsi dengan argumen default
def greet_person(name, greeting="Hello"):
    print(greeting + ", " + name + "!")

# Memanggil fungsi dengan dan tanpa argumen
greet_person("John")  # Output: Hello, John!
greet_person("Sarah", "Hi")  # Output: Hi, Sarah!