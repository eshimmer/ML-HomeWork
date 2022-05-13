import numpy as np
#均方误差
def mse(real,predict):
    real=np.array(real)
    predict=np.array(predict)
    a = np.power((real-predict),2)
    return a.mean()


#均方根误差
def rmse(real,predict):
    a = mse(real,predict)
    return np.power(a,1/2)


#平均绝对误差
def mae(real,predict):
    real = np.array(real)
    predict = np.array(predict)
    a = np.abs(real-predict)
    return a.mean()


#R方
def r_sqr(real,predict):
    real = np.array(real)
    predict = np.array(predict)
    a = np.power((real-predict),2)
    print(a,a.sum())
    b = np.power((real-np.mean(real)),2)
    print(b,b.sum())
    return 1-a.sum()/b.sum()