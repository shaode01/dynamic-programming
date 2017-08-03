# -*- coding: utf-8 -*- 
""" 
Created on Wed Aug 02 10:13:25 2017 

@author: DexinShao 
题目大意：给出一串数字。两个玩家A B分别取从两端取数。 
          A可以任意取，B采取贪心方法取大的一端，如果相等则取左边的数； 
          取完数后，每个人的数求和。求出A赢B的最多点数。 
          
说明：
dp[i][j]用来记录A从“第i个数到第j个数”（下标从0开始）中取数得到的最大值，初始化为0
def fun(left,right):
    如果A取left端，则B比较left+1和right处a的大小
    if a[left+1]>=a[right] B取left+1，A的最大值=a[left]+fun(left+2,right)
    否则B取right，A的最大值=a[left]+fun(left+1,right-1)
    为了避免重复计算，当 dp[left][right]!=0时，即dp[left][right]已经被计算过了，
    （也有可能计算出的最大值就是0，因此初始化为字符比较妥当）即可直接返回结果。
    判断left==right的情况，可以兼容a个数为奇数的情况。
""" 
dp=[['o']*10 for i in range(10)] 
a=[2,5,3,4] 
def fun(left,right): 
    if left>right: 
        return 0 
    if left==right: 
        return a[left] 
    if dp[left][right]!='o': 
        return dp[left][right] 
    leftsum=a[left]+(fun(left+2,right) if a[left+1]>=a[right] else fun(left+1,right-1)) 
    rightsum=a[right]+(fun(left+1,right-1) if a[left]>=a[right-1] else fun(left,right-2)) 
    dp[left][right]=max(leftsum,rightsum) 
    return dp[left][right] 
firstsum=fun(0,len(a)-1) 
suma=sum(a) 
print firstsum-(suma-firstsum) 
