# Class and Objects

# Contoh kelas sederhana
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hello, my name is", self.name)

# Membuat objek dari kelas Person
person1 = Person("John", 25)
person2 = Person("Sarah", 30)

# Memanggil metode pada objek
person1.greet()  # Output: Hello, my name is John
person2.greet()  # Output: Hello, my name is Sarah

# Mengakses atribut pada objek
print(person1.name)  # Output: John
print(person2.age)  # Output: 30

# Contoh kelas dengan pewarisan (inheritance)
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def study(self):
        print(self.name, "is studying")

# Membuat objek dari kelas Student
student1 = Student("Michael", 20, "12345")
student2 = Student("Emily", 22, "54321")

# Memanggil metode pada objek
student1.greet()  # Output: Hello, my name is Michael
student2.study()  # Output: Emily is studying

# Mengakses atribut pada objek
print(student1.student_id)  # Output: 12345
print(student2.age)  # Output: 22