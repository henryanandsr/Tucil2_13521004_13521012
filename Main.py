import src
import random

dimension = int(input("Dimensi: "))
numberOfPoints = int(input("Banyaknya Titik: "))

arrayPoint = [[0 for j in range(dimension)] for i in range (numberOfPoints)]

for i in range(numberOfPoints):
    for j in range(dimension):
        arrayPoint[i][j] = random.randint(0, 100)

src.printAllPoint(arrayPoint)
#yang bawah belum bener, baru basic
print(src.calculateDistance(arrayPoint[0],arrayPoint[1]))