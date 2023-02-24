import Point as src
import random
import time
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#Problem
# 1. Pencarian antara dua sisi berbeda masih brute force
# 3. Menemukan titik
# 4. Jumlah aksi yang dilakukan (ini bisa dilakuin klo udh bener di bagian nomer 1)
# 5. Plotting (kurang kalau beda2 dimensi)
# 6. Dimensi berbeda (sebenernya yang sekarang ini bisa cmn gabisa banyak2 karena brute force)
# 7. Banyaknya fungsi dipanggil

dimension = int(input("Dimensi: "))
numberOfPoints = int(input("Banyaknya Titik: "))
# dimension = 2
# numberOfPoints = 10
arrayPoint = [[0 for j in range(dimension)] for i in range (numberOfPoints)]
# arrayPoint = [[1,2],[1,4],[1,1],[2,1],[7,3],[5,3],[2,4],[0,0],[9,5],[3,6]]
for i in range(numberOfPoints):
    for j in range(dimension):
        arrayPoint[i][j] = random.randint(0, 1000)

arrayPoint=src.sortArrOfPoint(arrayPoint)
# src.printAllPoint(arrayPoint)
# src.printAllPoint(arrayPoint)
#yang bawah belum bener, baru basic

#pecah ke dua bagian
startTime = time.time()
result = src.findClosestPairDnC(arrayPoint, numberOfPoints, dimension)
# src.printAllPoint(result)
# print(src.calculateDistance(src.findClosestPairDnC(arrayPoint, numberOfPoints, dimension)[1],src.findClosestPairDnC(arrayPoint, numberOfPoints, dimension)[2]))
# print("Jarak "+str(src.findClosestPairDnC(arrayPoint, numberOfPoints, dimension)[0]))
# print("Jarak dg BF : " + str(src.findClosestPairBF(arrayPoint,numberOfPoints,dimension)[0]))
print("Jarak dg BF2 : " + str(src.findClosestPairBruteforce(arrayPoint)))
# print("Titik dg BF : " + str(src.findClosestPairBF(arrayPoint,numberOfPoints,dimension)[1] + src.findClosestPairBF(arrayPoint,numberOfPoints,dimension)[2]))
# print("Titik dg DNC : " + str(result[1]) + str(result[2]))
# print("Waktu eksekusi : " + str(time.time()-startTime))
print(src.eucCount)

#visualisasi 
fig = plt.figure(figsize=(100,100))
if dimension==3:
    tempdim = str(dimension)+"d"
    ax = fig.add_subplot(111, projection=tempdim)
    for i in range(len(arrayPoint)):
        ax.scatter(arrayPoint[i][0],arrayPoint[i][1],arrayPoint[i][2],c='black',marker='o')
    for i in range(1,len(result)):    
        ax.scatter(result[i][0],result[i][1],result[i][2],c='red',marker='o')
    plt.show()
elif dimension==2:
    for i in range(len(arrayPoint)):
        plt.scatter(arrayPoint[i][0],arrayPoint[i][1],color = 'black')
    for i in range(1,len(result)):
        plt.scatter(result[i][0],result[i][1],color = 'red')
    x = []
    y = []
    for i in range(len(arrayPoint)):
        x.append(arrayPoint[i][0])
        y.append(arrayPoint[i][1])
    for xy in zip(x,y):
        plt.annotate('(%.0f,%.0f)'% xy, xy = xy)
    plt.show()