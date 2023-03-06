from random import *

chars = ''


print('')
count = int(input('Сколько паролей я должен сгенерировать? '))
long = int(input(' А какая длина пароля? '))
print('')
print('Я понимаю только   да или нет')
print('')
digit = input('Включать ли цифры? ')
up = input('Включать ли прописные буквы? ')
low = input('Включать ли строчные буквы? ')
sym = input('Включать ли символы: !#$%&*+-=?@^_ ? ')
strange = input('Исключать ли неоднозначные символы il1Lo0O? ')

if digit == 'да':
    chars += '23456789'
if up == 'да':
    chars += 'ABCDEFGHIJKMNPQRSTUVWXYZ'
if low == 'да':
    chars += 'abcdefghjkmnpqrstuvwxyz'
if sym == 'да':
    chars += '!#$%&*+-=?@^_'
if strange == 'да':
    chars += 'il1Lo0O'


def generate_password(lenght, chars):
    password = ''
    for i in range(lenght):
        password += chars[randrange(len(chars))]
    return password


print(*[generate_password(long, chars) for i in range(count)], sep='\n')