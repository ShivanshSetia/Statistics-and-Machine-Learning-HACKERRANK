        ''' Hackerrank Correlation and Regression Lines - A Quick Recap #1 '''                              
         ''' Calculating Coefficent of correlation without using numpy '''
                            ''' CODE IN PYTHON 3 '''



import math as m

def conv(list1):
    return [int(i) for i in list1]        
            


def sqr(list1) :
    return [i**2 for i in list1]

def mul(lista ,listb ):
    
    list3 = [a*b for a,b in zip(lista,listb)]
        
    return list3

def r(list1,list2) :
    n = len(list1)
    numerator = n*sum(mul(list1,list2)) - sum(list1)*sum(list2)
    denominator = m.sqrt( (n*sum(sqr(list1))-sum(list1)**2)*(n*sum(sqr(list2))-sum(list2)**2)                        )
    return numerator/denominator


list1 =input() 
list2 = input()
list1 =conv(list1.split())
list2 =conv(list2.split())



print(r(list1,list2))
