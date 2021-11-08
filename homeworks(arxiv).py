# 30.09.2021
# # Задание 1:
# # Вводится целое число. Вывести число, обратное введенному по порядку составляющих его цифр. Например, введено 3425, надо вывести 5243.

# n = int(input('enter the number: '))
# while n > 0:
#     digit = n % 10
#     print(digit, end='')
#     n //= 10



# # Задание 2:
# # Вводится целое число. Найти сумму и произведение его цифр. Например, сумма цифр числа 253 равна 10-ти, так как 2 + 5 + 3 = 10. 
# # Произведение цифр числа 253 равно 30-ти, так как 2 * 5 * 3 = 30.

# n = int(input('enter the number: '))
# sum = 0
# prod = 1
# while n > 0:
#     digit = n % 10
#     sum += digit
#     prod *= digit
#     n //= 10
# print('сумма цифр равна:', sum)
# print('произведение цифр равна:', prod)



# # Задание 3:
# # Вводится целое число. Определить, сколько в числе четных цифр, а сколько нечетных.
# # Пример:
# # 65439
# # Even: 2, odd: 3

# n = int(input('enter the number: '))
# even = 0
# odd = 0
# while n > 0:
#     digit = n % 10
#     if digit % 2 == 0:
#         even += 1
#     else:
#         odd += 1
#     n //= 10
# print('even:', even, 'odd:', odd)



# # Задача 4:
# # Даны два целых числа A и В. Выведите все числа от A до B включительно, в порядке возрастания, если A < B, или в порядке убывания в противном случае.
# # Пример:
# # 5
# # 9
# # Вывод: 5 6 7 8 9
# # Пример 2:
# # 10
# # 4
# # Вывод: 10 9 8 7 6 5 4

# a = int(input('enter the 1st number: '))
# b = int(input('enter the 2nd number: '))
# if a < b:
#     for x in range (a, b + 1):
#         print(x, end=' ')
# else:
#     for y in range (a, b - 1, -1):
#         print(y, end=' ')



# # Задача 5:
# # Запрашивать у пользователя числа, до тех пор пока их сумма не будет больше 100. Пользователь может вводить как положительные, так и отрицательные числа

# sum = 0
# while sum < 100:
#     num = int(input('enter the number: '))
#     sum += num
# print('сумма превысила 100, вы не можете больше ввести числа!', 'сумма =', sum)



# # Задача 6: 
# # треугольнык из чисел
# a = int(input('enter the number: '))
# i = 0
# w = a
# while i <= a:
#     j = 0
#     while j <= w:
#         print(j, end=' ')
#         j += 1
#     w -= 1
#     print()
#     i += 1



# # Задача 7:
# # Напишите программу, которая возвращает среднее значение всех цифр введенного числа.
# # Например:
# # 46 -> 5
# # 666 -> 6
# # 104 -> 2
# # Примечание: среднее значение всегда должно быть целым числом

# num = int(input('enter the number: '))
# количество_чисел = 0 
# сумма_чисел = 0
# while num > 0:
#     digit = num % 10
#     количество_чисел += 1
#     сумма_чисел += digit
#     num //= 10
#     сред_ариф = сумма_чисел / количество_чисел
# print(int(сред_ариф))



#OCTOBER      #OCTOBER      #OCTOBER      #OCTOBER       #OCTOBER       #OCTOBER
# #task 1
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# for i in a:
#     if i < 5:
#         print(i)



# #task2
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# c = []
# for i in a:
#     for j in b:
#         if i == j:
#             c.append(i)
# print(c)



# #task3
# a = ['hello  ', '   world', '   hi   ', '  ', '  Elbek  ']
# for i in a:
#     if i.strip() == '' : continue
#     print(i.strip())



# #task4
# a = []
# for i in range(100, 150, 2):
#     a.append(i)
# print(a)



# # #task5
# num = int(input('сколько чисел Фибоначчи должно присутствовать: '))
# prev = 0
# next = 1
# a = 0
# list = []
# for i in range(num):
#     newNext = prev + next
#     prev = next
#     next = newNext
#     list.append(newNext)
# print(list)



