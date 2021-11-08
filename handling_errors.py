# x = 20
# try:
#     print(x)
# except:
#     print('X is not defined')



# try:
#     print(x)
# except NameError:
#     print("X is not defined")
# else:
#     print('я не знаю что делать')
# finally:
#     print('some text')



# x = int(input('enter positive number: '))
# try:
#     if x > 0:
#         print(x)
#     else:
#         raise Exception('no negatives')
# except:
#     print("no negative numbers")



# x = 'hello'
# if not type(x) is int:
#     raise TypeError('only int are valid')



# while True:
#     try:
#         a = int(input('enter the 1 number: '))
#         b = int(input('enter the 2 number: '))
#         print(a / b)
#     except ZeroDivisionError:
#         print('че матем не учил')
#     except ValueError:
#         print('введи числа')
#     else:
#         break



# while True:
#     x = input('enter the 1 number: ')
#     y = input('enter the 2 number: ')
#     if x.isdigit() and y.isdigit():
#         if int(y) == 0:
#             print("че матем не учил")
#         else:
#             print(int(x) / int(y))
#             break
#     else:
#         print('введи числа')



list = [10, 100, 'a', True, 2]
for i in range(1, len(list)):
    try:
        print(list[i - 1] / list[i])
        if i == len(list) - 1:
            print(list[i] / list[0])
    except:
        print('делить можно только числа')