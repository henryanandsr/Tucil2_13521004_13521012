import Point as src
import random
import time
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#ASCII ART
print("  ______   __                                            __            _______            __           ")
print(" /      \ /  |                                          /  |          /       \          /  |          ")
print("/$$$$$$  |$$ |  ______    _______   ______    _______  _$$ |_         $$$$$$$  | ______  $$/   ______  ")
print("$$ |  $$/ $$ | /      \  /       | /      \  /       |/ $$   |        $$ |__$$ |/      \ /  | /      \ ")
print("$$ |      $$ |/$$$$$$  |/$$$$$$$/ /$$$$$$  |/$$$$$$$/ $$$$$$/         $$    $$/ $$$$$$  |$$ |/$$$$$$  |")
print("$$ |   __ $$ |$$ |  $$ |$$      \ $$    $$ |$$      \   $$ | __       $$$$$$$/  /    $$ |$$ |$$ |  $$/ ")
print("$$ \__/  |$$ |$$ \__$$ | $$$$$$  |$$$$$$$$/  $$$$$$  |  $$ |/  |      $$ |     /$$$$$$$ |$$ |$$ |      ")
print("$$    $$/ $$ |$$    $$/ /     $$/ $$       |/     $$/   $$  $$/       $$ |     $$    $$ |$$ |$$ |      ")
print(" $$$$$$/  $$/  $$$$$$/  $$$$$$$/   $$$$$$$/ $$$$$$$/     $$$$/        $$/       $$$$$$$/ $$/ $$/       ")
print("=======================================================================================================")
print("                                     by 13521004 & 13521012                                            ")
print("=======================================================================================================")

# input banyaknya titik
numberOfPoints = int(input("Masukkan banyak Titik (n): "))

# input dimensi
dimension = int(input("Masukkan Dimensi: "))

# random int setiap elemen titik
arrayPoint = [[0 for j in range(dimension)] for i in range (numberOfPoints)]
for i in range(numberOfPoints):
    for j in range(dimension):
        arrayPoint[i][j] = random.uniform(0, 1000)

# sorting arrayPoint berdasarkan X membesar
arrayPoint=src.sortArrOfPoint(arrayPoint)
startTime1 = time.time()
result = src.findClosestPairDnC(arrayPoint, numberOfPoints, dimension)
print()
print("============[DIVIDE AND CONQUER]============")
print("Jarak dengan DnC "+ "{:.2f}".format(round((src.findClosestPairDnC(arrayPoint, numberOfPoints, dimension)[0]),2)) + " points")
resTimeDnC=(time.time()-startTime1)*1000
print("Waktu eksekusi DnC: " + "{:.2f}".format(round((resTimeDnC),2))+" ms")
eucCountDnC = src.eucCount
print("Euclidean Operation in DnC Count: "+str(eucCountDnC))
print()
print("===============[BRUTE FORCE]===============")
startTime2 = time.time()
print("Jarak dengan BF : "+ "{:.2f}".format(round((src.findClosestPairBruteforce(arrayPoint)[0]),2))+ " points")
resTimeBF=(time.time()-startTime2)*1000
print("Waktu eksekusi BF: " + "{:.2f}".format(round((resTimeBF),2))+" ms")
eucCountBF = src.eucCount-eucCountDnC
print("Euclidean Operation in BF Count: "+str(eucCountBF))
print("")

# visualisasi 
fig = plt.figure(figsize=(100,100))

# dimensi 3
if dimension==3:
    tempdim = str(dimension)+"d"
    ax = fig.add_subplot(111, projection=tempdim)
    for i in range(len(arrayPoint)):
        ax.scatter(arrayPoint[i][0],arrayPoint[i][1],arrayPoint[i][2],c='black',marker='o')
    for i in range(1,len(result)):    
        ax.scatter(result[i][0],result[i][1],result[i][2],c='red',marker='o')
    plt.show()
# dimensi 2
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
        plt.annotate('(%.2f,%.2f)'% xy, xy = xy)
    plt.show()