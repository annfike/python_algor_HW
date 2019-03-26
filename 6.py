import sys
#Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков. Проанализировать результат и
#определить программы с наиболее эффективным использованием памяти.

'''
#2. Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как массив, элементы которого это цифры числа.
#Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

# 1. решение с использванием ресурсов Питона без массивов

a = 'A2' #input("Введите 1-е число ")
b = 'C4F' #input("Введите 2-е число ")
suma = hex(int(a,16) + int(b,16))
mult = hex(int(a,16) * int(b,16))
#print("Сумма:", list(suma[2:]))
#print("Произведение:", list(mult[2:]))

print(sys.getrefcount(a))
print(sys.getrefcount(suma))

# 2. Решение с массивами (пока только сложение)

d = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
a = 'A2' #input("Введите число ")
b = 'C4F' #input("Введите число ")
a = a.upper()
b = b.upper()
a = list(a)
b = list(b)
a.reverse()
b.reverse()

# делаем списки одной длины
if len(a) > len(b):
    while len(a) != len(b):
        b.append(0)
else:
    while len(a) != len(b):
        a.append(0)

# заменяем буквы цифрами
aa = []
for i in a:
    for k, val in d.items():
        if i == k:
            i = val
    aa.append(i)
bb = []
for i in b:
    for k, val in d.items():
        if i == k:
            i = val
    bb.append(i)

# складываем "столбиком"
m = 0
s = []
for i in range(len(aa)):
    a = int(aa[i])
    b = int(bb[i])
    c = a + b + m
    if c > 16:
        c = c - 16
        m = 1
    else:
        m = 0
    s.append(c)

# заменяем цифры буквами
ss = []
for i in s:
    for k, val in d.items():
        if i == val:
            i = k
    ss.append(i)
ss.reverse()
        
#print(ss)
print(sys.getrefcount(a))
print(sys.getrefcount(ss))
---------------------------------------------------------------------------------------------------------------------
результат:
в решении 1 - a=3, сумма=2
в решении 2 - a=979(откуда столько???), сумма=2
питон версия 3,7, система 64-разрядная
'''  

#2. Создать пользовательский класс данных (или использовать) один из классов, реализованных в курсе Python.Основы. Реализовать класс с применением слотов
#и обычным способом. Для объекта обычного класса проверить отображение словаря атрибутов. Сравнить, сколько выделяется памяти для хранения атрибутов обоих классов.
from pympler import asizeof

class Student:
    def __init__ (self, name, surname, class_room):
        self.name = name
        self.surname = surname
        self.class_room = class_room
    def get_full_name(self):
        return self.name + ' ' + self.surname
student1 = Student("Александр", "Иванов", "5 А")

class Student_slot:
    __slots__ = ['name', 'surname', 'class_room']
    def __init__ (self, name, surname, class_room):
        self.name = name
        self.surname = surname
        self.class_room = class_room
    def get_full_name(self):
        return self.name + ' ' + self.surname
student2 = Student_slot("Александр", "Иванов", "5 А")

print(asizeof.asizeof(student1)) #368
print(asizeof.asizeof(student2)) #200


