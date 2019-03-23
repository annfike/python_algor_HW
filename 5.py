#1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия..
#Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести наименования предприятий, чья прибыль выше среднего и
#отдельно вывести наименования предприятий, чья прибыль ниже среднего.

companies = {}
n = int(input("Количество предприятий: "))
s = 0
for i in range(n):
    name = input(str(i+1) + "-е предприятие: ")
    profit1 = int(input("Прибыль за 1 квартал: "))
    profit2 = int(input("Прибыль за 2 квартал: "))
    profit3 = int(input("Прибыль за 3 квартал: "))
    profit4 = int(input("Прибыль за 4 квартал: "))
    profit =  profit1 + profit2 + profit3 + profit4
    companies[name] = profit
    s += profit
 
avrg = s / n
print("Средяя прибыль: %.0f" % avrg)
print("Предприятия с прибылью выше средней:")
for i in companies:
    if companies[i] > avrg:
        print(i)
print("Предприятия с прибылью ниже средней:")
for i in companies:
    if companies[i] < avrg:
        print(i)
print(companies)

# С импользованием collections (если честно - разницы не поняла)
import collections
companies = collections.defaultdict(list)
n = int(input("Количество предприятий: "))
s = 0
for i in range(n):
    name = input(str(i+1) + "-е предприятие: ")
    profit1 = int(input("Прибыль за 1 квартал: "))
    profit2 = int(input("Прибыль за 2 квартал: "))
    profit3 = int(input("Прибыль за 3 квартал: "))
    profit4 = int(input("Прибыль за 4 квартал: "))
    profit =  profit1 + profit2 + profit3 + profit4
    companies[name] = profit
    s += profit

print(companies)
avrg = s / n
print("Средяя прибыль: %.0f" % avrg)
print("Предприятия с прибылью выше средней:")
for i in companies:
    if companies[i] > avrg:
        print(i)
print("Предприятия с прибылью ниже средней:")
for i in companies:
    if companies[i] < avrg:
        print(i)



#2. Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как массив, элементы которого это цифры числа.
#Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

# 1. решение с использванием ресурсов Питона без массивов

a = 'A2' #input("Введите 1-е число ")
b = 'C4F' #input("Введите 2-е число ")
suma = hex(int(a,16) + int(b,16))
mult = hex(int(a,16) * int(b,16))
print("Сумма:", list(suma[2:]))
print("Произведение:", list(mult[2:]))

# 2. Решение с массивами (пока только сложение)
# Дмитрий, посмотрите, пожалуйста!!!  на это ужасное нагромождение, которое, тем не менее, работает:)) Как оптимизировать??

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
        
print(ss)



