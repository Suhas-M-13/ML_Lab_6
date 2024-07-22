import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score, classification_report

# Load the data with the correct delimiter
df = pd.read_csv("weather_forecast.csv", delimiter = "\t")

# One-hot encode categorical variables
df = pd.get_dummies(df, drop_first=True)

print(df.columns)

# Correctly identify the target column after get_dummies
target_column = 'Play_Yes'

# Separate features and target variable
x = df.drop(target_column, axis=1)
y = df[target_column]

# Split the data into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Initialize and train the Decision Tree classifier
clf_id3 = DecisionTreeClassifier(criterion='entropy', random_state=42)
clf_id3.fit(x_train, y_train)

# Plot the decision tree
plt.figure(figsize=(12, 8))
plot_tree(clf_id3, filled=True, feature_names=x.columns, class_names=["No", "Yes"])

plt.show()