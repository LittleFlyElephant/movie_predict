# encoding: utf-8
from sklearn.ensemble import RandomForestRegressor
from MysqlHelper import getData
from matplotlib import pyplot

def printPrecise(threshold, pre_res, res):
    ct=0
    for j in range(0, len(pre_res)):
        if (abs(pre_res[j]-res[j])<threshold):
            ct=ct+1
    precise=float(ct)/float(len(pre_res))
    print precise

data_set=getData()
# split train data and test data
test=data_set[0:4000]
target=data_set[4001:5000]
X=[]
y=[]
for data in test:
    tmp=data[1:]
    X.append(tmp)
    y.append(data[0])
# train
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
# test
pre_res=clf.predict(tar)
# print the ratio of preciseness
printPrecise(1, pre_res, res)
printPrecise(2, pre_res, res)
# draw a plot
pyplot.figure()
pyplot.plot(i,res,color="blue")
pyplot.plot(i,pre_res,color="red")
pyplot.show()