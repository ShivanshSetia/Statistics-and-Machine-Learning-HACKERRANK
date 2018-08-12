        ''' Hackerrank Correlation and Regression Lines - A Quick Recap #2 '''
        ''' Calculating slope of regression line without using numpy '''
                       ''' CODE IN PYTHON 3 '''
    



def mul(x,y) :
    lista=[]
    for i in range(len(x)) :
        lista.append(x[i]*y[i])
    return lista

def sqr(var) :
    return [i**2 for i in var]

x = [15 , 12 , 8 ,  8 ,  7 ,  7 ,  7 ,  6 ,  5 ,  3]
y =  [10 , 25 , 17 , 11 , 13 , 17 , 20 , 13 , 9 ,  15 ]
n = len(x)
num = n *sum(mul(x,y)) - sum(x)*sum(y)
den = n*sum(sqr(x)) - sum(x)**2
print(round((num/den),3) )
