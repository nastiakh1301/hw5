"""
    Необходимо реализовать форму регистрации пользователей.
    Поля формы: номер телефона, email, пароль и подтверждение пароля.
    пункты с ** - дополнительно, но не обязательно (не влияет на оценку)

    1. Пользователь вводит номер телефона.
        Программа проверяет валидность телефона:
        - приводит номер к формату 380501234567
        - если номер не получается привести к нужному формату
            то запрашивает ввод номера еще раз
            и так до тех пор, пока не будет введен валидный номер

    2. Пользователь вводит email.
        Программа проверяет валидность email:
        - должен иметь длину 6 символов и больше
            (функция len())
        - содержать один символ '@'
            (строчный метод count())
        - ** содержать логин и полный домен (логин@полный.домен)
        Пользователь может вводить email до тех пор, пока он не будет валидным.

    3. Пользователь ввод пароль.
        Программа проверяет надежность пароля:
        - минимум 8 символов
            (функция len())
        - пароль не должен содержать пробельные символы
            (строчный метод isspace())
        - наличие минимум 1 буквы в верхнем регистре, 1 в нижнем и 1 цифры
            (строчные методы isupper(), islower(), isdigit())
        - ** наличие минимум 1 спец символа

    4. После успешного ввода пароля пользователь вводит подтверждение пароля.
        Если подтверждение пароля не сходится с введенным паролем,
        то возвращаемся к пункту 3.

    Программа выводит сообщение:
    Поздравляем с успешной регистрацией!
    Ваш номер телефона: +380501234567
    Ваш email: example@mail.com
    Ваш пароль: ********** (кол-во  == кол-ву символов пароля)
"""
def main():
    mobile()
    mail()
    parol()
    print(
        "Поздравляем с успешной регистрацией!"
        f"\nВаш номер телефона: {phone}"
        f"\nВаш email: {email}"
        f"\nВаш пароль: {password}"
    )


def mobile():
    phone = input('Enter phone number: ')

    digits = ''
    for char in phone:
        if char.isdigit():
            digits += char

    if len(digits) >= 9:
        phone = '380' + digits[-9:]
        print(phone)
    else:
        print('Wrong format.')
        return mobile()
    return phone    


def mail():
    email = input('Enter email: ')

    if len(email) >= 6 and email.count('@') == 1:
        print(email)
    else:
        print('Wrong format.')
        return mail()
    return email   


def parol():
    password = input('Enter password: ')

    if len(password) >= 8 and password.isspace() is False:
        counter_d = counter_l = counter_u = 0

        for char in password:
            if char.isdigit():
                counter_d += 1
            elif char.islower():
                counter_l += 1
            elif char.isupper():
                counter_u += 1

        while counter_d != 0 and counter_l != 0 and counter_u != 0:
            print(password)
            break

    else:
        print('Wrong format.')
        return parol()

    copy_pass = input('Confirm password: ')
    if copy_pass == password:
        print('*' * len(password))
    else:
        return parol() 
    return password


if __name__ == '__main__':
    main()