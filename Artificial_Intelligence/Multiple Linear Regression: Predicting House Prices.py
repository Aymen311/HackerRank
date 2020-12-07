# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np 

def read_data():
  train_data = list()
  test_data = list()
  F,N = map(int, input().split(' '))
  [train_data.append(input().split(' ')) for _ in range(0,N)]
  T = int(input())
  [test_data.append(input().split(" ")) for _ in range(0, T)]
  train_data = np.array(train_data, dtype = np.float64)
  test_data = np.array(test_data, dtype = np.float64)
  X_train = train_data[:, 0:F]
  y_train = train_data[:,-1]
  X_test = test_data
  return X_train, y_train,X_test

X_train, y_train, x_test = read_data()
from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(X_train,y_train)
prediction_lin = lin_reg.predict(x_test)
print('\n'.join(list(map(str,prediction_lin))))



