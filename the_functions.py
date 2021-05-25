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
import re


def find_word(text, word):
    base = {
        'result': 0,
        'first_index': 0,
        'last_index': 0,
        'search_string': 0,
        'string': 0
    }
    find_first_index = re.search(word, text)
    if word in text:
        result = True
        base['result'] = result
        base['first_index'] = find_first_index.span()[0]
        base['last_index'] = find_first_index.span()[-1]
        base['search_string'] = find_first_index.group()
        base['string'] = text
    else:
        result = False
        base['result'] = result
        base['search_string'] = word
        base['first_index'] = None
        base['last_index'] = None
        base['string'] = text
    return base


print(find_word("Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC"
                " programming language, and first released it in 1991 as Python 0.9.0.", "Python"))
# _______________________________________________________________________________________________________________
articles_dict = [
    {
        "title": "Minim voluptate eu aliqua duis pariatur cupidatat voluptate.",
        "author": "Jhon Stark",
        "year": 2019,
    },
    {
        "title": "Dolore Lorem aliquip est labore elit labore ex consequat ad occaecat duis.",
        "author": "Artur Clark",
        "year": 2020,
    },
    {
        "title": "Aliqua minim amet ut pariatur et occaecat esse qui commodo ut duis sunt elit.",
        "author": "Silver Name",
        "year": 2021,
    },
    {
        "title": "Irure reprehenderit aliquip officia quis occaecat aute mollit laborum ullamco laboris Lorem commodo.",
        "author": "Golden Gun",
        "year": 2021,
    },
]


def find_articles(key, letter_case=False):
    base = []
    for dicts in articles_dict:
        for items in dicts.items():
            for item in items:
                try:
                    if key in item:
                        base.append(dicts)
                except TypeError:
                    continue
    return base


print(find_articles('elit'))
# __________________________________________________________________________________________________________________
test = "    +38(050)123-32-34"
test1 = "     0503451234"
test3 = "(050)8889900"
test4 = "38050-111-22-22"
test5 = "38050 111 22 11   "


def sanitize_phone_number(phone):
    base = []
    for i in phone:
        if i in ' -()+':
            continue
        base.append(i)
    real_string = ''.join(base)
    return real_string


print(sanitize_phone_number(test))


# Еще вариант
def sanitize_phone_number2(phone):
    new_phone = (
        phone.strip()
            .removeprefix("+")
            .replace("(", "")
            .replace(")", "")
            .replace("-", "")
            .replace(" ", "")
    )
    return new_phone


print(sanitize_phone_number2(test))
# ___________________________________________________________________________________________________________


def sanitize_phone_number(phone):
    new_phone = (
        phone.strip()
        .removeprefix("+")
        .replace("(", "")
        .replace(")", "")
        .replace("-", "")
        .replace(" ", "")
    )
    return new_phone


def get_phone_numbers_for_countries(list_phones):
    ua, jp, tw, sg = [], [], [], []
    countries = {'UA': [], 'JP': [], 'TW': [], 'SG': []}
    base = []
    for j in list_phones:
        base.append(sanitize_phone_number(j))
    for i in base:
        if i[0:2] == '81':
            jp.append(i)
        elif i[0:2] == '65':
            sg.append(i)
        elif i[0:3] == '886':
            tw.append(i)
        elif i[0:3] == '380':
            ua.append(i)
        else:
            ua.append(i)
    countries.update({'UA': ua, 'JP': jp, 'TW': tw, 'SG': sg})

    return countries


test = ["    +38(050)123-32-34", "     0503451234", "(050)8889900", "38050-111-22-22", "38050 111 22 11   ",
        "    +81(050)123-32-34", "     0653451234", "(886)8889900", "65050-111-22-22", "81050 111 22 11   "]
print(get_phone_numbers_for_countries(test))
# ______________________________________________________________________________________________________________


def is_spam_words(text, spam_words, space_around=False):
    if not space_around:
        for i in spam_words:
            if i in text:
                return True
            else:
                return False
    else:
        return False


