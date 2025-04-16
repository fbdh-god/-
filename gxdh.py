# -*- conding:utf-8 -*-
"""
作者；yhs
时期：2025年04月16日
内容：学习pandas
"""
#
import pandas as pd
import numpy as np
# v = [0,1,2,3]
# k = ["a","b","c","d"]
# sr = pd.Series(v,index = k)
# # print(sr)values可以为数组,且为数组，张量列表index可以省略
# v = [0,1,2,3]
# s = [6,7,8,9]
# k = ["a","b","c","d"]
# sr = pd.Series(v,index = k)
# st = pd.Series(s,index = k)
# n = pd.DataFrame({"ds":sr,"rs":st})
# print(sr)
# print(st)
# print(n)直接法
# v = np.array([[53,"nv"],[64,"nan"],[72,"nan"],[82,"nv"]])
# i = ["1hao","2hao","3hao","4hao"]
# c = ["nianling","xinbei"]
# df = pd.DataFrame(v,index = i, columns = c)
# print(v)
# print(df)数组法
# v = [0,1,2,3]
# k = ["a","b","c","d"]
# sr = pd.Series(v,index = k)
# print(sr.loc["b"]) #索引
# g = sr[["a","b"]]
# print(g)#花式索引
#切片
# cut = sr["a":"c"]
# cut["a"] = 1000
# print(sr,end="")
# print(cut)#和数组一样会改变原来的值
#新变量，需要。copy
v = np.array([[53,"nv"],[64,"nan"],[72,"nan"],[82,"nv"]])
i = ["1hao","2hao","3hao","4hao"]
c = ["nianling","xinbei"]
k = [1,2,3,4,]
df = pd.DataFrame(v,index = i, columns = c)
# s = df.loc[["1hao","2hao"],["nianling","xinbei"]]
# print(s)
# print(df.loc["1hao","nianling"])#二维索引需要loc和iloc对应着显和隐
# df.loc["2hao","nianling"] = 1000
# print(df)#改值
# sd = df.T
# print(df)
# print(sd)#转置
# print(df)
# a = df.iloc[:,::-1]#左右反转
# b = df.iloc[::-1,:]#上下反转
# print(a)
# print(b)
# df["niubi"] = k#加一行
# print(df["niubi"])#二维变一维
# print(df)
# pd.concat([arr,arr1])#一维合并二维
# pd.concat([arr,arr1]，axis = 1),1 为列 2为行
# df["niubi"] =df["niubi"] + 100 or *100  or /100    运算  df["无敌"] =df["niubi"] + df["niubi"]     这里是加新列
#布尔型
# sr.isnull()#查看缺失值
#  sr.fillna()#填充缺失值
#插入excel另外学