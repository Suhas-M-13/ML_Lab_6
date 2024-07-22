import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import GaussianNB as Classifier

def evaluate_naive_bayes(dataset, target_col, K_values):
    for K in K_values:
        x_train, x_test, y_train, y_test = train_test_split(dataset.drop(columns=[target_col]),
                                           dataset[target_col], test_size=(1 - K / 10), random_state=42)
        clf = Classifier()  
        clf.fit(x_train.values, y_train.values)
        y_pred = clf.predict(x_test.values)
        accuracy = accuracy_score(y_test, y_pred)
        print(f"Split {K * 10} - {100 - K * 10}  -->  Accuracy:{accuracy:.2f}")

titanic_data = pd.read_csv('titanic.csv')

titanic_data = titanic_data.drop(columns=['PassengerId', 'Name', 'Ticket', 'Cabin'])

titanic_data['Age'].fillna(titanic_data['Age'].median(), inplace=True)
titanic_data['Embarked'].fillna(titanic_data['Embarked'].mode(), inplace=True)

titanic_data = pd.get_dummies(titanic_data, columns=['Sex', 'Embarked'])


print("\nTitanic dataset Naive Bayes Classifier Results: ")
evaluate_naive_bayes(titanic_data, 'Survived', [3, 5, 7, 9])