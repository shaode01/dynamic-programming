# -*- coding: utf-8 -*- 
""" 
Created on Thu Jun 29 16:27:28 2017 

@author: ZJ-ShaoDexin
01背包问题
有N件物品和一个容量为V的背包。第i件物品的重量是weight[i]，价值是value[i]。求解将哪些物品装入背包可使价值总和最大。 

dp[i][j]表示容量为j的背包来装前i件物品的最大价值，初始化为0
遍历所有的物品：
    遍历所有的容量：
        如果当前容量j比第i件商品大，
            如果不放第i件商品，则最大值为在容量j内放前i-1件物品的最大价值
            如果放了第i件商品，则最大值为(在剩余容量j-weight[i]内放前i-1件物品的最大价值)+第i件商品的价值
            综上，在容量j内放前i件商品的最大价值为上述两个值中的最大值
        否则，只能在容量j内放前i-1件商品，dp[i][j]=dp[i-1][j]
        
输出结果：
19
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 8, 8, 8, 8]
[0, 0, 0, 0, 0, 10, 10, 10, 10, 10, 10]
[0, 0, 0, 4, 4, 10, 10, 14, 14, 14, 14]
[0, 0, 0, 4, 4, 10, 10, 14, 14, 15, 15]
[0, 0, 0, 4, 5, 10, 10, 14, 15, 15, 19]        
                               
""" 

value=[8,10,4,5,5] 
weight=[6,4,2,4,3] 
n=len(value) 
v=10 
dp=[[0]*(v+1) for i in range(n+1)] 
value=[0]+value 
weight=[0]+weight 
for i in range(1,n+1): 
    for j in range(1,v+1): 
        if j>weight[i]: 
            dp[i][j]=max(dp[i-1][j],dp[i-1][j-weight[i]]+value[i]) 
        else: 
            dp[i][j]=dp[i-1][j] 
            
print dp[n][v]     
for tmp in dp:
    print tmp
