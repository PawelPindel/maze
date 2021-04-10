
maze = [['*', '*', '*', '*', '*', '*', '*'], ['*', 'o', ' ', ' ', ' ', ' ', '*'], ['*', ' ', 'x', '*', '*', '*', '*'], ['*', ' ', ' ', ' ', ' ', ' ', '*'], ['*', '*', '*', '*', '*', '*', '*']]



def printMaze():
    print(maze[0])
    print(maze[1])
    print(maze[2])
    print(maze[3])
    print(maze[4])

exitFound = False
allPos = False
orient = ['up', 'down', 'left', 'right']
dire = orient[0]


while(exitFound == False):
    for col in maze:
        for row in col:
            if('o' == row):            
                x = maze.index(col)
                y = col.index('o')
    printMaze()
    print('Current position: ' + str(x) + ',' + str(y) + ' facing: ' + dire)
    print()
    if(dire == 'up'):
        if(maze[x-1][y] == 'x'):
            exitFound = True
            break
        elif(maze[x-1][y] == ' '):
            maze[x-1][y] = 'o'
            maze[x][y] = ' '
            dire = 'up'
        elif(maze[x][y + 1] == 'x'):
            exitFound = True
            break
        elif(maze[x][y + 1] == ' '):
            maze[x][y+1] = 'o'
            maze[x][y] = ' '
            dire = 'right'
        elif(maze[x][y - 1] == 'x'):
            exitFound = True
            break
        elif(maze[x][y - 1] == ' '):
            maze[x][y-1] = 'o'
            maze[x][y] = ' '
            dire = 'left'
        elif(maze[x+1][y] == 'x'):
            exitFound = True
            break
        elif(maze[x+1][y] == ' '):
            maze[x+1][y] = 'o'
            maze[x][y] = ' '
            dire = 'down'
    elif(dire == 'right'):
        if(maze[x][y + 1] == 'x'):
            exitFound = True
            break
        elif(maze[x][y + 1] == ' '):
            maze[x][y+1] = 'o'
            maze[x][y] = ' '
            dire = 'right'
        elif(maze[x+1][y] == 'x'):
            exitFound = True
            break
        elif(maze[x+1][y] == ' '):
            maze[x+1][y] = 'o'
            maze[x][y] = ' '
            dire = 'down'
        elif(maze[x-1][y] == 'x'):
            exitFound = True
            break
        elif(maze[x-1][y] == ' '):
            maze[x-1][y] = 'o'
            maze[x][y] = ' '
            dire = 'up'
        elif(maze[x][y - 1] == 'x'):
            exitFound = True
            break
        elif(maze[x][y - 1] == ' '):
            maze[x][y-1] = 'o'
            maze[x][y] = ' '
            dire = 'left'
        
    elif(dire == 'left'):
        if(maze[x][y - 1] == 'x'):
            exitFound = True
            break
        elif(maze[x][y - 1] == ' '):
            maze[x][y-1] = 'o'
            maze[x][y] = ' '
            dire = 'left'
        elif(maze[x-1][y] == 'x'):
            exitFound = True
            break
        elif(maze[x-1][y] == ' '):
            maze[x-1][y] = 'o'
            maze[x][y] = ' '
            dire = 'up'
        elif(maze[x+1][y] == 'x'):
            exitFound = True
            break
        elif(maze[x+1][y] == ' '):
            maze[x+1][y] = 'o'
            maze[x][y] = ' '
            dire = 'down'
        elif(maze[x][y + 1] == 'x'):
            exitFound = True
            break
        elif(maze[x][y + 1] == ' '):
            maze[x][y+1] = 'o'
            maze[x][y] = ' '
            dire = 'right'      
    elif(dire == 'down'):
        if(maze[x+1][y] == 'x'):
            exitFound = True
            break
        elif(maze[x+1][y] == ' '):
            maze[x+1][y] = 'o'
            maze[x][y] = ' '
            dire = 'down'
        elif(maze[x][y - 1] == 'x'):
            exitFound = True
            break
        elif(maze[x][y - 1] == ' '):
            maze[x][y-1] = 'o'
            maze[x][y] = ' '
            dire = 'left'
        elif(maze[x][y + 1] == 'x'):
            exitFound = True
            break
        elif(maze[x][y + 1] == ' '):
            maze[x][y+1] = 'o'
            maze[x][y] = ' '
            dire = 'right'
        elif(maze[x-1][y] == 'x'):
            exitFound = True
            break
        elif(maze[x-1][y] == ' '):
            maze[x-1][y] = 'o'
            maze[x][y] = ' '
            dire = 'up'                   
    

if(exitFound == True):
    print('Exit Found')
    



