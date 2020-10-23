student_list=['emir','aijan', 'baizak', 'zarina', 'sultan']
current_list=[]
current_list_not=[]
i=0
come_in=1
while come_in !='0':
    come_in = input("Ведите имя студента")
    if come_in not in current_list:# проверяем пришел ли студент на занятия
        if come_in in student_list:# проверяем пришел ли студент на занятия
            current_list.append(come_in)# добавить студента
            print('Студент пришел на занятея')
        else:
            print('Такого студента не существует в списке')
    else:
        print('Студент уже пришел')

current_list_not=student_list
while i < len(current_list):
     if current_list[i] in current_list_not:
         current_list_not.remove(current_list[i])
     i+=1
print('список присутствующих',current_list)
print('список отсутсвующих',current_list_not)


