# a = int(input("Введите число: "))
# b = int(input("Введите число: "))
# c = int(input("Введите число: "))
# d = (a + b)*c
# print(d)



# a = int(input("Введите число: "))
# b = int(input("Введите число: "))
# if a * b > 100:
#     print(1)
# else:
# #     print(-1)



# num = int(input("Введите число: "))
# if num > 0:
#     print("положительный")
# elif num < 0:
#     print("Отрицательный")
# else:
# #     print("ноль")



# Age = int(input("введите число: "))
# if Age >= 18:
#     print("тебе можно!")
# else:
#     print("тебе нельзя!")



# print(float(23))
# print(2e-2)



# a = int(input("введите число: "))
# if a > 0:
#     print(a % 10)



# x = float(input("введи значение x: "))
# if x <= 0:
#     print(x**2 + 9*x + 4)
# else:
#     print(x**3)



# c = int(input())
# m = int(input())
# if m > 0 and 0 < c <= m:
#     if not (m % 100) and not (c % 100):
#         change = m - c
#         thousands = change // 1000
#         change = change - thousands * 1000
#         five_hundreds = change // 500
#         change = change - five_hundreds * 500
#         one_hundreds = change // 100
#         print(thousands, five_hundreds, one_hundreds)



# hours = int(input("введи часы: "))
# minutes = int(input("введи минуты: "))
# delta = float(input("введи дельту: "))
# if 0 <= hours < 24:
#     if 0 <= minutes < 60:
#         newHours = int((hours + delta) % 24)
#         newMinutes = int((float((hours + delta)%24) - int((hours + delta) % 24)) * 60 + minutes) 
#         if newMinutes >= 60:
#             newMinutes = int(newMinutes - 60)
#             newHours = int(newHours + 1)
#         if newHours < 10:
#             newHours = "0" + str(newHours)
#         if newMinutes < 10:
#             newMinutes = "0" + str(newMinutes)
#         print(str(newHours) + ":" + str(newMinutes))
            

 
# # домашка на этажи
# total = int(input())
# floors = int(input())
# apartment = int(input())
# if not(total % floors) and floors > 0 and 0 < apartment <= total:
#     if apartment % (total/floors) == 0:
#         print(int(apartment / (total/floors)))
#     else:
#         print(int(apartment // (total/floors) + 1))
# else:
#     print("введите верные данные!")      



#минимум двух чисел 
# a = float(input())
# b = float(input())
# print(b) if a > b else print(a)



# сортировка 3 чисел по возрастанию
# a = float(input())
# b = float(input())
# c = float(input())
# if a < c < b:
#     print(a, b, c) 
# elif a < b < c:
#     print(a, b, c)
# elif b < a < c:
#     print(b, a, c)
# elif b < c < a:
#     print(b, c, a)
# elif c < a < b:
#     print(c, a, b)
# else:
#     print(c, b, a)



# числа от 0 до 9
# i = 0
# while i < 10:
#     print(i)
#     i += 1



# четные числа до 10
# i = 0
# while i <= 10:
#     print(i)
#     i += 2



# нечетные числа до 20
# i = 1
# while i <=20:
#     print(i)
#     i += 2



# # задание
# i = 3
# prev = 1
# next = 1
# while i <= 100:
#     newNext = prev + next
#     prev = next
#     next = newNext
#     print(newNext)
#     i += 1



# задание
# i = 3
# prev = 10
# next = 11
# while i <= 10:
#     newNext = (prev * next) ** 0.5
#     prev = next
#     next = newNext
#     print(newNext)
#     i += 1



# задание
# i = 100
# while i >= 0:
#     print(i)
#     i -= 10



# задание
# V1 = float(input("1 скорость: "))
# V2 = float(input("2 скорость: "))
# t = float(input("введите время: "))
# D = V1 * t + V2 * t
# print(D)
# print(D * 1000)



# високосный год
# a = int(input("введите год:"))
# if (a % 4 == 0 and a % 100 != 0) or (a % 100 == 0 and a % 400 == 0):
#     print(True)
# else:
#     print(False)



# если число четное, продолжать выпрашивать новое число, а если отрицательное - остановить цикл
# while True:
#     num = int(input("number: "))
#     if num < 0:
#         print("отрицательное число")
#         break




# если число четное, возвести его в 10-ую степень
# while True:
#     num = int(input("number: "))
#     if not(num % 2):
#         print(num ** 10)
    


# арифметическая прогрессия
# a = int(input("number: "))
# d = int(input("difference: "))
# n = int(input("кол-во чисел: "))
# sum = 0
# i = 0
# while i < n:
#     sum += a
#     a += d
#     i += 1
# print(sum)



# # является ли число простым
# N = int(input("write the number that you want to check: "))
# i = 2
# prime = True
# while i * i <= N:
#     if N % i == 0:
#         prime = False
#         break
#     i += 1
# print(True) if prime else print(False)



# # task 2
# N = int(input("enter the number: "))
# if 1 <= N <= 9:
#     sum = 0
#     i = 1
#     while i <= N:
#         j = i
#         while j <= N:
#             sum += i * j
#             j += 1
#         i += 1
#     print(sum)
# else:
#     print(False)



# # homework 4
# n = int(input("enter the max integer: "))
# i = 2
# while i <= n:
#     prime = True
#     j = 2
#     while j < i:
#         if i % j == 0:
#             prime = False
#             break
#         j += 1
#     if prime:
#         print(i)
#     i += 1




# # task 1
# N = int(input("enter the number: "))
# i = 0
# sum = 0
# while i < N:
#     a = int(input())
#     sum += a
#     i += 1
# print(sum)



# лежит ли цифра внутри числа
# a = int(input("enter the number: "))
# b = int(input("enter the digit: "))
# found = False
# while a > 0 and not found:
#     c = a % 10
#     if c == b:
#         found = True
#     else:
#         a //= 10
# print(found)



# факториал числа
# a = int(input('enter the number: '))
# i = 1
# prod = 1
# while i <= a:
#     prod *= i
#     i += 1
# print(prod)    



# # Задача 6: 
# # треугольнык из чисел
# a = int(input('enter the number: '))
# i = 1
# while i <= a:
#     j = 1
#     while j <= i:
#         print(j, end=' ')
#         j += 1
#     print()
#     i += 1



# for i in range(0, 10, 2):
#     print(i)



# name = 'Elbek'
# print(len(name))



# name = 'elbek'
# print(name[0])



# name = 'elbek'
# for i in range(0, len(name)):
#     print(name[i], end=' ')



# name = 'elbek'
# str = f'i am {name}'
# print(str)

# print('elbek'.lower())



# сколько 1 в двоичном виде этого числа?
# sum = 0
# x = int(input())
# while x > 0:
#     digit = x % 2
#     sum += digit
#     x //= 2
# print(sum)