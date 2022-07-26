#Import Libraries

import pandas as pd
from sklearn.linear_model import LinearRegression 
import matplotlib.pyplot as plt

#Load Dataset

dataset = pd.read_csv('dataset.csv')
dataset

print(dataset.shape)
print(dataset.head(5))

#Visualize Dataset

plt.xlabel('Area')
plt.ylabel('Price')
plt.scatter(dataset.area,dataset.price,color='red',marker='*')

#Segregate Dataset into Input X & Output Y

X = dataset.drop('price',axis='columns')
X

Y = dataset.price
Y

#Training Dataset using Linear Regression

clf = LinearRegression()
clf.fit(X,Y)

#Predicted Price for Land sq.Feet of custom values

x=int(input('Enter area :'))
LandAreainSqFt=[[x]]
PredictedmodelResult = clf.predict(LandAreainSqFt)
print(PredictedmodelResult)

#Let's check is our model is Right
#Y = m * X + b (m is coefficient and b is intercept)

a=clf.coef_
print('coefficient:',a)

b=clf.intercept_
print('intercept:',b)

y = m*x + b
print("The Price of {0} Square feet Land is: {1}".format(x,y[0]))
