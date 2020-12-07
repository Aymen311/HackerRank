#!/usr/bin/python

def displayPathtoPrincess(n,grid):
    
    if grid[0][0] == 'p' or grid[0][0] == 'P' : 
        dir1 = "LEFT"
        dir2 = "UP"
    elif grid[n-1][n-1] == 'p' or grid[n-1][n-1] == 'P' : 
        dir1 = "RIGHT"
        dir2 = "DOWN"
    elif grid[n-1][0] == 'p' or grid[n-1][0] == 'P' : 
        dir1 = "LEFT"
        dir2 = "DOWN"
    elif grid[0][n-1] == 'p' or grid[0][n-1] == 'P' : 
        dir1 = "RIGHT"
        dir2 = "UP"
    for i in range(0, n//2):
        print(dir1)
        print(dir2)
    
    
    
        
    


m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())

displayPathtoPrincess(m,grid)