print(is_spam_words("Молох", ["лох"]))  # True
print(is_spam_words("Молох", ["лох"], True))  # False
# ____________________________________________________________________________________
CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "u", "ja", "je", "ji", "g")
TRANS = {}
for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
    TRANS[ord(c)] = l
    TRANS[ord(c.upper())] = l.upper()


def translate(name):
    for i, j in TRANS.items():
        i = chr(i)
        name = name.replace(i, j)
    return name


print(translate("Дмитрий Коробов"))  # Dmitrij Korobov
print(translate("Александр Иванович"))  # Aleksandr Ivanovich

# ЕЩЕ ВАРИАНТ
TRANS2 = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'yo', 'ж': 'zh', 'з': 'z',
          'и': 'i', 'й': 'j', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r',
          'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch',
          'ъ': 'y', 'ы': 'y', 'ь': "'", 'э': 'e', 'ю': 'yu', 'я': 'ya',

          'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E', 'Ё': 'Yo', 'Ж': 'Zh', 'З': 'Z',
          'И': 'I', 'Й': 'Y', 'К': 'K', 'Л': 'L', 'М': 'M', 'Н': 'N', 'О': 'O', 'П': 'P', 'Р': 'R',
          'С': 'S', 'Т': 'T', 'У': 'U', 'Ф': 'F', 'Х': 'H', 'Ц': 'Ts', 'Ч': 'Ch', 'Ш': 'Sh', 'Щ': 'Shch',
          'Ъ': 'Y', 'Ы': 'Y', 'Ь': "'", 'Э': 'E', 'Ю': 'Yu', 'Я': 'Ya',
          }


def translate2(name):
    for i, j in TRANS2.items():
        name = name.replace(i, j)
    return name


print(translate2("Дмитрий Коробов"))  # Dmitrij Korobov
print(translate2("Александр Иванович"))  # Aleksandr Ivanovich
# _______________________________________________________________________________________________________________
grade = {"A": 5, "B": 5, "C": 4, "D": 3, "E": 3, "FX": 2, "F": 1}


def formatted_grades(students):
    base = []
    count = 0
    for v in students.items():
        count += 1
        name, val = v
        for k, i in grade.items():
            if k == val:
                base.append("{:>4}|{:<10}|{:^5}|{:^5}".format(count, name, val, i))
    return base


people = {"Nick": "A", "Olga": "B", "Mike": "FX", "Anna": "C"}

print(formatted_grades(people))

# ЕЩЕ ВАРИАНТ (КРАСИВЫЙ ВЫВОД)
grade2 = {"A": 5, "B": 5, "C": 4, "D": 3, "E": 3, "FX": 2, "F": 1}


def formatted_grades2(students):
    count = 0
    for v in students.items():
        count += 1
        name, val = v
        for k, i in grade2.items():
            if k == val:
                print("{:>4}|{:<10}|{:^5}|{:^5}".format(count, name, val, i))


people2 = {"Nick": "A", "Olga": "B", "Mike": "FX", "Anna": "C"}
formatted_grades2(people2)
# _____________________________________________________________________________________________________________


def formatted_numbers():
    num_list = []
    count = 0
    num_list.append("|{:^10}|{:^10}|{:^10}|".format("decimal", "hex", "binary"))
    for i in range(16):
        hex_count = '{:x}'.format(count)
        bin_count = '{:b}'.format(count)
        num_list.append("|{:<10}|{:^10}|{:>10}|".format(count, hex_count, bin_count))
        count += 1
    return num_list


for el in formatted_numbers():
    print(el)
# _________________________________________________________________________________________________
import re


def find_all_words(text, word):
    result = re.findall(word, text, re.IGNORECASE)
    return result


print(find_all_words("Guido PythoN van Rossum began working on Python in the late 1980s, as a successor to the ABC"
                     " programming language pYthon, and first released it PytHOn in 1991 as Python 0.9.0.", "Python"))
# _________________________________________________________________________________________________________________
import re


def replace_spam_words(text, spam_words):
    base = []
    result = ""
    for i in spam_words:
        stopper = re.findall(i, text, re.IGNORECASE)
        for x in stopper:
            base.append(x)
    base = "(" + "" + "|".join(base) + ")"
    for j in spam_words:
        result = re.sub(base, '*' * len(j), text)
    return result


