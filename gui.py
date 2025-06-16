user_name=input("Ввведите ваше имя")
gmail_logins = [
    "techlover42@gmail.com",
    "sunny.daydreamer@gmail.com",
    "quantum.leap@gmail.com",
    "starry.night@gmail.com",
    "bookworm.reader@gmail.com",
    "neon.pulse@gmail.com",
    "mystic.whisper@gmail.com",
    "urban.explorer@gmail.com",
    "luna.tides@gmail.com",
    "retro.gamer@gmail.com"
]
while not user_name.isalpha():
    print("Вы ввели не имя ")
    user_name=input("ВВведите ваше имя")
user_login=input("Введите ваш логин")
while "@gmail.com" not in user_login:
    print("Логин не соответвует ")
    user_login=input("Введите ваш логин")
if user_login not in  gmail_logins:
    print("В доступе отказано ")
full_data=f"{user_name} {user_login}"
print(full_data)



