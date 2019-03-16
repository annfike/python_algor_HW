#1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

a = [0]*8
for i in range(2, 100):
    for j in range(2, 10):
        if i % j == 0:
            a[j-2] = a[j-2] + 1

z = 2
for j in a:
    print("кратны", z, "-", j, "чисел")
    z += 1
        
#2. Во втором массиве сохранить индексы четных элементов первого массива. Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, то во второй массив надо
#заполнить значениями 1, 4, 5, 6 (или 0, 3, 4, 5 - если индексация начинается с нуля), т.к. именно в этих позициях первого массива стоят четные числа.

a = [8, 3, 15, 6, 4, 2]
b = []
for i in range(len(a)):
    if a[i] % 2 == 0:
        b.append(i)
print(b)

#или:
print( *(i for i in range(len(a)) if a[i] % 2 == 0))

#3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

lst = [8, 3, 15, 6, 4, 2]
maxel = max(lst)
max1 = lst.index(max(lst))
minel = min(lst)
min1 = lst.index(min(lst))
lst.remove(maxel)
lst.remove(minel)
lst.insert(max1, minel)
lst.insert(min1, maxel)
print(lst)

#4. Определить, какое число в массиве встречается чаще всего.

a = [8, 3, 15, 6, 4, 2, 2, 2, 6, 3]
n = a[0]
mv = 1
for i in range(len(a)):
    v = 1
    for j in range(i+1,len(a)):
        if a[i] == a[j]:
            v = v + 1
    if v > mv:
        mv = v
        n = a[i]
print(n, "встречается", mv, "раза")

# или:
lst = [8, 3, 15, 6, 4, 2, 2, 2, 6, 3]
mv = 1
for i in lst:
    a = (lst.count(i))
    if a > mv:
        mv = a
        n = i
print(n, "встречается", mv, "раза")    
        
#5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию (индекс) в массиве.

import random
lst = [random.randint(-20, 20) for _ in range(10)]
print(lst)
print(min(lst))
print(lst.index(min(lst)))

#6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами. Сами минимальный и максимальный элементы в сумму не включать.

lst = [8, 3, 15, 6, 4, 2]
max1 = lst.index(max(lst))
min1 = lst.index(min(lst))
if min1 > max1:
    min1, max1 = max1, min1
sum = 0
for i in range(min1+1, max1):
    sum += lst[i]
print(sum)


#7. В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между собой (оба являться минимальными), так и различаться.

import random
lst = [random.randint(0, 100) for _ in range(10)]
print(lst)
a = lst.pop(lst.index(min(lst)))
b = min(lst)
print(a, b)

#8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк. Программа должна вычислять сумму введенных элементов каждой строки
#и записывать ее в последнюю ячейку строки. В конце следует вывести полученную матрицу.

# ввод строк
a = []
for i in range(4):
    b = []
    k=input("Введите 4 цифры: ")
    b.append(k)
    s = 0
    for j in k:
        s = s + int(j)
    b.append(s)
    a.append(b)
for i in a:
    print(i)

#ввод цифр 
M = 5
a = []
for i in range(4):
    b = []
    s = 0
    print("Строка %d:" % (i+1))
    for j in range(M-1):
        k = int(input("Введите цифру "))
        s = s + k
        b.append(k)
    b.append(s)
    a.append(b)
for i in a:
    print(i)

#9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.

import random
M = 5
N = 4
a = []
for i in range(N):
    z = []
    for j in range(M):
        n = int(random.randint(1, 20))
        z.append(n)
        print("%3d" % n, end='')
    print()
    a.append(z)
print()
mx = 0
for j in range(M):
    mn = 20
    for i in range(N):
        if a[i][j] < mn:
            mn = a[i][j]
    if mn > mx:
        mx = mn
print("Максимальный среди минимальных: ", mx)
    





           
    
    
    
