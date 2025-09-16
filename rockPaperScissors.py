import random, sys

print("ROCK, PAPER, SCISSORS")
wins = 0 
losses = 0
ties = 0

while True:
    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
    while True:
        print("Enter your move: (r)ock (p)aper (s)cissor or (q)uit")
        player_move = input('>')
        if player_move == 'q':
            sys.exit()
        if player_move == 'p' or player_move == 'r' or player_move == 's':
            break
        print('Type one of r, p, s, or q')
    
    if player_move == 'r':
        print('ROCK versus...')
    elif player_move == 'p':
        print('PAPER versus...')
    elif player_move == 's':
        print('SCISSORS versus...')
    
    move_number = random.randint(1, 3)
    if move_number == 1:
        comp_move = 'r'
        print('ROCK')
    elif move_number == 2:
        comp_move = 'p'
        print('PAPER')
    elif move_number == 3:
        comp_move = 's'
        print('SCISSORS')    

    if player_move == comp_move:
        print('It is a tie!')
        ties = ties + 1
    elif player_move == 'r' and comp_move == 's':
        print('You win!')
        wins = wins + 1
    elif player_move == 'p' and comp_move == 'r':
        print('You win!')
        wins = wins + 1
    elif player_move == 's' and comp_move == 'p':
        print('You win!')
        wins = wins + 1
    elif player_move == 'r' and comp_move == 'p':
        print('You lose!')
        losses = losses + 1
    elif player_move == 'p' and comp_move == 's':
        print('You lose!')
        losses = losses + 1
    elif player_move == 's' and comp_move == 'r':
        print('You lose!')
        losses = losses + 1