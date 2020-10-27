list =[1,2,3,4,5,6,]
def change_list(mode,number):
    if mode =='add':
        list.append(number)
    elif mode == 'remove' and number in list:
        list.remove(number)
    elif mode =='pop':
        if number >= len(list):
            print('вы вели слишком большое число')
        else:
           list.pop(number)
    else:
        print('Вы не ввели неверный мод!')

change_list('add',7)
change_list('remove',7)
change_list('pop',3)
print(list)
