
a = [
    [1, 2, 3],
    [4, 5, 6]
]

b = [
    [7, 8],
    [9, 10],
    [11, 12]
]

a2 = [
    [4,-1,3],
    [4,-2,-6],
    [2,0,3]
]
b2 = [
    [5,3,-7],
    [-1,6,-3],
    [2,-4,1]
]

def printMatrix(m):
    for i in m:
        print(*i)




def transpose(m):
    new_matrix = []
    for i in range(0, len(m[0])):
        new_matrix.append([])
        for q in range(0,len(m)):
            new_matrix[i].append(m[q][i])
    return new_matrix

def getCollumn(m, index):
    collumn = []
    for i in range(0, len(m)):
        collumn.append(m[i][index])
    return collumn

def multiplication(a, b):
    if len(a[0]) != len(b):
        return False
    new_matrix = []

    for i in range(0,len(a)):
        new_matrix.append([])
        
        for q in range(0, len(b[0])):
            row = a[i]
            collumn = getCollumn(b, q)
            element = 0
            for p in range(0, len(row)):
                element+=row[p]*collumn[p]
            new_matrix[i].append(element) 

    return new_matrix
        
# printMatrix(a)
# printMatrix(transpose(a))
printMatrix(multiplication(a2, b2))
    