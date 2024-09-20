import random
import sys
from queue import Queue

dx = [1,-1,0,0,1,-1,1,-1]
dy = [0,0,1,-1,1,-1,-1,1]

def can(i,j):
    return (i < 8 and i > -1 and j < 8 and j > -1)
def set_game_grid():
    grid = []
    for i in range(0,8):
        row = [0] * 8
        grid.append(row)

    bombs = set()
    while len(bombs) < 10:
       x = random.randint(0,7)
       y = random.randint(0,7)
       bombs.add((x,y))

    for i in bombs:
       grid[i[0]][i[1]] = '*'

    for ind in bombs:
       for i in range(0,8):
           ni = ind[0] + dx[i]
           nj = ind[1] + dy[i]
           if can(ni,nj) and not (grid[ni][nj] == '*'):
               grid[ni][nj] += 1
    return grid
def set_empty_grid(val):
    grid = []
    for i in range(0,8):
        row = [val] * 8
        grid.append(row)
    return grid
def print_grid(grid):
    for i in range(0,9):
        print(i ,end= ' | ')
    for i in range(0,8):
        print(' \n-----------------------------------')
        print(i + 1,end= ' ')
        for j in range(0,8):
           print('|',grid[i][j] ,end= ' ')
    print('\n-----------------------------------')
def bfs(i,j,real_grid,fake_grid,visited):
    q = Queue()
    q.put((i,j))
    visited[i][j] = 1
    fake_grid[i][j] = real_grid[i][j]
    while(not q.empty()):
        x, y = q.get()
        for ind in range(0,8):
            ni = x + dx[ind]
            nj = y + dy[ind]
            if(can(ni,nj) and visited[ni][nj] == 0):
                if(real_grid[ni][nj] == '*'):
                    pass
                else:
                    fake_grid[ni][nj] = real_grid[ni][nj]
                    if(real_grid[ni][nj] == 0):
                        q.put((ni,nj))
                        visited[ni][nj] = 1

    return


hidden_grid = set_game_grid()
shown_grid = set_empty_grid('.')
visited = set_empty_grid(0)

rem_bombs = 10
shown_rem_bombs = 10
while rem_bombs:
    print('The remaining bombs = ',shown_rem_bombs)
    print_grid(shown_grid)
    print("enter F for flag or S for safe: ")
    status = input()
    print("enter the x , y: ")
    x = int(input())
    y = int(input())
    x -= 1 
    y -= 1
    if(status == 'F'):
        if(shown_grid[x][y] == 'F'):
            shown_grid[x][y] = '.'
            shown_rem_bombs += 1
            if(hidden_grid[x][y] == '*'):
                rem_bombs += 1
        else:
            shown_rem_bombs -= 1
            shown_grid[x][y] = 'F'
            print(shown_grid[x][y])
            if(hidden_grid[x][y] == '*'):
               rem_bombs -= 1
    else:
        if(hidden_grid[x][y] == '*'):
            print('you lost TT')
            print_grid(hidden_grid)
            sys.exit(0)
        elif(hidden_grid[x][y] == 0):
            bfs(x,y,hidden_grid,shown_grid,visited)
        else:
            shown_grid[x][y] = hidden_grid[x][y]

print("you win!!!")
print_grid(hidden_grid)
