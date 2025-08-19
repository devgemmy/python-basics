# import necessary libraries
import pandas as pd
from sklearn.linear_model import LogisticRegression
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
# to prevent overfitting
from sklearn.metrics import accuracy_score

# loading the dataset and displaying the first few rows
iris_data = pd.read_csv('iris.csv')
# inspect dataset and get a quick overview of the content
iris_data.head()

x = iris_data.drop(columns=['Id', 'Species'])
y = iris_data['Species']

# x.head()
# split the data into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# standardise the features
scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.transform(x_test)

# Create a machine learning model, to initialise the model with default settings
model = LogisticRegression()

# train the model
model.fit(x_train_scaled, y_train)

# evaluate the model on the testing set
y_pred = model.predict(x_test_scaled)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy: ", accuracy)

# Sample new data for prediction
new_data = np.array ([[5.1, 3.5, 1.4, 0.21],
                     [6.3, 2.9, 5.6, 1.8],
                     [4.9, 3.0, 1.4, 0.2]])

# Standardise the new data
new_data_scaled = scaler.transform(new_data)

# Make predictions
predictions = model.predict(new_data_scaled)

# Display the predicted classes
print("Predictions: ", predictions)