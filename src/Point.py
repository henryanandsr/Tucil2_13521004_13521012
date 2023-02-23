import math
import sys
def calculateDistance(point1, point2):
    result=float(0)
    for i in range (len(point1)):
        result+=(point2[i]-point1[i])**2
    return math.sqrt(result)

def printAllPoint(arrayPoint):
    for i in range(len(arrayPoint)):
        print(arrayPoint[i])


def findClosestPairBruteforce(arrayPoint, dimensi, result):
    temp=float(calculateDistance(arrayPoint[0], arrayPoint[1]))
    result[0]=arrayPoint[0]
    result[1]=arrayPoint[1]
    for i in range(len(arrayPoint)):
        for j in range(len(arrayPoint)):
            if i!=j:
                if temp>calculateDistance(arrayPoint[i], arrayPoint[j]):
                    temp=calculateDistance(arrayPoint[i], arrayPoint[j])
                    result[0]=arrayPoint[i]
                    result[1]=arrayPoint[j]

def findClosestPairDnC(arr, n, dimensi, result):
    if (n==3):
        d1 = calculateDistance(arr[0],arr[1])
        d2 = calculateDistance(arr[0],arr[2])
        d3 = calculateDistance(arr[1],arr[2])
        if (d1>=d2 and d1>=d3):
            result[0]=arr[0]
            result[1]=arr[1]
            return d1
        elif (d2>=d1 and d2>=d3):
            result[0]=arr[0]
            result[1]=arr[2]
            return d2
        else:
            result[0]=arr[1]
            result[1]=arr[2]
            return d3
    elif (n==2):
        d = calculateDistance(arr[0],arr[1])
        result[0]=arr[0]
        result[1]=arr[1]
        return d
    else:
        mid = n//2
        # print(mid)
        arr1 = arr[:mid]
        # print(arr1)
        arr2 = arr[mid:]
        # print(arr2)
        d1 = findClosestPairDnC(arr1,mid,dimensi, result)
        d2 = findClosestPairDnC(arr2,mid,dimensi, result)
        d = min(d1,d2)
        tempResult=[]
        #cari titik yang paling minimum yang dibedakan dari dua sisi
        #sementara mari brute force dl ~
        if(n%2==0):
            avg=(arr[n//2][0]+arr[n//2+1][0])/2
        else:
            avg=arr[n//2][0]
        
        for i in range(len(arr)):
            if arr[i][0]<avg+d and arr[i][0]>avg-d:
                tempResult.append(arr[i])
        temp=float(calculateDistance(tempResult[0],tempResult[1]))
        for i in range (len(tempResult)):
            for j in range(len(tempResult)):
                if i!=j:
                    if temp>calculateDistance(tempResult[i],tempResult[j]):
                        temp=calculateDistance(tempResult[i],tempResult[j])
                        result[0]=tempResult[i]
                        result[1]=tempResult[j]
        return temp
                        
            
                
        
# def findClosestPairDnC
def sortArrOfPoint(arr):
    for i in range(len(arr)):
        tempx = arr[i][0]
        for j in range(i,len(arr)):
            if (tempx>=arr[j][0]):
                tempx = arr[j][0]
                idxfound = j
        temp = arr[i]
        arr[i] = arr[idxfound]
        arr[idxfound] = temp
    return arr

# tempo = [[3,1],[4,1],[2,1],[0,1],[6,1],[-1,2],[2,1]]
# print(sortArrOfPoint(tempo))