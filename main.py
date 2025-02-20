import numpy as np

dataset = np.genfromtxt('maison.txt', delimiter=",")

# surface
x1 = dataset[:,0]
# nombre chambre
x2 = dataset[:,1]
# prix
y = dataset[:,2]

datasetTemp = dataset
dataset = np.ones((np.size(x1),4))
dataset[:,1] = datasetTemp[:,0]
dataset[:,2] = datasetTemp[:,1]
dataset[:,3] = datasetTemp[:,2]

# X | Y
X = dataset[:,0:3]
Y = dataset[:,3]

# B = (X^T*X)^(-1)*X^T*Y
# B =  np.dot(np.linalg.inv(np.dot(X,X.T)), np.dot(X.T,Y))

B = np.linalg.inv(X.T @ X) @ X.T @ Y
print(f"y = {B[0]} + { B[1] }x1 + { B[2] }x2")
def regression(x1,x2):
    predict = B[0] + (B[1] * x1) + (B[2] * x2)
    return predict















