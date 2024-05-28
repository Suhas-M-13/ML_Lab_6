import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier as KNN

glass_data=pd.read_csv("glass.csv")

k_values=[3]
distance_metrics= ['manhattan','euclidean']
test_splits = [0.3]

for k in k_values:
    for p,distance_metric in enumerate(distance_metrics):
        for ts in test_splits:
            print(f"K={k},Distance Metric={distance_metric}: ")
            print(f"Split = {ts}")
            knn=KNN(n_neighbors=k,p=p+1,weights="distance")
            X_train,X_test, y_train,y_test=train_test_split(glass_data.drop(columns=['Type']),glass_data['Type'],test_size=ts,random_state=42)
            knn.fit(X_train,y_train)
            accuracy=knn.score(X_test,y_test)
            print(f"accuracy on test set: {accuracy:.2f}")
            print("----------------------------")