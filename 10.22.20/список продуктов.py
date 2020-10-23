product_list=['bread','cheese','egg','meat']
cook_list=[]
print('У вас имеются такие подукты',product_list)
prduct=input("возьмите продукты")
i=1
while prduct !='0' and i<=len(product_list):
    if prduct in product_list:
        cook_list.append(prduct)
    else:
        print('используйте продукты из тарелки')
        prduct=input("Возьмите продукт")
        i=i+1
buter=['bread','sheese']
biff=['meat', 'egg']
ham=['bread','egg','meat']
ch_ham=['bread','cheese','egg','meat']
if len(cook_list) == len(buter):
    j=0
    while j <len(cook_list):
     if cook_list[j] in buter:
        j=j+1
     else:
      print('вы дали мне не тот продукт')
      break
    if j== len (buter):
                print('готовте бутерброд')
elif cook_list==biff:
    j=0
    while j<len(cook_list):
        if cook_list[j] in biff:
            j=j+1
        elif cool
            print('вы можете приготовить бутерброд')
        elif cook_list == biff:
            print('вы можете приготовить бифштекс')
        elif cook_list==ham:
            print('вы можете приготовить гамбургер ')
        elif cook_list==ch_ham:
            print('вы можете приготовить чизбургер')