from copy import deepcopy
 
 
class Matrix:
    def __init__(self, list_of_lists):
        self.matrix = deepcopy(list_of_lists)
 
    def mult(self, other):
        if isinstance(other, int) or isinstance(other, float):
            result = [[other * x for x in y] for y in self.list2D]
            return Matrix(result)
        elif self.dim_C != other.dim_R:
            return 'Нельзя перемножить матрицы таких размерностей'
        else:
            a = range(self.dim_C)
            b = range(self.dim_R)
            c = range(other.dim_C)
            result = []
            for i in b:
                res = []
                for j in c:
                    el, m = 0, 0
                    for k in a:
                        m = self.list2D[i][k] * other.list2D[k][j]
                        el += m
                    res.append(el)
                result.append(res)
            return Matrix(result)
        
    def mult_(self, scalar):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                self=self.matrix[i][j]*scalar
        return self
                
    def sum(self, other):
        other = Matrix(other)
        result = []
        numbers = []
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                summa = other[i][j] + self.matrix[i][j]
                numbers.append(summa)
                if len(numbers) == len(self.matrix):
                    result.append(numbers)
                    numbers = []
        return Matrix(result)   
 
    def subt(self, other):
        other = Matrix(other)
        result = []
        numbers = []
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                raznost = other[i][j] - self.matrix[i][j]
                numbers.append(raznost)
        return Matrix(result)         
 
    def transpose(self):
       self.transpose()
       return self
