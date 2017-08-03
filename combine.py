# -*- coding: utf-8 -*- 
""" 
Created on Tue Aug 01 09:15:56 2017 

@author: DexinShao 
""" 

#m个数里选n个数的全部组合（而非排列，求排列可以先求组合然后每个组合内全排列） 
#字典序法 
#01置换法 
def combine01(m,n,b): 
    if n>m: 
        return 
    ptable=[1]*n+[0]*(m-n) 
    bfind=True 
    a=[] 
    while(bfind): 
        tmp=[] 
        for i in range(m): 
            if(ptable[i]==1): 
                tmp.append(b[i]) 
        a.append(tmp) 
        bfind=False 
        for i in range(m-1): 
            if(ptable[i]==1 and ptable[i+1]==0): 
                ptable[i]=0 
                ptable[i+1]=1 
                bfind=True 
                if(ptable[0]==0): 
                    j=0 
                    for k in range(1,i): 
                        if(ptable[k]==1): 
                            ptable[j]=1 
                            ptable[k]=0 
                            j+=1 
                break 
    return a     
            
                
                
        
#递归法 
import copy 
def combineRecur(m,n,c): 
    global totalNumber 
    for i in range(m,n-1,-1): 
        b[n-1]=c[i-1] 
        #print b,n-1,len(totalNumber) 
        if(n-1>0): 
            combineRecur(i-1,n-1,c) 
        else: 
            totalNumber.append(copy.deepcopy(b)) 
            #print totalNumber 

def combineRmain(m,n,c): 
    global b 
    b=[0]*n 
    combineRecur(m,n,c) 
    

c=[1,2,3,4,5] 
totalNumber=[] 
b=[] 
combineRmain(5,3,c) 
result01=combine01(5,3,c) 


#python内置算法 
import itertools 
a=itertools.combinations(c,3) 
resultpy=[]
for tmp in a: #type(tmp) : tuple
    resultpy.append(tmp)
    

#python内置算法 
def combinepy(b,n): 
    pool=tuple(b) 
    m=len(pool) 
    if n>m: 
        return 
    indices=list(range(n)) 
    yield tuple(pool[i] for i in indices) 
    while True: 
        for i in reversed(range(n)): 
            if indices[i]!=i+m-n: 
                break 
            else: 
                return 
