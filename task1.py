"""
    Генератор паролей.
    Пользователь выбирает 1 из 3 вариантов:
    1. Сгенерировать простой пароль (только буквы в нижнем регистре, 8 символов)
    2. Сгенерировать средний пароль (любые буквы и цифры, 8 символов)
    3. Сгенерировать сложный пароль (минимум 1 большая буква, 1 маленькая, 1 цифра и 1 спец-символ, длина от 8 до 16 символов)
        (для 3 пункта можно генерировать пароли до тех пор, пока не выполнится условие)
    Для решения использовать:
    - константы строк из модуля string (ascii_letters, digits и т.д.)
    - функцию choice из модуля random (для выборки случайного элемента из последовательности)
    - функцию randint из модуля random (для генерации случайной длины сложного пароля от 8 до 16 символов)

    Дополнительно:
    1. Позволить пользователю выбирать длину пароля, но предупреждать, что
        пароль ненадежный, если длина меньше 8 символов
    2. Добавить еще вариант генерации пароля - 4. Пользовательский пароль:
        - пользователь вводил пул символов, из которых будет генерироваться пароль
        - вводит длину желаемого пароля
        - программа генерирует пароль из нужной длины из введенных символов
        - * игнорируются пробелы
"""  # noqa: E501
import random
import string


def main():
    print(
        "Выберите сложность пароля:"
        "\n1. Простой"
        "\n2. Средний"
        "\n3. Сложный"
        )
    a = int(input())
    if a == 1:
        print(simple())
    elif a == 2:
        print(medium())
    elif a == 3:
        print(hard())
        

def simple():
    password = string.ascii_lowercase
    size = 8 
    simple = ''.join(random.choice(password) for i in range(size))
    return simple


def medium():
    password = string.ascii_letters + string.digits
    size = 8 
    medium = ''.join(random.choice(password) for i in range(size))
    return medium


def hard():
    password = string.ascii_letters + string.digits + string.punctuation
    size = random.randint(8, 16)
    hard = ''.join(random.choice(password) for i in range(size))

    specials = ''
    counter_d = counter_l = counter_u = 0

    for char in hard:
        if char.isdigit():
            counter_d += 1
        elif char.islower():
            counter_l += 1
        elif char.isupper():
            counter_u += 1
        elif not char.isspace():
            specials += char

    while counter_d == 0 or counter_l == 0 or counter_u == 0 or specials == 0:
        hard = ''.join(random.choice(password) for i in range(size))
        for char in hard:
            if char.isdigit():
                counter_d += 1
            elif char.islower():
                counter_l += 1
            elif char.isupper():
                counter_u += 1
            elif not char.isspace():
                specials += char
    else:
        return hard


if __name__ == '__main__':
    main()