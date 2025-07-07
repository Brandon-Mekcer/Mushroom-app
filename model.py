from sklearn.model_selection import train_test_split 
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score, classification_report 
import matplotlib.pyplot as plt
import pandas as pd

# Loading the data
df = pd.read_csv('mushrooms.csv')
# Cleaning the data
for col in df.columns:
    df[col] = df[col].astype("category")
    df[col] = df[col].cat.codes
# df.head()
# Modelling
X = df.drop("class", axis=1)
y = df["class"]
# Split the data for training and testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
# Creating and training the model
decision_model = DecisionTreeClassifier()
decision_model.fit(X_train, y_train)
y_pred = decision_model.predict(X_test)
print("Accuracy: ",accuracy_score(y_test, y_pred))
print("Classification Report:", classification_report(y_test, y_pred))


plt.figure(figsize=(40,20))
plot_tree(decision_model, max_depth=None, filled=True, feature_names=X.columns, class_names= ["edible", "poisonous"], rounded=True)
plt.savefig("Mushroom_decision_tree.png", dpi = 300, bbox_inches = "tight")
plt.close

