# -*- coding: utf-8 -*- 
""" 
Created on Tue Aug 01 09:15:56 2017 

@author: DexinShao 
#m个数里选n个数的全部组合（而非排列，求排列可以先求组合然后每个组合内全排列） 
#字典序法 
#01置换法 
def combine01(m,n,b):
    从长度为m的b中选n个数
    ptable记录m中n个数的组合，0表示没选中，1表示选中，初始化前n个为1，后面的为0
    bfind记录是否进行了10置换，也就是循环到再也没有10置换为止
    每次循环根据ptable输出当前n个数的组合（即将等于1的位置的b对应位置的值存入tmp计入a
    遍历ptable的前m-1个数：
        遇到10组合就交换10位置
        把bfind置为True
        如果10组合在起始位置，continue，这个过程第n+1个位置的0，即第一个0从位置n+1移到了首位
        下一轮会找到10组合，置换10位置，并把原10位置之前的1都移动到首位，此时第二个0往前移动一位，第一个0回到第二个0前面
        直到没有10组合位置
    
""" 


def combine01(m,n,b): 
    if n>m: 
        return 
    ptable=[1]*n+[0]*(m-n)
    
    bfind=True 
    a=[] 
    while(bfind): 
        print ptable
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
                    print i
                    for k in range(1,i): 
                        if(ptable[k]==1): 
                            ptable[j]=1 
                            ptable[k]=0 
                            j+=1 
                break 
    return a     
            
                
""" 
#递归法 
def combineRecur(m,n,c):
    从长度为m的c中选n个数
    b用来记录这n个数，初始化为0
    依次固定b的最后一位为c的第m到第n位数，
    当固定b的最后一位为c的第i位数时，
    如果n大于1，则固定b的最后一位之后剩下的问题就是从c中前i-1位数中选n-1个数（i-1≥n-1，i>n,这就是b的最后一位只能为c的第n位以后的原因）
    否则n=1,b[n-1]即为b[0],b的最后一位也就是第一位，b已经被赋值完毕，
    存入totalNumber，此处必须用deepcopy，否则在b被赋值为其他组合时，之前存入totalNumber的值也会随之改变
    b的初始化需要在递归之前完成，因此必须在combineRecur外面包装一层函数用来初始化b，在递归里面对b完成赋值
"""                 
        

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
d=c+[6]
totalNumber=[] 
b=[] 
combineRmain(5,3,c) 
result01=combine01(6,3,d) 

"""   
#python内置算法 
注意这里的tmp是个元组type(tmp) : tuple
"""   
import itertools 
a=itertools.combinations(c,3) 
resultpy=[]
for tmp in a: 
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
