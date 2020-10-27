username = 'user'
password = '1234'

def login(login,check_password):
    if login == username and check_password == password:
        return (username , password)
    else:
        return('Пароли не совподают')
(login('user','1234','1234'))