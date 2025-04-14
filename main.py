import numpy as np
# arr1 = np.array([1.0,2,3])
# print(arr1)
# #数组（int，float）
# arr1 = np.array([1,2,3])
# arr1[0]=100.9
# print(arr1)
# #插入会截断（）
# arr1 = np.array([1,2,3,4,5])
# print(arr1)
# arr2 = arr1.astype(float)
# print(arr2)
# #整体转型（astype）
# arr = np.array([1,2,3,4,5])
# print(arr+0.0)
# print(arr/1)
# int_arr = np.array([1,2,3])
# float_arr = np.array([1.0,2.0,3.0])
# print(int_arr+float_arr)
#整体转化
# arr1 = np.ones((1,1,3))
# print(arr1)
#记得二维三维加括号，
# arr1 = np.ones((1,1,3))
# print(arr1.shape )
#shape方法，看形状的
# arr1 = np.arange(10)
# print(arr1)
# print(arr1.reshape(2,5))
# print(arr1.reshape(-1))
#reshape变换几何
# arr1 = np.array([1,2,3,4,5])
# print(arr1)
# arr2 = np.array([[1],[2],[3]])
# print(arr2)
# 创造矩阵加【【】】
# arr1 = np.arange(10,100,10)
# print(arr1)
# 递增数组arange
# arr1 = np.zeros(5)
# arr2 = np.ones((5,6))
# arr3 = 3.14*np.ones((5,6))
# print(arr1,end="")
# print(arr2,end="")
# print(arr3)
# 同智数组
# arr1 = 40*np.random.random((2,5))+60#（0-1）的float数组
# print(arr1)
# arr2 = np.random.randint(0,10,(2,5))#random。randint（0，100，（2，5））整数
# arr3 = np.random.normal(0,1,(2,3))#正态分布的随机数组
#访问
# arr1 = np.arange(10)
# print(arr1[3])
# arr1[5] = 100
# print(arr1[5])
# arr1 = np.arange(0,90,10).reshape(3,3)
# print(arr1[[0,2],[2,0]])#狠花的索引
# arr1 = np.arange(10)
# print(arr1[1:4])
# print(arr1[:4])
#切片
#矩阵切片
# arr1 = np.arange(1,21).reshape(4,5)
# print(arr1[1:3,1:-1])
# print(arr1[::3,::2])
# print(arr1[2,:])
# print(arr1[1:3,:])
# print(arr1[2,:])
# print(arr1[2])
# arr1 = np.arange(10).reshape(2,5)
# print(arr1.T)
# arr2 = arr1.reshape(1,-1)
#升级矩阵
#拷贝copy
#绑定也变
#.T只对矩阵有效
# arr1 = np.arange(1,4)
# arr2 = arr1.reshape(1,-1)
# print(arr2.T)
# print(arr2)
#向量的反转
# arr1 = np.arange(10)
# arr_ud = np.flipud(arr1)
# print(arr_ud)#向量是上下的关系
# arr1 = np.arange(1,21).reshape(4,5)
# arr_lr = np.fliplr(arr1)
# arr_ud = np.flipud(arr1)
# print(arr1)
# print(arr_ud)
# print(arr_ud)
# #flipud是上下反转，fliplr是左右，flipud，fliplr
#向量的拼接concatenate
# arr1 = np.array([1, 2, 3])
# arr2 = np.array([4, 5, 6])
# arr3 = np.concatenate([arr1,arr2])
# print(arr3)
#数组的分裂
# arr = np.arange(10,100,10)
# arr1,arr2,arr3 = np.split(arr,[2,8])
# print(arr1)
# print(arr2)
# print(arr3)
#矩阵分为行列来分割
# arr = np.arange(1,9).reshape(2,4)
# arr1,arr2 = np.split(arr,[1])
# print(arr1)
# print(arr2)
# arr1,arr2,arr3 = np.split(arr,[1,3],axis = 1)
# print(arr1)
# print(arr2)
# print(arr3)
# arr1 = np.arange(10)
# print(arr1**100)#数组的运算
#向量广播
# arr1 = np.arange(4)
# arr2 = np.arange(16).reshape((4,4))
# print(arr1*arr2)#向下广播，还有一种横向广播
#向量的乘积
#np.dot(arr1,arr2)
#绝对值函数np。abs
#np.max(arr,axis =0)聚合
#布尔型数组print(arr1>arr2)
#and or not
#print(arr[arr>4])
#满足元素所在位置
# arr = np.random.normal(500,60,1000)
# print(np.where(arr>500))
# print(np.where(arr == np.max(arr)))
#张量









