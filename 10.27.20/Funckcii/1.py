user_db = ''
password_db =''
def register(username,password,repeat_password):
    if password == repeat_password:
        user_db = username

        return user_db, password_db
    else:
        return'Пароли не совподают'
print(register('sulti','666','666'))