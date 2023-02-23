import src
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
result=[[0 for j in range(dimension)] for i in range (2)]
arrayPoint = [[0 for j in range(dimension)] for i in range (numberOfPoints)]
for i in range(numberOfPoints):
    for j in range(dimension):
        arrayPoint[i][j] = random.randint(0, 1000)

arrayPoint=src.sortArrOfPoint(arrayPoint)
# src.printAllPoint(arrayPoint)
#yang bawah belum bener, baru basic

#pecah ke dua bagian
startTime = time.time()
src.findClosestPairDnC(arrayPoint, numberOfPoints, dimension, result)
src.printAllPoint(result)
print("Jarak "+str(src.calculateDistance(result[0],result[1])))
print("Waktu eksekusi : " + str(time.time()-startTime))

#visualisasi 
fig = plt.figure(figsize=(100,100))
if dimension==3:
    tempdim = str(dimension)+"d"
    ax = fig.add_subplot(111, projection=tempdim)
    for i in range(len(arrayPoint)):
        ax.scatter(arrayPoint[i][0],arrayPoint[i][1],arrayPoint[i][2],c='black',marker='o')
    for i in range(len(result)):    
        ax.scatter(result[i][0],result[i][1],result[i][2],c='red',marker='o')
    plt.show()
elif dimension==2:
    for i in range(len(arrayPoint)):
        plt.scatter(arrayPoint[i][0],arrayPoint[i][1],color = 'black')
    for i in range(len(result)):
        plt.scatter(result[i][0],result[i][1],color = 'red')
    plt.show()