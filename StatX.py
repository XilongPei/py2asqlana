from numpy import ndarray

class StatX(object):

    def __init__(self, X, Y):
        self.X = X
        self.Y = Y
        #a = ndarray((5,),int)
        self._statX = [False]*X
        self._matrix = [[0]*X] * Y
        #matrix = [[0 for i in range(3)] for i in range(3)]

    def statX(self, x):
        self._statX[x] = True

    def resetX(self):
        self._statX[x] = [False]*self.X

    def statY(self, y):
        for i in range(X):
            if self._statX[x]:
                self._matrix[i,y] += 1

    def getResult(self):
        return self._matrix