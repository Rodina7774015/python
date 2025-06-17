#Список доступных gmail
gmail_logins = [
    "techlover42@gmail.com",
    "sunny.daydreamer@gmail.com",
]
flag=1 #На будующие так можно выйти из цикла при помощи этого флага  
while(flag):
    user_name=input("Ввведите ваше имя :")
    while not user_name.isalpha():#Проверка на то что введено имя
        print("Вы ввели не имя ")
        user_name=input("Введите ваше имя:")
    user_login=input("Введите ваш логин:")
    while "@gmail.com" not in user_login:#Проверка на корректность 
        print("Логин не соответвует стандарту '@gmail.com' ")
        user_login=input("Введите ваш логин:")
    if not gmail_logins:#Проверка на пусоту списка 
        print("Все пользователи авторизовались")
        break
    if user_login not in gmail_logins:
        print("В доступе отказано. ")
    else:
        gmail_logins.remove(user_login)#Удаление из списка 
        print("Есть доступ к программе. ")
        full_data=f"{user_name} {user_login}"#Обеденение в одной переменной f-format
        print(full_data)



