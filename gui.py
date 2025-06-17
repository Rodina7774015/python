gmail_logins = [
    "techlover42@gmail.com",
    "sunny.daydreamer@gmail.com",
]
flag=1
while(flag):
    user_name=input("Ввведите ваше имя :")
    while not user_name.isalpha():
        print("Вы ввели не имя ")
        user_name=input("ВВведите ваше имя:")
    user_login=input("Введите ваш логин:")
    while "@gmail.com" not in user_login:
        print("Логин не соответвует стандарту '@gmail.com' ")
        user_login=input("Введите ваш логин:")
    if not gmail_logins:
        print("Все пользователи зашли")
        break
    if user_login not in gmail_logins:
        print("В доступе отказано. ")
    else:
        gmail_logins.remove(user_login)
        print("Есть доступ к программе. ")
        full_data=f"{user_name} {user_login}"
        print(full_data)