print(replace_spam_words('Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC'
                         ' programming PYTHOn language, and first released pYthoN it in 1991 as Python 0.9.0. pythOn',
                         ['began', 'Python']))
# ___________________________________________________________________________________________________________________
import re


def find_all_links(text):
    result = []
    pattern = r"https?://(\w+\.)+\w+"
    iterator = re.finditer(pattern, text)
    for match in iterator:
        result.append(match.group())
    return result
# __________________________________________________________________________________
# Скрипт заходит в указанную папку с файлами, создает папки и сортирует файлы по папкам, архивы распаковывает
# содержимое архивов распаковывается в папку созданую по имени архива. Все файлы транслитерируются.
# Файлы с неизвесными расширениями остаются без изменений
import os
import shutil


def unpack_archives(paths):
    for arch in os.listdir(os.path.join(paths, 'archives')):
        archiv = 'archives'
        try:
            os.mkdir(f'{os.path.join(paths, archiv)}/{os.path.splitext(arch)[0]}')
            shutil.unpack_archive(os.path.join(os.path.join(paths, 'archives'), arch),
                                  os.path.join(os.path.join(paths, 'archives'), os.path.splitext(arch)[0]))
        except (FileExistsError, shutil.ReadError):
            continue


def normalize(name):
    trans = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'yo', 'ж': 'zh', 'з': 'z',
             'и': 'i', 'й': 'j', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r',
             'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch',
             'ъ': 'y', 'ы': 'y', 'ь': "'", 'э': 'e', 'ю': 'yu', 'я': 'ya', '`': '_', '~': '_', '!': '_',
             '@': '_', '#': '_', '$': '_', '%': '_', '^': '_', '&': '_', '*': '_', '(': '_', ')': '_',
             '-': '_', '=': '_', '+': '_', '{': '_', '}': '_', '[': '_', ']': '_', ';': '_', ':': '_', '|': '_',
             '"': '_', '/': '_', '?': '_', '>': '_', '<': '_', ',': '_',

             'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E', 'Ё': 'Yo', 'Ж': 'Zh', 'З': 'Z',
             'И': 'I', 'Й': 'Y', 'К': 'K', 'Л': 'L', 'М': 'M', 'Н': 'N', 'О': 'O', 'П': 'P', 'Р': 'R',
             'С': 'S', 'Т': 'T', 'У': 'U', 'Ф': 'F', 'Х': 'H', 'Ц': 'Ts', 'Ч': 'Ch', 'Ш': 'Sh', 'Щ': 'Shch',
             'Ъ': 'Y', 'Ы': 'Y', 'Ь': "'", 'Э': 'E', 'Ю': 'Yu', 'Я': 'Ya',
             }
    for i, j in trans.items():
        name = name.replace(i, j)
    return name


def del_empty_normalize_dirs(root_path, cur_path):
    for filename in os.listdir(cur_path):
        if os.path.isfile(os.path.join(cur_path, filename)):
            shutil.move(os.path.join(cur_path, filename), os.path.join(root_path, filename))
        elif os.path.isdir(os.path.join(cur_path, filename)):
            del_empty_normalize_dirs(root_path, os.path.join(cur_path, filename))
    if cur_path != root_path:
        os.rmdir(cur_path)
    normalize_files(root_path)


def normalize_files(path):
    for file in os.listdir(path):
        shutil.move(os.path.join(path, file), os.path.join(path, normalize(file)))
    sort_unpack_files(path)


