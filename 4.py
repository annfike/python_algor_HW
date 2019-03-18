import timeit
import cProfile

#3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран. Например, если введено число 3486, то надо вывести число 6843.
def reverse1(x):
#    x = int(input('Введите число '))
    y = 0
    while x > 0:
        y = y * 10 + x % 10
        x = x // 10
    return y

x = 3486
print(reverse1(x))
#print(timeit.timeit('reverse1(x)', setup = 'from __main__ import reverse1, x'))

# Решение с рекурсией:
def recursion(a): 
    if a > 0:
        return str(a % 10) + str(recursion(a // 10))
    if a == 0:
        return ' '

a = 3486
print(recursion(a))
#print(timeit.timeit('recursion(a)', setup = 'from __main__ import recursion, a'))

# скорость решения без рекурсии - 1.138550785, с рекурсией - 3.668927761
'''
cProfile.run('recursion(a)')

         8 function calls (4 primitive calls) in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
      5/1    0.000    0.000    0.000    0.000 3.py:18(recursion)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

'''

#Написать два алгоритма нахождения i-го по счёту простого числа. 2 3 5 7 11 13 17 19 23 29 31
#Без использования «Решета Эратосфена»;

# k-ое простое не превосходит 1,5 k ln( k ) при k > 1:
import math
n1=13
def simple(n1):
#    n1 = int(input('Введите число '))
    n = int(1.5 * n1 * math.log(n1))
    lst = []
    for i in range(2, n+1):
        for j in lst:
            if i % j == 0:
                break
        else:
            lst.append(i)
        if len(lst) >= n:
            break
    print(lst)
    print('{}-ое по счёту простое число - {}'.format(n1, lst[n1-1]))
simple(int(input('Введите число ')))

#Используя алгоритм «Решето Эратосфена»
def simple1(n1):
#    n1 = int(input("n= "))
    n = int(1.5 * n1 * math.log(n1))
    a = [0] * n 
    for i in range(n):
        a[i] = i
    a[1] = 0
    m = 2
    while m < n:
        if a[m] != 0:
            j = m * 2
            while j < n:
                a[j] = 0
                j = j + m
        m += 1
    lst = []
    for i in a:
        if i != 0:
            lst.append(i)
    print(lst)
    print('{}-ое по счёту простое число - {}'.format(n1, lst[n1-1]))
simple1(int(input('Введите число ')))

#print(timeit.timeit('simple(n1)', setup = 'from __main__ import simple, n1')) #вариант без решета - 26.380455544
#print(timeit.timeit('simple1(n1)', setup = 'from __main__ import simple1, n1')) #вариант с решетом - 26.293425481
cProfile.run('simple(n1)')
cProfile.run('simple1(n1)')