# #task6
# numbers = []
# digit = int(input('сколько чисел будет в массиве: '))
# d = 0
# while d <= digit - 1:
#     num = d
#     numbers.append(num**2)
#     d += 1
# print(numbers)



# #task7
# numbers = []
# digit = int(input('сколько чисел будет в массиве: '))
# l = 0

# while l < digit:
#     num = int(input('enter the number: '))
#     numbers.append(num)
#     l += 1

# for i in range((len(numbers))):
#     if i % 2 == 0: numbers[i] = 1
#     else: numbers[i] = i % 5
# print(numbers)



# #task8
# # Найти количество четных чисел в массиве.
# list = []
# digit = int(input('сколько чисел будет в массиве: '))
# l = 0
# количество_четных_чисел = 0

# while l < digit:
#     num = int(input('enter the number: '))
#     list.append(num)
#     l += 1

# for i in list:
#     if i % 2 == 0: количество_четных_чисел += 1
# print(количество_четных_чисел)



# #task9
# list = []
# digit = int(input('сколько чисел будет в массиве: '))
# l = 0
# количество_чисел = 0

# while l < digit:
#     num = int(input('enter the number: '))
#     list.append(num)
#     l += 1

# for i in list:
#     if i % 3 == 0 and i % 7 != 0: количество_чисел += 1
# print(количество_чисел)



# #task10
# # Найдите сумму и произведение элементов массива.
# list = []
# digit = int(input('сколько чисел будет в массиве: '))
# l = 0
# sum = 0
# prod = 1

# while l < digit:
#     num = int(input('enter the number: '))
#     list.append(num)
#     l += 1

# for i in list:
#     sum += i
#     prod *= i

# print('сумма элементов равна:', sum, 'произведение элементов равна:', prod)



# #task11
# # Найдите сумму нечетных чисел массива, которые не превосходят 11.
# list = []
# digit = int(input('сколько чисел будет в массиве: '))
# l = 0
# sum = 0

# while l < digit:
#     num = int(input('enter the number: '))
#     list.append(num)
#     l += 1

# for i in list:
#     if i % 2 != 0 and i <= 11: sum += i
# print('сумма нечетныx чисел массива равна:', sum)



# #task12
# list = []
# digit = int(input('сколько чисел будет в массиве: '))
# l = 0
# sum = 0

# while l < digit:
#     num = int(input('enter the number: '))
#     list.append(num)
#     l += 1

# for i in list:
#     if i % 2 != 0: sum += i
#     else: break

# print(sum)



# #task13
# # Найдите сумму чисел массива, которые стоят на нечетных местах и при этом превосходят сумму крайних элементов массива.
# list = []
# digit = int(input('сколько чисел будет в массиве: '))
# l = 0
# sum = 0

# while l < digit:
#     num = int(input('enter the number: '))
#     list.append(num)
#     l += 1

# for i in range(len(list)):
#     if i % 2 != 0:
#         sum1 = list[0] + list[-1]
#         if list[i] > sum1: sum += list[i]

# print(sum)



# #task14
# # Найдите сумму наибольшего и наименьшего элементов массива.
# list = []
# digit = int(input('сколько чисел будет в массиве: '))
# l = 0

# while l < digit:
#     num = int(input('enter the number: '))
#     list.append(num)
#     l += 1

# for i in list:
#     sum = max(list) + min(list)

# print(sum)



# #task15
# # Найдите количество элементов массива, которые отличны от наибольшего элемента не более чем на 10%.
# list = []
# digit = int(input('сколько чисел будет в массиве: '))
# l = 0
# sum = 0

# while l < digit:
#     num = int(input('enter the number: '))
#     list.append(num)
#     l += 1

# for i in list:
#     число = max(list) / 10
#     if i > число: sum += 1

# print(sum)



# #task16
# # Среди элементов с нечетными индексами найдите наибольший элемент массива, который делится на 3.
# a = [1, 21, 5, 6, 27, 0]
# b = []
# for i in range(len(a)):
#     if i % 2 != 0:
#         b.append(a[i])
# print(max(b))



