class Matrix:
    def __init__(self, array2d):
        self.array = array2d
    def rowCount(self):
        return len(self.array)
    def colCount(self):
        return len(self.array[0])
    def __add__(self, M2):
        newMatrix = [[self.array[x][y]+M2.array[x][y] for y in range(self.colCount())] for x in range(self.rowCount())]
        return Matrix(newMatrix)
    def __sub__(self, M2):
        newMatrix = [[self.array[x][y]-M2.array[x][y] for y in range(self.colCount())] for x in range(self.rowCount())]
        return Matrix(newMatrix)
    def __mul__(self, M2):
        m1 = self.array
        m2 = M2.array
        x1, y1, x2, y2 = len(m1[0]), len(m1), len(m2[0]), len(m2)
        if(x1!=y2):
            return("Error. Bad Matrix")
        x3, y3, c = x2, y1, x1
    
        Result = [[0 for x in range(x3)] for y in range(y3)]
        for x in range(x3):
            for y in range(y3):
                answer = 0
                for i in range(c):
                    product = m1[x][i] * m2[i][y]
                    answer+=product
                Result[x][y] = answer
        
        return(Matrix(Result))
