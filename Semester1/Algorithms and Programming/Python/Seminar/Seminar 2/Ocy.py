from math import sqrt
def isPrime(n):
    for i in range(2,int(sqrt(n))):
        if n%i==0:
            return False
    return True
def getHighestPrime(n):
    for i in range(n,2,-1):
        if isPrime(i)==True:
            return i
    return 1

def explosion(s):
    final=""
    for i in range(0,len(s)):
        final=final+s[:i+1]
    return final

def stringMatch(s1,s2):
    count=0
    length=min(len(s1),len(s2))
    for i in range (0,length):
        if (s1[i:i+2]==s2[i:i+2]):
            count+=1
    return count

def listesunt(l):
    m=0
    for i in range (len(l)):
        if l[i]%2==0:
            m+=1
    return m

def readlist():
    l=[]
    while True:
        n=int(input("n= "))
        if(n==-1):
            break
        l.append(n)
    return l

def sumList(l):
    sum=0
    for i in range(len(l)):
        if(l[i]!=13):
            sum+=l[i]
    return sum

def minMaxList(l):
    min=max=l[0]
    for i in range(len(l)):
        if l[i]>max:
            max=l[i]
        if l[i]<min:
            min=l[i]
    return [min,max]

def verifyInList(l,x):
    for elem in l:
        if elem==x:
            return True
    return False

def getSet(l):
    list=[]
    for x in l:
        if not (verifyInList(list,x)):
            list.append(x)
    return list

def listOfDivisors(x):
    list=[1]
    for i in range(2,int(x/2)+1):
        if x%i==0:
            list.append(i)
    return list

def sumOfDivisors(l):
    sum=0
    for i in l:
        sum+=i
    return sum

def friendCheck(a,b):
    if( sumOfDivisors(listOfDivisors(a))==b or sumOfDivisors(listOfDivisors(b))==a ):
        return True
    return False

def sequenceCheck(k):
    i=1
    aux=k
    while k>i:
        k-=i
        i+=1
    print(aux,"'th element is ",i)
