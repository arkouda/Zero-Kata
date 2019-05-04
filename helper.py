import random

def proPlayer(matrix,player,oppon):
    gridSize = len(matrix)
    #print(player,oppon)         
    move = MakeorBlockMove(matrix,player)
    if move != [] : 
        return move
    move = MakeorBlockMove(matrix,oppon)
    if move != [] :
        return move
    if all([all([matrix[i][j]=='' for j in range(gridSize)]) for i in range(gridSize)]) :
        choices = [[0,0],[0,gridSize-1],[gridSize-1,0],[gridSize-1,gridSize-1]]
        choices.append([(gridSize-1)//2,(gridSize-1)//2])
        if gridSize % 2 == 0 :
            choices.append([1+(gridSize-1)//2,1+(gridSize-1)//2])
        return choices[random.randint(0,len(choices)-1)]
    return noobplayer(matrix)

def MakeorBlockMove(matrix,player):
    gridSize = len(matrix)
    if matrix[0][0] == '':
        if all([matrix[k][k]==player for k in range(1,gridSize)]) or \
            all([matrix[0][k]==player for k in range(1,gridSize)]) or \
                all([matrix[k][0]==player for k in range(1,gridSize)]):
                return ([0,0])
    if matrix[0][0] == player:
        temp = gridSize - 2
        returnPos = []
        for i in range(1,gridSize):
            if matrix[i][i] == player:
                temp -= 1
            elif matrix[i][i] == '' and returnPos == []:
                returnPos = [i,i]
            else:
                break
        if temp == 0 and returnPos != [] :
            return returnPos
        
        temp = gridSize - 2
        returnPos = []
        for i in range(1,gridSize):
            if matrix[0][i] == player:
                temp -= 1
            elif matrix[0][i] == '' and returnPos == []:
                returnPos = [0,i]
            else:
                break
        if temp == 0 and returnPos != [] :
            return returnPos
        
        temp = gridSize - 2
        returnPos = []
        for i in range(1,gridSize):
            if matrix[i][0] == player:
                temp -= 1
            elif matrix[i][0] == '' and returnPos == []:
                returnPos = [i,0]
            else:
                break
        if temp == 0 and returnPos != [] :
            return returnPos

    for m in range(1,gridSize-1):
        if matrix[0][m] == '' and all([matrix[k][m]==player for k in range(1,gridSize)]) :
            return [0,m]
        if matrix[0][m] == player:
            temp = gridSize - 2
            returnPos = []
            for i in range(1,gridSize):
                if matrix[i][m] == player:
                    temp -= 1
                elif matrix[i][m] == '' and returnPos == []:
                    returnPos = [i,m]
                else:
                    break
            if temp == 0 and returnPos != [] :
                return returnPos
    if matrix[0][gridSize-1] == '' and \
        (all([matrix[i][gridSize-1-i]==player for i in range(1,gridSize)]) or \
            all([matrix[i][gridSize-1]==player for i in range(1,gridSize)])) :
            return [0,gridSize-1]
    if matrix[0][gridSize-1] == player :
        temp = gridSize - 2
        returnPos = []
        for i in range(1,gridSize):
            if matrix[i][gridSize-1-i] == player:
                temp -= 1
            elif matrix[i][gridSize-1-i] == '' and returnPos == []:
                returnPos = [i,gridSize-1-i]
            else:
                break
        if temp == 0 and returnPos != [] :
            return returnPos
        
        temp = gridSize - 2
        returnPos = []
        for i in range(1,gridSize):
            if matrix[i][gridSize-1] == player:
                temp -= 1
            elif matrix[i][gridSize-1] == '' and returnPos == []:
                returnPos = [i,gridSize-1]
            else:
                break
        if temp == 0 and returnPos != [] :
            return returnPos

    for m in range(1,gridSize-1):
        if matrix[m][0] == '' and all([matrix[m][k]==player for k in range(1,gridSize)]) :
            return [m,0]
        if matrix[m][0] == player:
            temp = gridSize - 2
            returnPos = []
            for i in range(1,gridSize):
                if matrix[m][i] == player:
                    temp -= 1
                elif matrix[m][i] == '' and returnPos == []:
                    returnPos = [m,i]
                else:
                    break
            if temp == 0 and returnPos != [] :
                return returnPos

    if matrix[gridSize-1][0] == '' and all([matrix[gridSize-1][i]==player for i in range(1,gridSize)]) :
        return [gridSize-1,0]
    if matrix[gridSize-1][0] == player :
        temp = gridSize - 2
        returnPos = []
        for i in range(1,gridSize):
            if matrix[gridSize-1][i] == player:
                temp -= 1
                print(temp)
            elif matrix[gridSize-1][i] == '' and returnPos == []:
                returnPos = [gridSize-1,i]
            else:
                break
        if temp == 0 and returnPos != [] :
            print("here")
            return returnPos
    return []

def noobplayer(matrix):
    choices = []
    n =len(matrix)
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == '':
                choices.append([i,j])
    return choices[random.randint(0,len(choices)-1)]

def hasPlayerWon(i,j,n,matrix):
    checkFor =  matrix[i][j]
    if (i+j) == (n-1) and i != j:
        return all([matrix [i][x] == checkFor for x in range(n)]) or \
            all([matrix [x][j] == checkFor for x in range(n)]) or \
            all([matrix [x][n-x-1] == checkFor for x in range(n)])
    elif i == j and (i+j) != (n-1):
        return all([matrix [i][x] == checkFor for x in range(n)]) or \
            all([matrix [x][j] == checkFor for x in range(n)]) or \
            all([matrix [x][x] == checkFor for x in range(n)])
    elif i == j and (i+j) == (n-1) :
        return all([matrix [i][x] == checkFor for x in range(n)]) or \
            all([matrix [x][j] == checkFor for x in range(n)]) or \
            all([matrix [x][x] == checkFor for x in range(n)]) or \
            all([matrix [x][n-x-1] == checkFor for x in range(n)])
    else :
        return all([matrix [i][x] == checkFor for x in range(n)]) or \
            all([matrix [x][j] == checkFor for x in range(n)])
        
