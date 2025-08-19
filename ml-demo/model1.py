###
Machine Learning
- Loading data,
- Preprocessing,
- Training a model,
- Evaluating the model,
- Making Predictions.
###

# import necessary libraries
import pandas as pd
from sklearn.linear_model import LogisticRegression

# loading the dataset and displaying the first few rows
iris_data = pd.read_csv('iris.csv')
# inspect dataset and get a quick overview of the content
iris_data.head() 

# Output: []

x = iris_data.drop(columns=['Id', 'Species']) 
y = iris_data['Species']

x.head()

# Output: []

# Create a machine learning model, to initialise the model with default settings
model = LogisticRegression()

# train the model
model.fit(x.values, y)
# x is for training the model with the data and it's labels, while y is for understanding the relationships

#predict using the trained model 
predictions = model.predict([[4.6, 3.5, 1.5, 0.2]])

print(predictions)

# Output: ['Iris-Setosa']
