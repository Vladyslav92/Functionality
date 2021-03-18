def func(a, b, c=2):
    return a + b + c


print(func(1, 2))  # 5
print(func(1, 2, 3))  # 6
print(func(a=5, b=5, c=5))  # 15


def func2(*args):
    return args


print(func2(1, 2, 3, 'abc'))  # (1, 2, 3, 'abc')
print(func2())  # ()
print(func2(1))  # (1,)


def func3(**kwargs):
    return kwargs


print(func3(a=1, b=2, c=3, d=4, f=5))  # {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'f': 5}
print(func3(a='python'))  # {'a': 'python'}

func4 = (lambda x, y: x + y)
print(func4(10, 10))  # 20
print(func4('a', 'b'))  # ab

func5 = lambda *args: args
print(func5(1, 2, 3, 4, 5))  # (1, 2, 3, 4, 5)


def func6():
    print("You just created a function!")


func6()  # You just created a function!
print(func6())  # You just created a function!


# None

def func7():
    pass


print(func7())  # None


def func8(*args, **kwargs):
    print(args)
    print(kwargs)
    # (1, 2, 3)


func8(1, 2, 3, name='Vlad', job='iT programmer')  # {'name': 'Vlad', 'job': 'iT programmer'}


def func9():
    global a
    a = 1
    b = 2
    return a + b


def func10():
    c = 3
    return a + c


print(func9())  # 3
print(func10())  # 4


def print_max(a, b):
    if a > b:
        print("{} больше {}".format(a, b))
    elif a < b:
        print("{} меньше {}".format(a, b))
    else:
        print("{} и {} равны".format(a, b))


print_max(3, 4)  # 3 меньше 4

x = 50


def func11(x):
    print("x равен {}".format(x))  # x равен 50
    x = 2
    print("Замена локального x на {} ".format(x))  # Замена локального x на 2


func11(x)
print('x по-прежнему {}'.format(x))  # x по-прежнему 50

X = 50


def func12():
    global x
    print("x равно {}".format(x))  # x равно 50
    x = 2
    print("Заменяем глобальное значение x на {}".format(x))  # Заменяем глобальное значение x на 2


func12()
print('Значение x составляет {}'.format(x))  # Значение x составляет 2


def func_outer():
    x = 2
    print("x равно {}".format(x))  # x равно 2

    def func_inner():
        nonlocal x
        x = 5

    func_inner()
    print("Локальное x сменилось на {}".format(x))  # Локальное x сменилось на 5


func_outer()


def say(message, times=1):
    print(message * times)


say("Hello World!")  # Hello World!
say("Hello ", 5)  # Hello Hello Hello Hello Hello


def func13(a, b=5, c=10):
    print('\ta равно {}'.format(a), ', \tb равно {}'.format(b), ', \tа c равно {}'.format(c))


func13(3, 7)  # a равно 3 , 	b равно 7 , 	а c равно 10
func13(25, c=24)  # a равно 25 , 	b равно 5 , 	а c равно 24
func13(c=50, a=100)  # a равно 100 , 	b равно 5 , 	а c равно 50


def print_max2(x, y):
    """Выводит максимальное из двух чисел.
Оба значения должны быть целыми числами."""
    x = int(x)  # конвертируем в целые, если возможно
    y = int(y)

    if x > y:
        print(x, 'наибольшее')
    else:
        print(y, 'наибольшее')


print_max2(3, 5)  # 5 наибольшее
print(print_max2.__doc__)  # Выводит максимальное из двух чисел. Оба значения должны быть целыми числами.


def total(a=5, *numbers, **phonebook):
    print('a', a)

    # проход по всем элементам кортежа
    for single_item in numbers:
        print('single_item', single_item)

    # проход по всем элементам словаря
    for first_part, second_part in phonebook.items():
        print(first_part, second_part)


print(total(10, 1, 2, 3, Jack=1123, John=2231, Inge=1560))


# Перевод числа с двоичной в десятеричную
def bin_to_dec(digit):
    dlina = len(digit)
    print(dlina)
    chislo_dec = 0
    for i in range(0, dlina):
        chislo_dec = chislo_dec + int(digit[i]) * (2 ** (dlina - i - 1))
    return chislo_dec


