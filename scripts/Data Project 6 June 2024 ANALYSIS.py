#!/usr/bin/env python
# coding: utf-8

# In[27]:


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import OneHotEncoder

data = pd.read_csv(r"long_format_annual_surface_temp CLEANED.csv")


# In[28]:


print(data.head())
print(data.dtypes)


# In[29]:


# One-hot encode the categorical columns
onehotencoder = OneHotEncoder(drop='first', sparse_output=False)
categorical_cols = ['Country', 'CountryID']
onehot_encoded = onehotencoder.fit_transform(data[categorical_cols])
onehot_encoded_df = pd.DataFrame(onehot_encoded, columns=onehotencoder.get_feature_names_out(categorical_cols))

# Concatenate one-hot encoded columns with the original dataset (excluding the original categorical columns)
data_processed = pd.concat([onehot_encoded_df, data[['Year', 'Temperature']]], axis=1)


# In[30]:


# Define features (X) and target variable (y)
X = data_processed.drop('Temperature', axis=1)
y = data_processed['Temperature']


# In[31]:


# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=200)

# Initialize and train the linear regression model
reg = LinearRegression().fit(X_train, y_train)

# Make predictions on the testing set
y_pred = reg.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)

# Additional analysis (e.g., correlation)
correlation_matrix = data.corr()
print("Correlation Matrix:")
print(correlation_matrix)


# In[ ]:




