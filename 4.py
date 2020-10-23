day_plan=['go to shop','clean house', 'cook smth','ear']
plan_len=len(day_plan)
i=0 #счетчик для цикла
while i<plan_len:
    action= input("ведите действие")
    if action in day_plan:
        act_index=day_plan.index(action) #находим индекс нашего действия
        if act_index==0: #действие выполняеться в приоритете, нужно выполнять действие которые сверху
            day_plan.remove(action)# дело сделано, вычеркиваем из списка
            i=i+1
        else:
            print('не торопитесь')
    else:
        print("Вы это не плонировали!")

    print(f"оставшейся дела:{day_plan}")
        