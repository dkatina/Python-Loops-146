import random

#Random package, imports alot of functions that give us the thrill of chance

# .randint(start, stop) will give you a random number between the start and stop INCLUSIVE

print(random.randint(1,6))


players = ['Dylan', 'Clinton', 'Harsh']


for player in players:
    roll = random.randint(1,6)
    print(player, 'rolled a :', roll)

# .shuffle(list) mixes the order of the list randomly

chores = ['Dishes', 'Laundry', 'Dust', 'Take Dog Out']

random.shuffle(chores)

print('This is the order Im doing my chores!')
for chore in chores:
    print(chore)


pass
# name = 'dylan'

# random.shuffle(name)

# print('Unscramble this name:', name)


#--- .choice(list) returns a random item from that list

game = ['Rock', 'Paper', 'Scissors']

while True:
    my_choice = input('Rock, Paper, Scissors, SHOOT!: ')
    computer = random.choice(game)
    print('Computer chose:', computer)
    win = input('Did you win? yes or no ')
    if win == 'yes':
        print('Nice Work!')
        print('According to you', my_choice, 'beats', computer)
        break
