
grid = ['_','_','_','_','_','_','_','_','_']

def board(grid):
    board =  f'''
    {grid[0]}|{grid[1]}|{grid[2]}
    {grid[3]}|{grid[4]}|{grid[5]}
    {grid[6]}|{grid[7]}|{grid[8]}
    '''
    print(board)

def check(grid, symbol):
    if grid[0] == grid[1] == grid[2] == symbol:
        return True
    elif grid[3] == grid[4] == grid[5] == symbol:
        return True
    elif grid[6] == grid[7] == grid[8] == symbol:
        return True
    elif grid[0] == grid[3] == grid[6] == symbol:
        return True
    elif grid[1] == grid[4] == grid[7] == symbol:
        return True
    elif grid[2] == grid[5] == grid[8] == symbol:
        return True
    elif grid[0] == grid[4] == grid[8] == symbol:
        return True
    elif grid[2] == grid[4] == grid[6] == symbol:
        return True
            

def player_choose(symbol):
    result = int(input('in which column you want to put your symbol? choose from 1 to 9\n'))
    if result in range(1, 10):
        if grid[result -1] == '_':
            grid[result - 1] = symbol
        else:
            print('this feild is not empty')
            board(grid)
            player_choose(symbol)
    else:
        print('Please Choose A Valid Number')

def check_empty(grid):
    if '_' not in grid:
        return True
        

player_char = input('Please Choose X or O: ')
board(grid)

game_on = True
while game_on:
    if player_char.upper() == 'X':
        print('Player 1 Turn')
        player_choose('X')
        board(grid)
        if check(grid, 'X'):
            print('Player 1 Won')
            game_on = False
        elif check_empty(grid) == True:
            print('it is a draw')
            game_on = False

        print('Player 2 Turn')
        player_choose('O')
        board(grid)
        if check(grid, 'O'):
            print('Player 2 Won')
            game_on = False
        elif check_empty(grid) == True:
            print('it is a draw')
            game_on = False   


    elif player_char.upper() == 'O':
        print('Player 1 Turn')
        player_choose('O')
        board(grid)
        if check(grid, 'O'):
            print('Player 1 Won')
            game_on = False
        elif check_empty(grid) == True:
            print('it is a draw')
            game_on = False

        print('Player 2 Turn')
        player_choose('X')
        board(grid)
        if check(grid, 'X'):
            print('Player 2 Won')
            game_on = False
        elif check_empty(grid) == True:
            print('it is a draw')
            game_on = False
    
    else:
        print('Please Choose A Valid Symbol')
        player_char = input('Please Choose X or O: ')