def sort_unpack_files(root_path):
    for file in os.listdir(root_path):
        if file.endswith(base[0]):
            try:
                os.mkdir(f'{root_path}/photo')
                shutil.move(os.path.join(root_path, file), os.path.join(root_path, 'photo'))
            except FileExistsError:
                shutil.move(os.path.join(root_path, file), os.path.join(root_path, 'photo'))
        elif file.endswith(base[1]):
            try:
                os.mkdir(f'{root_path}/video')
                shutil.move(os.path.join(root_path, file), os.path.join(root_path, 'video'))
            except FileExistsError:
                shutil.move(os.path.join(root_path, file), os.path.join(root_path, 'video'))
        elif file.endswith(base[2]):
            try:
                os.mkdir(f'{root_path}/documents')
                shutil.move(os.path.join(root_path, file), os.path.join(root_path, 'documents'))
            except FileExistsError:
                shutil.move(os.path.join(root_path, file), os.path.join(root_path, 'documents'))
        elif file.endswith(base[3]):
            try:
                os.mkdir(f'{root_path}/music')
                shutil.move(os.path.join(root_path, file), os.path.join(root_path, 'music'))
            except FileExistsError:
                shutil.move(os.path.join(root_path, file), os.path.join(root_path, 'music'))
        elif file.endswith(base[4]):
            try:
                os.mkdir(f'{root_path}/archives')
                shutil.move(os.path.join(root_path, file), os.path.join(root_path, 'archives'))
            except FileExistsError:
                shutil.move(os.path.join(root_path, file), os.path.join(root_path, 'archives'))
    unpack_archives(root_path)


def main():
    path = r'C:/Users/Владыка/Desktop/Разобрать'
    flag = r'C:/Users/Владыка/Desktop/Разобрать'
    return del_empty_normalize_dirs(path, flag)


if __name__ == '__main__':
    base = [('jpg', 'jpeg', 'png', 'svg'), ('avi', 'mp4', 'mov', 'mkv'), ('doc', 'docx', 'txt', 'pdf', 'xlsx', 'pptx'),
            ('mp3', 'ogg', 'wav', 'amr'), ('zip', 'gz', 'tar')]
    main()
# _________________________________________________________________________________________________________________
import re


def read_file(path):
    with open(path, 'r') as file:
        result = list(map(int, re.findall(r'\d+', ''.join(file.readlines()))))
    return sum(result)


# должен быть создан текстовый файл с словами и цифрами
test = 'C:/Users/Владыка/PycharmProjects/Functionality/money.txt'
print(read_file(test))
# ________________________________________________________________________________________


def write_and_get_employees(employee_list, path):
    base = []
    with open(path, 'w') as write_file:
        for elements in employee_list:
            if elements == list(elements):
                for elem in elements:
                    write_file.write(elem + '\n')
            else:
                write_file.write(elements + '\n')
    with open(path, 'r') as read_file:
        read_file = read_file.readlines()
        for line in read_file:
            base.append(line)
    return base


test = [['Robert Stivenson, 28 years', 'Alex Denver, 30 years'], ['Drake Mikelsson, 19 years']]
test2 = 'C:/Users/Владыка/PycharmProjects/Functionality/money.txt'
print(write_and_get_employees(test, test2))


# ЕЩЕ ВАРИАНТ (УПОРОТЫЙ)
def write_and_get_employees(employee_list, path):
    base = []
    write_file = open(path, 'w')
    for elements in employee_list:
        if elements == list(elements):
            for elem in elements:
                write_file.write(elem + '\n')
        else:
            write_file.write(elements + '\n')
    write_file.close()
    read_file = open(path, 'r')
    for line in read_file:
        base.append(line)
    read_file.close()
    return base


test3 = [['Robert Stivenson, 28 years', 'Alex Denver, 30 years'], ['Drake Mikelsson, 19 years']]
test4 = 'C:/Users/Владыка/PycharmProjects/Functionality/money.txt'
print(write_and_get_employees(test3, test4))
# ________________________________________________________________________________________________
import re


def add_order(order, path):
    base = []
    count = 0
    with open(path, 'a') as write_file:
        write_file.write(order + '\n')
    with open(path, 'r') as read_file:
        for line in read_file:
            base.append(line)
    for element in base:
        if re.search(r'\b:active\b', element):
            count += 1
    return count


test = 'Big chicken:active'
way = 'C:/Users/Владыка/PycharmProjects/Functionality/money.txt'
print(add_order(test, way))


# ЕЩЕ ВАРИАНТ (УПОРОТЫЙ)
def add_order(order, path):
    base = []
    count = 0
    write_file = open(path, 'a')
    write_file.write(order + '\n')
    write_file.close()
    read_file = open(path, 'r')
    for line in read_file:
        base.append(line)
    for element in base:
        if re.search(r'\b:active\b', element):
            count += 1
    read_file.close()
    return count


