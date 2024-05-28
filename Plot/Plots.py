import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D

# Load the data
data = pd.read_csv("iris.csv")

# Define the variables
x = data['SepalLengthCm']
y = data['SepalWidthCm']
z = data['PetalLengthCm']

# Scatter plot
plt.figure()
plt.scatter(x, y)
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Sepal Width (cm)')
plt.title('Scatter Plot')
plt.show()

# Box plot
plt.figure()
sns.boxplot(data=data)
plt.title("Box Plot")
plt.show()

# Heat map
plt.figure()
select = data.iloc[:, [1, 2]]
sns.heatmap(select.corr(), annot=True)
plt.title("Heat Map")
plt.show()

# Contour plot
plt.figure()
plt.tricontour(x, y, z, levels=20, cmap="jet")
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Sepal Width (cm)')
plt.title("Contour Plot")
plt.colorbar()
plt.show()

# 3D surface plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_trisurf(x, y, z, cmap="jet")
ax.set_xlabel('Sepal Length (cm)')
ax.set_ylabel('Sepal Width (cm)')
ax.set_zlabel('Petal Length (cm)')
ax.set_title('3D Surface Plot')
plt.show()
