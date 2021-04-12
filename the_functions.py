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
enter_string = input("Enter your string: ")


def normalize(string):
    alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    for x in string:
        if x in alphabet:
            string = string.replace(x, '_')
    return string


print(normalize(enter_string))


# _________________________________________________________________________________________________________
def fibonacci(number):
    if number == 0:
        return 0
    elif len(base) == number:
        return base[number - 1]
    else:
        if len(base) < 2:
            base.append(1)
            base.append(1)
        result = base[-1] + base[-2]
        base.append(result)
        return fibonacci(number)


def main():
    n = int(input("Enter the number (maximum - 998): "))
    return fibonacci(n)


if __name__ == '__main__':
    base = []
    print(main())


# Еще вариант

def fibonacci(n):
    if n == 0:
        print(0)
    elif n < 2:
        print(1)
    else:
        f1 = f2 = 1
        print(0, f1, f2, end=' ')
        i = 2
        while i < n:
            f1, f2 = f2, f1 + f2
            print(f2, end=' ')
            i += 1


fibonacci(4)
# __________________________________________________________________________________________________________
import os


# Разобрать файлы и папки в пути


def sort_files(paths):
    for values in os.listdir(paths):
        if os.path.isdir(paths + '/' + values):
            sort_files(paths + '/' + values)
        else:
            if values.endswith(base_photo[0]):
                base_photo.append(values)
            elif values.endswith(base_video[0]):
                base_video.append(values)
            elif values.endswith(base_documents[0]):
                base_documents.append(values)
            elif values.endswith(base_music[0]):
                base_music.append(values)
            elif values.endswith(base_archives[0]):
                base_archives.append(values)
            else:
                base_unknoun.append(values)


def main():
    path = r'C:/Users/Владыка/Desktop/Разобрать'
    return sort_files(path)


if __name__ == '__main__':
    base_photo = [('jpg', 'jpeg', 'png', 'svg')]
    base_video = [('avi', 'mp4', 'mov', 'mkv')]
    base_documents = [('doc', 'docx', 'txt', 'pdf', 'xlsx', 'pptx')]
    base_music = [('mp3', 'ogg', 'wav', 'amr')]
    base_archives = [('zip', 'gz', 'tar')]
    base_unknoun = []
    main()
    print(f'Photos:\n {base_photo[1:-1]}\nVideos:\n {base_video[1:-1]}\nDocuments:\n {base_documents[1:-1]}\n'
          f'Music:\n {base_music[1:-1]}\nArchives:\n {base_archives[1:-1]}\nUnknoun:\n {base_unknoun}')
# ___________________________________________________________________________________________________________
# Создать строку, вставить запятые и перед повледним ингридиентом поставить (и)
# яйца 2шт, сахар 1 л., соль 1 чл. и уксус
test = ['яйца 2шт', 'сахар 1 л.', 'соль 1 чл.', 'уксус']


def format_ingredients(items):
    new_items = []
    if len(items) < 2:
        result = ''.join(items)
        return result
    elif len(items) == 0:
        return 'Empty list of ingredients'
    else:
        for i in items[0:-2]:
            i += ', '
            new_items.append(i)
        item = items[-2] + ' и ' + items[-1]
        new_items.append(item)
        result = ''.join(new_items)
    return result


print(format_ingredients(test))


# _______________________________________________________________________________________________________________
def lookup_key(data, value):
    base = []
    try:
        for key, val in data.items():
            if val == value:
                base.append(key)
    except AttributeError:
        return base
    return base


test2 = []
test = {1: 'susanna', 2: 'superman', 3: 'ashley', 4: 'jack', 5: 'superman'}
print(lookup_key(test, 'superman'))


# _______________________________________________________________________________________________________________

def split_list(grade):
    middle_or_less = []
    more_then_middle = []
    middle_value = sum(grade) // max(len(grade), 1)
    for i in grade:
        if i <= middle_value:
            middle_or_less.append(i)
        elif i > middle_value:
            more_then_middle.append(i)
        else:
            return middle_or_less, more_then_middle
    if len(grade) == 0:
        return middle_or_less, more_then_middle
    else:
        return middle_or_less, more_then_middle


test = [10, 25, 33, 44]
test2 = []
test3 = [50, 10]
test4 = [5]
test5 = [1, 12, 3, 24, 5]
print(split_list(test))
# _______________________________________________________________________________________________________________
from random import randint


def get_random_password():
    base = [chr(randint(40, 126)) for _ in range(8)]
    pas = ''.join(base)
    return pas


print(get_random_password())
print(chr(40))
# _______________________________________________________________________________________________________________
from random import randint


# Используя решения из предыдущих двух задач напишите функцию get_password,
# которая сгенерирует нам случайный надежный пароль и вернет его. Алгоритм простой,
# мы генерируем пароль с помощью функции get_random_password
# и если он проходит надежность проверкой функцией is_valid_password возвращаем его, если нет повторяем итерацию снова.
# Примечание: Хорошей практикой будет ограничить количество попыток (например до 100),
# чтобы не получить бесконечный цикл.


def get_random_password():
    result = ""
    count = 0
    while count < 8:
        random_symbol = chr(randint(40, 126))
        result = result + random_symbol
        count = count + 1
    return result


def is_valid_password(password):
    has_upper = False
    has_lower = False
    has_num = False
    for ch in password:
        if "A" <= ch <= "Z":
            has_upper = True
        elif "a" <= ch <= "z":
            has_lower = True
        elif "0" <= ch <= "9":
            has_num = True
    if len(password) == 8 and has_upper and has_lower and has_num:
        return True
    return False


def get_password():
    counter = 0
    while counter <= 100:
        if is_valid_password(get_random_password()):
            return get_random_password()
        else:
            is_valid_password(get_random_password())


print(get_password())
# _____________________________________________________________________________________________________________
from pathlib import Path


# Напишите функцию parse_folder, она принимает единственный параметр path,
# который является объектом Path. Функция должна просканировать директорию path
# и вернуть кортеж из двух списков. Первый это список файлов внутри директории, второй список директорий.


def parse_folder(path):
    files = []
    folders = []
    for i in path.iterdir():
        if i.is_dir():
            folders.append(i.name)
        elif i.is_file():
            files.append(i.name)
    return files, folders


test = Path('Путь....')
print(parse_folder(test))
# _____________________________________________________________________________________________________________