test2 = 'Big chicken:active'
way2 = 'C:/Users/Владыка/PycharmProjects/Functionality/money.txt'
print(add_order(test2, way2))
# ___________________________________________________________________________________________


def navigate_clients(path, code):
    base = ''
    file = open(path, 'r')
    file.seek(9)
    base = base + file.readline()
    file.close()
    return base


test = 'C:/Users/Владыка/PycharmProjects/Functionality/money.txt'
test1 = 9
# print(navigate_clients(test, test1))


# Еще Вариант
def navigate_clients2(path, code):
    base = []
    result = ''
    file = open(path, 'r')
    for j in file:
        base.append(j)
    file.close()
    for elem in base:
        for i in elem:
            if i not in '1234567890\n.':
                result = result + i
    result = result.lstrip(' ')
    return result


test2 = 'C:/Users/Владыка/PycharmProjects/Functionality/money.txt'
test3 = 9
print(navigate_clients2(test2, test3))
# ________________________________________________________________________________________________________
import re


def get_ingredients(path, position_name):
    base = []
    result = []
    with open(path, 'r') as file:
        for line in file:
            base.append(line)
        for elem in base:
            if re.search(r'\b{}\b'.format(position_name), elem):
                result = elem.split(':')
                result = result[1].rstrip('\n').split(',')
    return result


test = 'C:/Users/Владыка/PycharmProjects/Functionality/money.txt'
test2 = 'Big chicken4'
print(get_ingredients(test, test2))
# ________________________________________________________________________________________


def encode_password(password):
    base = []
    for i in password.encode():
        i = hex(i)
        base.append(i)
    return base


test = 'hardpassword123'
print(encode_password(test))
# ________________________________________________________


def is_equal(utf_8_pass, utf_16_pass):
    utf_8_pass, utf_16_pass = utf_8_pass.decode('utf-8', 'ignore'), utf_16_pass.decode('utf-16', 'ignore')
    return utf_8_pass == utf_16_pass


test = 'Привет!'
test = test.encode()
print(is_equal(test, test))


# ЕЩЕ ВАРИАНТ
def is_equal2(utf_8_pass, utf_16_pass):
    utf_8_pass, utf_16_pass = utf_8_pass.decode('utf-8', 'ignore'), utf_16_pass.decode('utf-16', 'ignore')
    return utf_8_pass.casefold() == utf_16_pass.casefold()


test2 = 'Привет!'
test2 = test2.encode()
print(is_equal2(test2, test2))
# _________________________________________________________________________


def write_to_bin(path, user_info):
    base = []
    with open(path, 'wb') as file:
        for items in user_info.items():
            for item in items:
                if item == items[0]:
                    file.write(items[0].encode())
                    file.write(':'.encode())
                elif item == items[-1]:
                    file.write(items[-1].encode())
                    file.write('\n'.encode())
    with open(path, 'rb') as file2:
        # for i in file2:
        for i in file2.readlines():
            base.append(i.replace('\n'.encode(), ''.encode()).decode('utf-8', 'ignore'))
            #  base.append(i.decode('utf-8', 'ignore').replace('\n', '')
    return base


test = {'Andreiev': 'uyro18890D', 'Stivenson': 'oppjM13LL9e'}
test1 = 'C:/Users/Владыка/PycharmProjects/Functionality/money.bin'
print(write_to_bin(test1, test))
# ____________________________________________________________________________________________
# Поиск слова в строке


def solve_riddle(riddle, word_length, start_letter, reverse=False):
    base, result = [elem for elem in riddle], ''
    if not reverse:
        base.reverse()
        base = ''.join(base)
        for elem in base:
            if elem == start_letter:
                flag = base[base.index(elem): base.index(elem) + word_length]
                result = result.join(flag)
                return result
    else:
        base = ''.join(base)
        for elem in base:
            if elem == start_letter:
                flag = base[base.index(elem): base.index(elem) + word_length]
                result = result.join(flag)
                return result


test = 'mi1powrepret'
lenght_str = 3
start_let = 'r'
print(solve_riddle(test, lenght_str, start_let, True))  # power
# __________________________________________________________________________________________
# Сглаживание списка


