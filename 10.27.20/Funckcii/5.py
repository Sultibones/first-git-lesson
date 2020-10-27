def translation():
    print(f"выберите правельный ответ как переводиться кошка:{['cat','apple']}")
    answer = input("ведите ответ:")
    if answer == 'cat':
        print('вы ответили првельно!')
    else:
        print('не правельно!')

translation()