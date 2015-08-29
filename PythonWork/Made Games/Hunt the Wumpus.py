__author__ = 'RoccoLouis'

from random import choice

cave_numbers = range(1,21)
wumpus_location = choice(cave_numbers)
player_location = choice(cave_numbers)
while player_location == wumpus_location:
    player_location = choice(cave_numbers)

print('Welcome to Hunt the Wumpus!')
print('You can see'), len(cave_numbers), ('caves')
print('To play, just type the number')
print('of the cave you wish to enter next')

while True:
    s = 'You are in cave ' + str(player_location)
    #print('You are in cave s% ' % player_location)   # this line is not working at the moment
    print(s)
    if (player_location == wumpus_location - 1 or
        player_location == wumpus_location + 1):
        print('I smell a Wumpus!')

    print('Which cave next?')
    player_location = input(">")
    if (not player_location.isdigit() or
        int(player_location) not in cave_numbers):
        print (player_location, ('Is not a cave!'))

    else:
        player_location = int(player_location)
        if player_location == wumpus_location:
            print('Aargh! You got eaten by a Wumpus!')
            break


