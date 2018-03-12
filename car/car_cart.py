# -*- coding: utf-8 -*-
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

#构建CART决策树模型
from sklearn.tree import DecisionTreeClassifier #导入决策树模型
treefile = 'F:\\book\\taididata\\chapter6\\tree.pkl' #模型输出名字
tree = DecisionTreeClassifier() #建立决策树模型
model=tree.fit(x_train, y_train) #训练

#保存模型
from sklearn.externals import joblib
joblib.dump(tree, treefile)


#注意到Scikit-Learn使用predict方法直接给出预测结果。
from sklearn import metrics
from matplotlib import pyplot as plt
cm_train = metrics.confusion_matrix(y_train, model.predict(x_train)) #训练样本的混淆矩阵
cm_test = metrics.confusion_matrix(y_test, model.predict(x_test)) #测试样本的混淆矩阵


plt.matshow(cm_train, cmap=plt.cm.Greens) 
plt.colorbar() 
for x in range(len(cm_train)): 
    for y in range(len(cm_train)):
      plt.annotate(cm_train[x,y], xy=(x, y), horizontalalignment='center', verticalalignment='center')
plt.ylabel('True label') 
plt.xlabel('Predicted label')
plt.show()



plt.matshow(cm_test, cmap=plt.cm.Greens) 
plt.colorbar() 
for x in range(len(cm_test)): 
    for y in range(len(cm_test)):
      plt.annotate(cm_test[x,y], xy=(x, y), horizontalalignment='center', verticalalignment='center')
plt.ylabel('True label')
plt.xlabel('Predicted label')
plt.show()