# еще вариант из любой в любую
def convert_base(num, to_base=10, from_base=10):
    # first convert to decimal number
    if isinstance(num, str):
        n = int(num, from_base)
    else:
        n = int(num)
    # now convert decimal to 'to_base' base
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if n < to_base:
        return alphabet[n]
    else:
        return convert_base(n // to_base, to_base) + alphabet[n % to_base]


convert_base('AA16342F', from_base=16, to_base=8)  # '25205432057'
convert_base('111', from_base=2)  # 7
convert_base(33, to_base=16)  # 21
convert_base(33333, to_base=20)  # '436D'
convert_base(3333333, to_base=20)  # '10GD6D'
# print(
#    convert_base(input("Введите число: "),
#    from_base=int(input("Из какой системы вычисляем: ")),
#    to_base=int(input("В какую систему переводим: ")))
# )

# ---------------------------------------------------------------------
# Шифр Цезаря

# First variant
def code_cesar(text, key):
    new_word = []
    new_letter = ''
    for i in text:
        if 65 <= ord(i) <= 90:
            new_letter = chr((((ord(i) - 65) + key) % 26) + 65)
            new_word.append(new_letter)
        elif 97 <= ord(i) <= 122:
            new_letter = chr((((ord(i) - 97) + key) % 26) + 97)
            new_word.append(new_letter)
        else:
            new_word.append(i)
            # print(i)
    return ''.join(new_word)


first = input("Введите сообщение: ").lower()
second = int(input("Введите сдвиг: "))
print(code_cesar(first, second))

# Seocnd variant
message = input("Введите сообщение: ").lower()
offset = int(input("Введите сдвиг: "))
encoded_message = ""
alphabet = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
for ch in message:
    position = alphabet.find(ch)
    newPosition = position + offset
    if ch in alphabet:
        encoded_message = encoded_message + alphabet[newPosition]
    else:
        encoded_message = encoded_message + ch

print(encoded_message)
# -----------------------------------------------------------------------
'''
Напишите два двойных цикла.
В первом цикле while мы постоянно запрашиваем целое число,
а во втором, с помощью цикла for считаем сумму чисел от 0 до введенного числа.
Выход из первого цикла осуществляем если ввели число 0.
'''

# Variant - 1
num = int(input("Введите целое число (0 для выхода): "))
summ = 0
while num != 0:
    for i in range(0, num + 1):
        summ += i
    print(summ)
    num = int(input("Введите целое число (0 для выхода): "))
    break

# Variant - 2
num2 = int(input("Введите целое число (0 для выхода): "))
summ2 = 0
while num2 != 0:
    counter = 0
    while counter <= num2:
        summ2 += counter
        counter += 1
    print(summ2)
    num2 = int(input("Введите целое число (0 для выхода): "))

# Создание пароля
import random


def create_pass(length):
    alpha = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM`!@#$%^&*()_-+{}[]|:;?/><.,'
    password = ''
    for _ in range(length):
        password += random.choice(alpha)

    return password


base = []
for _ in range(8000000000):
    base.append(create_pass(5))
print(set(base))
print(len(base))

# НЕ ПРАВИЛЬНЫЙ КАЛЬКУЛЯТОР ___________________________________________________________________________
# 1.
result = None
operand = None
operand2 = None
operator = None
wait_for_number = True

while wait_for_number:
    base = []
    try:
        operand = input("Enter the number: ")
        if operand in 'abcdefghijklmnopqrstuvwxyz':
            raise ValueError
        base.append(operand)
    except ValueError:
        print("Is not a number")
        continue

    try:
        operator = input("Enter the operator (+ - * /): ")
        if operator not in '+-*/':
            raise ValueError
        base.append(operator)
    except ValueError:
        print("Is not '+' or '-' or '/' or '*'. Try again")
        continue

    try:
        operand2 = input("Enter second number: ")
        if operand2 in 'abcdefghijklmnopqrstuvwxyz':
            raise ValueError
        base.append(operand2)
    except ValueError:
        print("Is not a number")
        continue

    result = ''.join(base)

    try:
        operator2 = input("Enter finish operator '=': ")
        if operator2 == '=':
            print(eval(result))
            wait_for_number = False
        else:
            raise ValueError
    except ValueError:
        print("Is not '=' Try again")
        continue
# 2.
result = None
operand = None
operand2 = None
operator = None
wait_for_number = True
base = []

while wait_for_number:
    try:
        operand = input("Enter the number: ")
        base.append(operand)
        operator = input("Enter operator (- + * /): ")
        base.append(operator)
    except ValueError:
        print('Error!')

    if '=' in base:
        base.remove('=')
    result = ''.join(base)

    if operator == '=':
        try:
            if result in '10+56/3-a2*6':
                result = 18
                print(result)
            print(float(eval(result)))
        except NameError:
            print("Error!")
        except TypeError:
            print("Error!!")
        break
# ________________________________________________________________________________________________________
