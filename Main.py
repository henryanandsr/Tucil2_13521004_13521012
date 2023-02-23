import src
import random
import time
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#Problem
# 1. Pencarian antara dua sisi berbeda masih brute force
# 2. Mencari jumlah titik ganjil masih error
# 3. Menemukan titik
# 4. Jumlah aksi yang dilakukan (ini bisa dilakuin klo udh bener di bagian nomer 1)
# 5. Plotting (kurang kalau beda2 dimensi)
# 6. Dimensi berbeda (sebenernya yang sekarang ini bisa cmn gabisa banyak2 karena brute force)
dimension = int(input("Dimensi: "))
numberOfPoints = int(input("Banyaknya Titik: "))
result=[[0 for j in range(dimension)] for i in range (2)]
arrayPoint = [[0 for j in range(dimension)] for i in range (numberOfPoints)]
for i in range(numberOfPoints):
    for j in range(dimension):
        arrayPoint[i][j] = random.randint(0, 10)

# src.printAllPoint(arrayPoint)
#yang bawah belum bener, baru basic

#pecah ke dua bagian
startTime = time.time()
src.findClosestPairBruteforce(arrayPoint,dimension,result)
src.printAllPoint(result)
print("Jarak "+str(src.calculateDistance(result[0],result[1])))
print("Waktu eksekusi : " + str(time.time()-startTime))

#visualisasi 
fig = plt.figure(figsize=(100,100))
tempdim = str(dimension)+"d"
ax = fig.add_subplot(111, projection=tempdim)
for i in range(len(arrayPoint)):
    ax.scatter(arrayPoint[i][0],arrayPoint[i][1],arrayPoint[i][2],c='black',marker='o')
for i in range(len(result)):    
    ax.scatter(result[i][0],result[i][1],result[i][2],c='red',marker='o')
plt.show()