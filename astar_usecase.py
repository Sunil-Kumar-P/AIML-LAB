#use case 1
grid = [[1,1,1,1], #1-not blocked, 0 -  not blocked
        [1,1,1,1],
        [1,1,1,1],
        [1,1,0,0],
        [1,1,0,1]]

#Convert all the points to instances of node


start = grid[4][0]
goal = grid [0][3]

#use case 2
grid =[[1,1,0,0,0,1,1],
       [1,1,1,1,0,1,1],
       [1,1,1,1,0,1,1],
       [1,1,1,1,0,1,1],
       [1,1,0,0,0,1,1],
       [1,1,1,1,1,1,1],
       [1,1,1,1,1,1,1] ]

#Convert all the points to instances of node

start = grid[3][1]
goal = grid [5][5]