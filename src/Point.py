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

def findClosestPairBruteforce(arrayPoint, result):
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
def findClosestPairBF(arr,n,dimensi):
    if (n==3):
        d1 = calculateDistance(arr[0],arr[1])
        d2 = calculateDistance(arr[0],arr[2])
        d3 = calculateDistance(arr[1],arr[2])
        if (d1>=d2 and d1>=d3):
            return d1
        elif (d2>=d1 and d2>=d3):
            return d2
        else:
            return d3
    elif (n==2):
        d = calculateDistance(arr[0],arr[1])
        return d
    else:
        mid = n//2
        arr1 = arr[:mid]
        arr2 = arr[mid:]
        d1 = findClosestPairBF(arr1,mid,dimensi)
        d2 = findClosestPairBF(arr2,mid,dimensi)
        d = min(d1,d2)
          #cari titik yang paling minimum yang dibedakan dari dua sisi
        #sementara mari brute force dl ~
        minDistOp = 999999
        for i in range (len(arr1)):
            for j in range (len(arr2)):
                temp = calculateDistance(arr1[i],arr2[j])
                if (minDistOp>temp):
                    minDistOp = temp
    if (n==2 or n==3):
        return d
    else :
        if (minDistOp<d):
            return minDistOp
        else:
            return d
def findClosestPairDnC(arr, n, dimensi):
    if (n==3):
        d1 = calculateDistance(arr[0],arr[1])
        d2 = calculateDistance(arr[0],arr[2])
        d3 = calculateDistance(arr[1],arr[2])
        if (d1>=d2 and d1>=d3):
            ret = []
            ret.append(d1)
            ret.append(arr[0])
            ret.append(arr[1])
            return ret
        elif (d2>=d1 and d2>=d3):
            ret = []
            ret.append(d2)
            ret.append(arr[0])
            ret.append(arr[2])
            return ret
        else:
            ret = []
            ret.append(d3)
            ret.append(arr[1])
            ret.append(arr[2])
            return ret
    elif (n==2):
        d = calculateDistance(arr[0],arr[1])
        ret = []
        ret.append(d)
        ret.append(arr[0])
        ret.append(arr[1])
        return ret
    else:
        mid = n//2
        # print(mid)
        arr1 = arr[:mid]
        # print(arr1)
        arr2 = arr[mid:]
        # print(arr2)
        d1 = findClosestPairDnC(arr1,mid,dimensi)
        d2 = findClosestPairDnC(arr2,mid,dimensi)
        d = min(d1[0],d2[0])
        if(d1[0]<d2[0]):
            ret = d1
        else:
            ret = d2
        tempResult=[]
        #cari titik yang paling minimum yang dibedakan dari dua sisi
        #sementara mari brute force dl ~
        if(n%2==0):
            avg=(arr[n//2][0]+arr[n//2+1][0])/2
        else:
            avg=arr[n//2][0]
        
        for i in range(len(arr)):
            if arr[i][0]<=avg+d and arr[i][0]>=avg-d:
                tempResult.append(arr[i])
        # print("Temporary result dg n " + str(n))
        # print(tempResult)
        if (len(tempResult)>=2):
            temp=float(calculateDistance(tempResult[0],tempResult[1]))
            ti = 0
            tj = 1
            for i in range (len(tempResult)):
                for j in range(len(tempResult)):
                    if i!=j:
                        if temp>calculateDistance(tempResult[i],tempResult[j]):
                            temp=calculateDistance(tempResult[i],tempResult[j])
                            ti = i
                            tj = j
        if (len(tempResult)>=2):
            if(temp<d):
                ret = [temp,tempResult[ti],tempResult[tj]]
                return ret
            else:
                return ret
        else:
            return ret
                        
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