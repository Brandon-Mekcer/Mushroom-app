from sklearn.model_selection import train_test_split 
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report 
import seaborn as sns
import numpy as np
import pandas as pd

# Loading the data
df = pd.read_csv('mushrooms.csv')
# Cleaning the data

for col in df.columns:
    df[col] = df[col].astype("category")
    df[col] = df[col].cat.codes

# Modelling
X = df.drop("class", axis=1)
y = df["class"]
# Feature selection
correlation = X.corrwith(y).abs()
selected_cols = correlation[correlation > 0.3].index
print_cols = selected_cols.to_list()
print(print_cols)
X = X[selected_cols]

# Split the data for training and testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
# Creating and training the model
decision_model = DecisionTreeClassifier()
decision_model.fit(X_train, y_train)
y_pred = decision_model.predict(X_test)
print("Accuracy: ",accuracy_score(y_test, y_pred))
print("Classification Report:", classification_report(y_test, y_pred))
print(y.value_counts())
