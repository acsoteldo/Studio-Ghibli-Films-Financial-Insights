#!/usr/bin/env python
# coding: utf-8

# In[12]:


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import seaborn as sns
import matplotlib.pyplot as plt


# In[13]:


data = pd.read_csv(r"Studio_Ghibli CLEANED.csv")


# In[14]:


# Displaying the first few rows of the dataset
print(data.head())

# Checking the data types of columns
print(data.dtypes)


# In[17]:


data['Budget'] = data['Budget'].replace('[\$,]', '', regex=True).astype(float)
data['Revenue'] = data['Revenue'].replace('[\$,]', '', regex=True).astype(float)
print(data[['Budget', 'Revenue']].head())


# In[18]:


# Visualizing the relationship between Budget and Revenue
sns.scatterplot(x='Budget', y='Revenue', data=data)
plt.title('Budget vs. Revenue')
plt.xlabel('Budget')
plt.ylabel('Revenue')
plt.show()


# In[25]:


# Training a simple linear regression model to predict Revenue based on Budget
# Splitting the data into features (X) and target variable (y)
X = data[['Budget']]
y = data['Revenue']

# Splitting the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Training the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Making predictions on the testing set
y_pred = model.predict(X_test)

# Evaluating the model
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)


# In[26]:


# Visualizing the model's predictions
plt.scatter(X_test, y_test, color='black')
plt.plot(X_test, y_pred, color='blue', linewidth=3)
plt.title('Linear Regression: Budget vs. Revenue')
plt.xlabel('Budget')
plt.ylabel('Revenue')
plt.show()


# In[27]:


# Checking correlation between Budget and Revenue
correlation = data['Budget'].corr(data['Revenue'])
print("Correlation between Budget and Revenue:", correlation)


# In[ ]:




