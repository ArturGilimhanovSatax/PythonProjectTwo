import os

s = input()
#1
print(s[2])
#2
print(s[-2])
#3
print(s[:5])
#4
print(s[:-2])
#5
print(s[::2])
#6
print(s[1::2])
#7
print(s[::-1])
#8
print(s[::-2])
#9
print(len(s))

input()
os.system('cls')
#------------------------------------------------------------------------------
#Количество слов
print('\nКолличество слов')
w = ('PyCharm cool soft!')
text = w.split()
line_text = len(text)
print(line_text)

input()
os.system('cls')
#------------------------------------------------------------------------------
#Две половинки
print('\nДве половинки')
s = input()
index = len(s) // 2
print(s[index:], s[:index])

input()
os.system('cls')
#------------------------------------------------------------------------------
#Первое и последнее вхождения
print('\nПервое и последнее вхождения')
t = input()
if t.count('f') == 1:
    print(t.find('f'))
elif t.count('f') >= 2:
    print(t.find('f'), t.rfind('f'))

input()
os.system('cls')
#------------------------------------------------------------------------------
#Удаление фрагмента
print('\nУдаление фрагмента')
f = input()
f = f[:f.find('h')] + f[f.rfind('h') + 1:]
print(f)

input()
os.system('cls')
#
#------------------------------------------------------------------------------
#Замена подстроки
print('\nЗамена подстроки')
print(input().replace('1', 'one'))

input()
os.system('cls')
#------------------------------------------------------------------------------
#Удаление символа
print('\nУдаление символа')
s = input()
print(s.replace('@', ''))

input()
os.system('cls')
#------------------------------------------------------------------------------
#Замена внутри фрагмента
print('\nЗамена внутри фрагмента')
f = input()
a = f[:f.find('h') + 1]
b = f[f.find('h') + 1:f.rfind('h')]
c = f[f.rfind('h'):]
s = a + b.replace('h', 'H') + c
print(f)

input()
os.system('cls')
#------------------------------------------------------------------------------
#Минимум из двух чисел
print('\nМинимум из двух чисел')
first = int(input())
second = int(input())
if first < second:
    print(first)
else:
    print(second)

input()
os.system('cls')
#------------------------------------------------------------------------------
#Знак числа
print('\nЗнак числа')
x = int(input())
if x > 0:
    print(1)
elif x == 0:
    print(0)
else:
    print(-1)

input()
os.system('cls')
#------------------------------------------------------------------------------
#Шахматная доска
print('\nШахматная доска')
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if (x1 + y1 + x2 + y2) % 2 == 0:
    print('YES')
else:
    print('NO')

input()
os.system('cls')
#------------------------------------------------------------------------------
#Високосный год
print('\nВисокосный год')
y = int(input())
if (y % 4 == 0) and (y % 100 != 0):
    print('YES')
elif (y % 400 == 0):
    print('YES')
else:
    print('NO')

input()
os.system('cls')
#------------------------------------------------------------------------------
#Сколько совпадает чисел
print('\nСколько совпадает чисел')
num1 = int(input())
num2 = int(input())
num3 = int(input())
if num1 == num2 == num3:
    print(3)
elif num1 == num2 or num2 == num3 or num1 == num3:
    print(2)
else:
    print(0)

input()
os.system('cls')
#------------------------------------------------------------------------------
#Ход ладьи
print('\nХод ладьи')
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if x1 == x2 or y1 == y2:
    print('YES')
else:
    print('NO')

input()
os.system('cls')
#------------------------------------------------------------------------------
#Шоколадка
print('\nШоколадка')
n = int(input())
m = int(input())
k = int(input())
if k < n * m and ((k % n == 0) or (k % m == 0)):
    print('YES')
else:
    print('NO')

input()
os.system('cls')
#------------------------------------------------------------------------------
#Яша плавает в бассейне
print('\nЯша плавает в бассейне')
N = int(input())
M = int(input())
x = int(input())
y = int(input())
if N > M:
    N, M = M, N
if x >= N / 2:
    x = N - x
if y >= M / 2:
    y = M - y
if x < y:
    print(x)
else:
    print(y)

input()
os.system('cls')
#------------------------------------------------------------------------------
