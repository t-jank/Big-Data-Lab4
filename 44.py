import random
import matplotlib.pyplot as plt
import math

def Points(n,k):
    X=[]
    for number_of_points in range(0,k):
        point=[]
        for space in range(0,n):
            point.append(random.random())
        X.append(point)
    return X

def distance(p1,p2):
    n=len(p1)
    suma=0
    for i in range(0,n):
        suma=(p1[i]-p2[i])**2
    return math.sqrt(suma)

def distances(points):
    n=len(points[0])
    sqn=math.sqrt(n)
    k=len(points)
    distances=[]
    for i in range(0,k):
        l=i+1
        for j in range(l,k):
            distances.append(distance(points[i],points[j]) / sqn)            
    return distances

n=1  # 1, 10, 100, 1000, 10000
k=100

X=Points(n,k)
d=distances(X)

plt.hist(d,bins=10,color='hotpink')
plt.xlabel('Odległość/sqrt(n)')
plt.ylabel('Liczba par punktów')
plt.title('Liczba punktów: k='+str(k)+'\n''Przestrzeń [0,1]^n: n='+str(n))
plt.show()
