# encoding: utf-8
from sklearn.ensemble import RandomForestRegressor
from MysqlHelper import getData
from matplotlib import pyplot

data_set=getData()
test=data_set[0:4000]
target=data_set[4001:4100]
X=[]
y=[]
for data in test:
    tmp=data[1:]
    X.append(tmp)
    y.append(data[0])

clf = RandomForestRegressor(n_estimators=10)
clf.fit(X, y)
tar=[]
res=[]
i=[]
cnt=1
for data in target:
    tar.append(data[1:])
    res.append(data[0])
    i.append(cnt)
    cnt=cnt+1
pre_res=clf.predict(tar)
pyplot.figure()
pyplot.plot(i,pre_res,color="red")
pyplot.plot(i,res,color="blue")
pyplot.show()