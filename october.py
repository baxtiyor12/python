#треугольник чисел
# num = int(input('enter the number: '))
# for i in range(num):
#     for j in range(i):
#         print(' ', end=' ')
#     for j in range(num-i):
#         print(j, end=' ')
#     print()



# name = 'elbek'
# for i in range(len(name)):
#     print(i, name[i])



# name = 'elbek'
# for i in name:
#     print(i)



# name = 'elbek'
# print(name.upper())



# students = ['maqsad', 'asad', 'asliddin', 'mirsaid', 'botir', 'nemo']
# # print(students)
# # for i in range(len(students)):
# #     print(students[i])

# for student in students:
#     print(student)

# students.append('baxti') #добавляет в конец
# students.insert(1, 'tima') #добавляет под индекс
# print(students)



# #добавляет в список до тех пор пока не вводится пустота
# names = []
# while True:
#     name = input('enter the name: ')
#     if name.strip() == '': print(names)
#     else: names.append(name.strip().capitalize()) 
#     #strip = убирает пробелы
#     #capitilaze = делает первую букву заглавной, а остальные маленькие



# #добавленные в список имена выводит в обратном порядке
# names = []

# while True:
#     name = input('enter the name: ')
#     if name.strip() == '': break
#     else: names.append(name.strip().capitalize())

# # reversed_names = []
# # for i in range(len(names) - 1, -1, -1):
# #     reversed_names.append(names[i])

# # print(reversed_names)

# print(names[::-1]) #выдает список начиная с конца[::-1]



# names = []
 
# names.append('max')
# names.extend('elbek') #передает по символам

# print(names)



# #матрица
# # [
# #     [1,2,3],
# #     [4,5,6],
# #     [7,8,9]
# # ]
# matrix = [[1,2,3],[4,5,6],[7,8,9]]
# for list in matrix:
#     for value in list:
#         print(value, end=' ')

# # for i in range(len(matrix)):
# #     for j in range(len(matrix[i])):
# #         print(matrix[i][j])




                                                        #20.10.2021


# month = {
#     1: 'january',
#     2: 'february',
#     3: 'march', 
#     4: 'april', 
#     5: 'may', 
#     6: 'june',
#     7: 'july',
#     8: 'august',
#     9: 'september',
#     10: 'october',
#     11: 'november',
#     12: 'december'
# }

# def transfer_month_num_to_string(monthNum):
#     return f'{month[monthNum]}'

# num = int(input('enter the month number: '))
# print(transfer_month_num_to_string(num))



# print('select one of the listed figures: \n1 - circumference \n2 - square \n3 - rectangle \n4 - right triangle:')
# fig = int(input('select one of the listed figures: '))

# def calc_area_of_circumference(radius):
#     from math import pi
#     return pi * radius * radius


# def calc_are_of_square(side):
#     return side * side


# def calc_are_of_rectangle(side1, side2):
#     return side1 * side2


# def calc_are_of_right_triangle(katet1, katet2):
#     return (katet1 * katet2) / 2 

# if fig is 1:
#     print('you have selected circumference')
#     r = int(input('enter the radius of your figure: '))
#     print(calc_area_of_circumference(r))


# if fig is 2:
#     print('you have selected square')
#     side = int(input('enter the side: '))
#     print(calc_are_of_square(side))


# if fig is 3:
#     print('you have selected rectangle')
#     side1 = int(input('enter the side1: '))
#     side2 = int(input('enter the side2: '))
#     print(calc_are_of_rectangle(side1, side2))


# if fig is 4:
#     print('you have selected right triangle')
#     katet1 = int(input('enter the katet1: '))
#     katet2 = int(input('enter the katet2: '))
#     print(calc_are_of_right_triangle(katet1, katet2))



# prod = 1
# for n in range(1, 5):
#     prod *= 2 * n
# print(prod)



# import math





                                                     #22.10.2021


# sum = lambda x, y : (x + y, x - y)
# print(sum(1, 2))



# abc = lambda x : x
# print(abc(1))



# print((lambda x, y : x + y)(1, 2))

# print((lambda First_name, Sur_name : f'Hello! I am {First_name} {Sur_name}')('Muhammadyusuf','Alijanov'))


                                                 #25.10.2021


