# with open('books.txt', 'r', encoding='utf-8') as f:
#     print(f.read())



# with open('books.txt', 'r') as rf:
#     with open('books_copy.txt', 'w') as wf:
#         for line in rf:
#             wf.write(line)

# from datetime import datetime

# login = input('enter your login: ')
# password = input('enter your password: ')

# with open('users.txt', 'r') as rf:
#     for users in rf:
#         [login_db, password_db] = users.split(' ')

#         if login is login_db.rstrip() and password is password_db.rstrip():
#             print(f'Hi, {login}')
#             with open('log.txt', 'a', encoding='utf-8') as rw:                    
#                 rw.write(f'пользователь {login} вошел в систему успешно в {datetime.now()}')
#         else: print('Enter the correct login or password')             