def data_preparation(list_data):
    base = []
    for lists in list_data:
        if len(lists) > 2:
            lists.remove(min(lists))
            lists.remove(max(lists))
        for elements in lists:
            base.append(elements)
    base.sort(reverse=True)
    return base


test = [[1, 2, 3], [3, 4], [5, 6]]
test2 = [[1, 2, 3, 0], [3], [5, 6, 1, 7, 2]]
print(data_preparation(test))
# _____________________________________________________________________


def token_parser(s):
    base = s.split()
    result = []
    for elem in base:
        if elem in '0123456789':
            result.append(elem)
        else:
            for i in elem:
                result.append(i)
    return result


test = '2+ 34 -5 * 3'  # ['2', '+', '3', '4', '-', '5', '*', '3']
print(token_parser(test))
# _________________________________________________________________________


def make_request(keys, values):
    if len(keys) != len(values):
        result = {}
        return result
    else:
        result = dict(zip(keys, values))
        return result


keyss = ['first', 'second', 'third', 'fourth']
valuess = ['value1', 'value2', 'value3', 'value4']
print(make_request(keyss, valuess))  # {'first': 'value1', 'second': 'value2', ......}
# ___________________________________________________________________________________________
# Имитация набора текста на старом кнопочном телефоне (выводит числа клавиш)


def sequence_buttons(string):
    base = {
        1: '.,?!:',
        2: 'ABC',
        3: 'DEF',
        4: 'GHI',
        5: 'JKL',
        6: 'MNO',
        7: 'PQRS',
        8: 'TUV',
        9: 'WXYZ',
        0: ' '
    }
    result = []
    for letter in string:
        for key, value in base.items():
            for item in value:
                if letter.upper() == item:
                    for _ in range(0, value.index(item) + 1):
                        result.append(str(key))
    result = ''.join(result)
    return result


test = 'Hello World!'
print(sequence_buttons(test))
# _________________________________________________________________________


def file_operations(path, additional_info, start_pos, count_chars):
    base = ''
    with open(path, 'a') as file:
        file.write(additional_info)
    with open(path, 'r') as reading_file:
        while reading_file.seek(start_pos) != count_chars:
            base = base + reading_file.read(1)
            start_pos += 1
    return base


test_string = 'Hello World'
way = 'C:/Users/Владыка/PycharmProjects/Functionality/test_file.txt'
start = 0
count = len(test_string)
print(file_operations(way, test_string, start, count))
# _________________________________________________________________________________


def get_employees_by_profession(path, profession):
    with open(path, 'r') as fh:
        line_list = fh.readlines()
    result = list()
    for line in line_list:
        if line.find(profession) != -1:
            result.append(line.removesuffix('\n').strip())
    strr = ''.join(result)
    return strr.replace(profession, '').strip()
# ______________________________________________________________________________


def to_indexed(start_file, end_file):
    with open(start_file, 'r') as fh:
        row_list = fh.readlines()
    with open(end_file, 'w') as fh:
        for item in row_list:
            result = f'{row_list.index(item)}: ' + item
            fh.write(result)
# ________________________________________________________________________
# Сглаживание списка


def flatten(data):
    if len(data) == 0:
        return data
    if isinstance(data[0], list):
        return flatten(data[0]) + flatten(data[1:])
    return data[:1] + flatten(data[1:])


test = [1, 2, [3, 4, [5, 6]], 7]
test2 = []
print(flatten(test))
# ___________________________________________________________________


def encode(data, base=None):
    if not data:
        return []
    if base is None:
        base = []
    idx = 0
    next_idx = 1
    for _ in data:
        try:
            if data[idx] == data[next_idx]:
                idx += 1
                next_idx += 1
            else:
                base.append(data[idx])
                base.append(idx + 1)
                if next_idx in base:
                    encode(data[next_idx:], base)
        except IndexError:
            base.append(data[-1])
            base.append(2)
    return base[0:10]


def decode(data, *args, idx=0, next_idx=1):
    if not data:
        return data
    base = []
    for _ in data:
        try:
            for _ in range(data[next_idx]):
                base.append(data[idx])
            idx += 2
            next_idx += 2
            decode(base, idx=idx, next_idx=next_idx)
        except (TypeError, IndexError):
            return base


