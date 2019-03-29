#1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив, заданный случайными числами на промежутке [-100; 100).
#Выведите на экран исходный и отсортированный массивы. Сортировка должна быть реализована в виде функции. По возможности доработайте алгоритм (сделайте его умнее).

import timeit
import random

#вариант, когда цикл останавливается, если после первого прохода менять нечего
#orig_list = [1,1,1,1,1]
def bubble_sort(orig_list):
    n = 1
    s = 0
    while n < len(orig_list):
        for i in range(len(orig_list)-n):
            if orig_list[i] < orig_list[i+1]:
                orig_list[i],orig_list[i+1] = orig_list[i+1],orig_list[i]
            if orig_list[i] == orig_list[i+1]:
                s = s + 1
        n += 1
        if s == len(orig_list)-1:
            break
    return orig_list

orig_list = [random.randint(-100, 100) for _ in range(10)]
print(orig_list)
print(bubble_sort(orig_list))
# замеры
print(timeit.timeit("bubble_sort(orig_list)", \
    setup="from __main__ import bubble_sort, orig_list", number=1))


#2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на промежутке [0; 50).
#Выведите на экран исходный и отсортированный массивы.

def merge_sort(orig_list):
    if len(orig_list) > 1:
        center = len(orig_list) // 2
        left = orig_list[:center]
        right = orig_list[center:]

        merge_sort(left)
        merge_sort(right)

        i, j, k = 0, 0, 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                orig_list[k] = left[i]
                i += 1
            else:
                orig_list[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            orig_list[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            orig_list[k] = right[j]
            j += 1
            k += 1
        return orig_list

orig_list = [round(random.uniform(0, 50), 2) for _ in range(10)]
print(orig_list)
print(merge_sort(orig_list))
# замеры
print(timeit.timeit("merge_sort(orig_list)", \
    setup="from __main__ import merge_sort, orig_list", number=1))

#3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найдите в массиве медиану. Медианой называется элемент ряда, делящий его
#на две равные части: в одной находятся элементы, которые не меньше медианы, в другой – не больше медианы.
#Задачу можно решить без сортировки исходного массива. Но если это слишком сложно, то используйте метод сортировки, который не рассматривался на уроках.
        
def shaker(orig_list):
    n = 1
    lst = range(len(orig_list) - 1)
    while n < len(orig_list):
        for part in (lst, reversed(lst)):
            for i in part:
                if orig_list[i] > orig_list[i+1]:
                    orig_list[i], orig_list[i+1] =  orig_list[i+1], orig_list[i]
        n += 1
    print(orig_list)
    b = orig_list[len(orig_list)//2]
    print(b)

orig_list = [random.randint(0, 100) for _ in range(2 * (random.randint(1, 10)) + 1)]
print(orig_list)
shaker(orig_list)
# замеры
print(timeit.timeit("shaker(orig_list)", \
    setup="from __main__ import shaker, orig_list", number=1))

# вариант решения без сортировки
#orig_list = [1,5,7,0,2,13,15,28,31,3,4]
b = len(orig_list) // 2
lst = []
for i in orig_list:
    c = min(orig_list)
    lst.append(c)
    orig_list.remove(c)
    if len(lst) == b + 1:
        print(lst[-1])
        break
      

