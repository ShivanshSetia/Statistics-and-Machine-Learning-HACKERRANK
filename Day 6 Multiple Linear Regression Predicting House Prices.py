     ''' Hackerrank Day 6: Multiple Linear Regression: Predicting House Prices '''


                                ''' CODE IN PYTHON 3 '''


import numpy as np

def conv(lista) :
    return[float(i) for i in lista]

def addfeature(lista):
    for i in lista :
        i.append(1)
    return lista

def features(fmatrix,n) :
    lista =  [i[:n] for i in fmatrix ]
    return addfeature(lista)
def output(fmatrix) :
    lista = []
    for i in fmatrix:
        lista.append(i[-1])
    return lista 

def calcweights(ftr , out):
    return np.linalg.pinv(ftr).dot(out)
    

def predict(t , tempmatr , fmatrix , n  ) :
    ftr = np.asarray(features(fmatrix,n))
    out = np.asarray(output(fmatrix))
    wts = calcweights(ftr,out)
    
    for i in tempmatr.dot(wts) :
        i = round(i,2)
        print(i)

f = conv (input().split())
n = int(f[0] )
m =int(f[1])


fmatrix =  [[j for j in conv(input().strip().split())] for i in range(m)] 
t = int(input())
tempmatr = [[j for j in conv(input().strip().split())] for i in range(t)] 
tempmatr= np.asarray (addfeature(tempmatr) )
predict(t , tempmatr , fmatrix , n)