test = 'XXXZZXXYYYZZ'
test3 = ["X", 3, "Z", 2, "X", 2, "Y", 3, "Z", 2]
test2 = ["X", "X", "X", "Z", "Z", "X", "X", "Y", "Y", "Y", "Z", "Z"]
test1 = ''
test4 = []
print(decode(test3))  # ["X", "X", "X", "Z", "Z", "X", "X", "Y", "Y", "Y", "Z", "Z"]
print(encode(test))  # ["X", 3, "Z", 2, "X", 2, "Y", 3, "Z", 2]
# _______________________________________________________________________________________________
from datetime import datetime


def get_days_from_today(date):
    base = date.split('-')
    first = datetime(int(base[0]), int(base[1]), int(base[2]))
    second = datetime.now()
    result = second - first
    return result.days


test = '2020-10-09'
print(get_days_from_today(test))
# ________________________________________________________________________
import random


def random_winners(count, user_dict):
    dict_keys = user_dict.keys()
    random.shuffle(list(dict_keys))
    return random.sample(list(dict_keys), k=count)


print(random_winners(2, {"Oleg": 1362, "Anna": 3295, "Ira": 1234, "Boris": 3333}))
# ______________________________________________________________________________________
from decimal import Decimal, getcontext


def decimal_average(number_list, signs_count):
    getcontext().prec = signs_count
    number_list = [Decimal(x) for x in number_list]
    result = sum(number_list) / len(number_list)
    return Decimal(result)


test = [3, 5, 77, 23, 0.57]
test1 = 6
test2 = [31, 55, 177, 2300, 1.57]
test3 = 9
print(decimal_average(test2, test3))
# ____________________________________________________________________________
import math


def cil_volume(h, r, x):
    result = h * math.sin(math.radians(x)) * math.pi * r ** 2
    return result


print(cil_volume(10, 3, 5))  # Вычислить объем наклоненного цилиндра (h-высота r-радиус x-градус наклона)
# _________________________________________________________________________________________________________
import collections


def to_named(tup):
    Person = collections.namedtuple('Person', ['id', 'name', 'discount', 'city', 'age'])
    person = Person(tup[0], tup[1], tup[2], tup[3], tup[4])
    return person, person.discount


test = (1985, "Nick", 15, "Kharkiv", 34)
print(to_named(test))
# ___________________________________________________________________________________________
import collections


def count_activity(clients_activity):
    base = []
    for lists in clients_activity:
        for elements in lists:
            base.append(elements)
    res = collections.Counter(base)
    return res.most_common(1)


student_marks = [['Edvardson', 'Damriel', 'Mbape', 'Columb'], ['Edvardson', 'Mbape', 'Mbape']]
print(count_activity(student_marks))
# _________________________________________________________________________________________________
from collections import defaultdict


def group_clients(clients):
    grouped_words = defaultdict(list)
    for word in clients:
        char = word[0:2]
        grouped_words[char].append(word)
    return grouped_words


test = ['34345', '76788', '34654']
print(group_clients(test))
# _________________________________________________________
from collections import deque


def form_deque(clients_id, max_len):
    obj = deque(maxlen=max_len)
    count = 0
    count1 = -1
    for i in clients_id:
        if i % 2 == 0:
            obj.insert(count, i)
            count += 1
        else:
            obj.insert(count1, i)
    return obj


test = [1233, 4566, 1234, 7877, 2]
test1 = 5
print(form_deque(test, test1))  # deque([4566, 1234, 7877, 2, 1233], maxlen=5)
# _____________________________________________________________________________________
def modify_lists(list_for_dict, pow_dict, list_for_list, add_num):
    flag1 = {i: i ** pow_dict for i in list_for_dict}
    flag2 = [i + add_num for i in list_for_list]
    return flag1, flag2


test = [1, 3]
test1 = 2
test3 = [3, 5]
test4 = 7
# modify_lists([1,3],2,[3,5],7)
print(modify_lists(test, test1, test3, test4))  # ({1: 1, 3: 9}, [10, 12])
# ________________________________________________________________________________