# #task17
# # Дан массив и число
# # p. Найдите два различных числа в массиве, сумма которых наиболее близка к p
# p = 3.145
# list = [0, 1, 2, 3, 4]
# sum = []
# for i in range(len(list)-1):
#     num = list[i] + list[i + 1]
#     if num <= p:
#         sum.append(num)
# print(max(sum))



# #task18
# # Дан массив. Найдите два соседних элемента, сумма которых минимальна.
# list = [1, 3, 4.5, 29, -12]
# sum = []
# for i in range(len(list)-1):
#     num = list[i] + list[i + 1]
#     sum.append(num)
# print(min(sum))



# #task19
# # Дан массив. Найдите три последовательных элемента в массиве, сумма которых максимальна.
# list = [1, 3, 56, 8.5, -12]
# sum = []
# for i in range(1, len(list)-2):
#     num = list[i] + list[i + 1] + list[i + 2]
#     sum.append(num)
# print(max(sum))




# #task20
# # Найдите количество чисел, каждое из которых равно сумме квадратов своих соседей и при этом не является наибольшим в массиве.
# list = [2, 13, 3, 25]
# количество_чисел = 0
# for i in list:
#     for j in range(1, len(list) - 1):
#         a = list[j]
#         b = list[j-1] ** 2
#         c = list[j+1] ** 2
#         if a == b + c and not(max(list)):
#             количество_чисел += 1

# print(количество_чисел)




# task21
# Проверьте, образует ли элементы массива в данном порядке арифметическую или геометрическую прогрессии.
# list = [1, 2, 3, 4, 5, 6]
# for i in range(len(list)):
#     if list[1] - list[0] == list[-1] - list[-2]:
#         print('арифметическая прогрессия')
#     elif list[1] / list[0] == list[-1] / list[-2]:
#         print("геометрическая прогрессия")



# # task22
# # Проверьте, является ли данный массив возрастающим или убывающим.
# numbers = [2, 3.2, 4, 67, 89]
# if numbers[0] < numbers[1]: print('массив является возрастающим')
# else: print('массив является убывающим')



# # task23
# # Найдите количество различных элементов данного массива.
# list = [1, 23, 1.5, -34.4, 'hello', 'world']
# print(len(list))



# # task24
# # Определите, есть ли в массиве повторяющиеся элементы.
# list = [1, 2, 4, 6, 1]
# # list.sort()
# for i in list:
#     for value in i:
#         print(value, end=' ')
        
#     # else: print("нет повторяющиеся чисел")



# task25
# Определите, можно ли вычеркнуть из данного массива одно число так, чтобы оставшиеся числа оказались упорядоченными по возрастанию.



# #task 1
# dictionary_1 = {'a': 300, 'b': 400}
# dictionary_2 = {'c': 500, 'd': 600}
# dictionary_3 = {}

# for k, v in dictionary_1.items():
#     dictionary_3[k] = v
    
# for k1, v1 in dictionary_2.items():
#     dictionary_3[k1] = v1

# print(dictionary_3)




# #task 2
# my_dictionary = {'data1': 375, 'data2': 567, 'data3': -37, 'data4': 21}
# prod = 1

# for i in my_dictionary.values():
#     prod *= i

# print(prod)



# #task 3
# dict = {a: a ** 3 for a in range(1, 11)}
# print(dict)



# #task 4
# keys = ['red', 'green', 'blue']
# values = ['#FF0000','#008000', '#0000FF']
# dict = {} 

# for i in range(len(keys)):
#     dict[keys[i]] = values[i]

# print(dict)



#task 5
str1 = 'pythonist'
dict = {}
for i in str1:
    if str1[i] != str1[i + 1]:
        dict[i] = 1
    else: dict[i] = 2
print(dict)



# #task 6
# to_dict = ['grey', (2, 17), 3.11, -4]
# dict = {}
# for i in to_dict:
#     dict[i] = i
# print(dict)



# #task 7
# dict = {'data1': 375, 'data2': 567, 'data3': -37, 'data4': 21, 'data5': 0}
# dict['data1'] = 0
# dict['data5'] = 375
# del dict['data2']
# dict['new_key'] = 'new_value'
# print(dict)