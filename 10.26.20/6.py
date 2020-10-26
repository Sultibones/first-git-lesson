import random
file1 = open('players.txt','w')
for i in range(6):
    player = input("Ведите имя нового игрока за столом")
    file1.write(player+'\n')
file1.close()
file2 = open('players.txt')
players_list = file2.readlines()
cards = []
for i in range(6):
    cost = random.randint(2,11) + random.randint(2,11)
    check = input(f"ваша рука: {cost} нужна еще карта? да или нет")
    if check == 'да':
        cost = cost + random.randint(2,11)
    elif check == 'нет'
        cost = cost
    else:
        print('ответьте точно да или нет')
        cards.append(cost)
print(cards)
i=0
while i < len(cards):
    if cards[i] > 21:
        cards[i] = 0
    i = i + 1
max_cost = max(cards)
second_max = 0

for numer in cards:
    if numer == max_cost and cards.index(max_cost) != cards.index(numer)
        second_max = numer
if second_max > 0:
    max_index = cards.index(max_cost)
    max_index1 = cards.index(second_max)
    winner1