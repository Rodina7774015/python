#Список доступных gmail
gmail_logins = [
    "techlover42@gmail.com",
    "sunny.daydreamer@gmail.com",
]
user_name=[]
flag=1 #На будующие так можно выйти из цикла при помощи этого флага  
while(flag):
        if not gmail_logins:#Проверка на пусоту списка 
            print("Все пользователи авторизовались")
            break
        user_input_name=input("Ввведите ваше имя :")
        while not user_input_name.isalpha():#Проверка на то что введено имя
            print("Вы ввели не имя ")
            user_input_name=input("Введите ваше имя:")
        user_login=input("Введите ваш логин:")
        while "@gmail.com" not in user_login:#Проверка на корректность 
            print("Логин не соответвует стандарту '@gmail.com' ")
            user_login=input("Введите ваш логин:") 
        if user_login not in gmail_logins:
            print("В доступе отказано. ")
        else:
            gmail_logins.remove(user_login)#Удаление из списка 
            user_name.append(user_input_name) 
            full_data=f"{user_input_name} {user_login}"#Обеденение в одной переменной f-format
            print("Есть доступ к программе. ")
            print(full_data)
number_of_names=len(user_name)#количество имен в списке 
print("Вас всего "+str(number_of_names)+"человека")#Использование конкатенации
for name in user_name:
    print(name)
