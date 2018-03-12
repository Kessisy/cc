# -*- coding: utf-8 -*-
"""
@author: Anne
"""
import pandas as pd
from scipy.interpolate import lagrange 
from numpy.random import shuffle
inputfile = 'F:\\book\\taididata\\chapter6\\拓展思考\\拓展思考样本数据.xls'
outputfile='F:\\book\\taididata\\chapter6\\拓展思考\\拓展思考样本处理后数据.xls'
data=pd.read_excel(inputfile,header=None)
for i in range(data.shape[0]):
    if data[15][i]==u'异常':
        data[15][i]=0
    elif data[15][i]==u'正常':
        data[15][i]=1
def ployinterp_column(s, n, k=5):
  y = s[list(range(n-k, n)) + list(range(n+1, n+1+k))] #取数
  y = y[y.notnull()] #剔除空值
  return lagrange(y.index, list(y))(n) #插值并返回插值结果

#逐个元素判断是否需要插值
for i in range(data.shape[1]):
  for j in range(data.shape[0]):
    if (data[i].isnull())[j]: #如果为空即插值。
      data[i][j] = ployinterp_column(data[i], j)
data=data.iloc[1:,3:16]
data.to_excel(outputfile, header=None, index=False)

data = data.as_matrix()
shuffle(data)
data_train = data[:int(0.8*len(data)), :] #选取前80%为训练数据
data_test = data[int(0.8*len(data)):, :] #选取前20%为测试数据
x_train = data_train[:, :12]
y_train = data_train[:, 12].astype(int)
x_test = data_test[:, :12]
y_test = data_test[:, 12].astype(int)

from keras.models import Sequential #导入神经网络初始化函数
from keras.layers.core import Dense, Activation #导入神经网络层函数、激活函数

netfile = 'F:\\book\\taididata\\chapter6\\net.model' #构建的神经网络模型存储路径

net = Sequential() #建立神经网络
net.add(Dense(input_dim = 12, output_dim = 16)) #添加输入层（3节点）到隐藏层（10节点）的连接
net.add(Activation('relu')) #隐藏层使用relu激活函数
net.add(Dense(input_dim = 16, output_dim = 1)) #添加隐藏层（10节点）到输出层（1节点）的连接
net.add(Activation('sigmoid')) #输出层使用sigmoid激活函数
net.compile(loss = 'binary_crossentropy', optimizer = 'adam') #编译模型，使用adam方法求解

net.fit(x_train, y_train, epochs=100, batch_size=1) #训练模型，循环1000次
net.save_weights(netfile) #保存模型
predict_result1 = net.predict_classes(x_train).reshape(len(x_train)) #预测结果变形
predict_result2 = net.predict_classes(x_test).reshape(len(x_test)) #预测结果变形


from sklearn import metrics
from matplotlib import pyplot as plt
cm_train = metrics.confusion_matrix(y_train, predict_result1) #训练样本的混淆矩阵
cm_test = metrics.confusion_matrix(y_test, predict_result2 ) #测试样本的混淆矩阵
plt.matshow(cm_train,cmap=plt.cm.Purples) #»­»ìÏý¾ØÕóÍ¼£¬ÅäÉ«·ç¸ñÊ¹ÓÃcm.Greens£¬¸ü¶à·ç¸ñÇë²Î¿¼¹ÙÍø¡£
plt.colorbar() 
for x in range(len(cm_train)): #Êý¾Ý±êÇ©
    for y in range(len(cm_train)):
      plt.annotate(cm_train[x,y], xy=(x, y), horizontalalignment='center', verticalalignment='center')
plt.ylabel('True label') #×ø±êÖá±êÇ©
plt.xlabel('Predicted label')
plt.show()
plt.matshow(cm_test, cmap=plt.cm.Greens) #»­»ìÏý¾ØÕóÍ¼£¬ÅäÉ«·ç¸ñÊ¹ÓÃcm.Greens£¬¸ü¶à·ç¸ñÇë²Î¿¼¹ÙÍø¡£
plt.colorbar() 
for x in range(len(cm_test)): #Êý¾Ý±êÇ©
    for y in range(len(cm_test)):
      plt.annotate(cm_test[x,y], xy=(x, y), horizontalalignment='center', verticalalignment='center')
plt.ylabel('True label') #×ø±êÖá±êÇ©
plt.xlabel('Predicted label')
plt.show()



