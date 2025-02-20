import numpy as np


dataset = np.genfromtxt('maison.txt', delimiter=",")

# surface
x1 = dataset[:,0].reshape(-1,1)
# nombre chambre
x2 = dataset[:,1].reshape(-1,1)
# prix
y = dataset[:,2].reshape(-1,1)
y_moyenne = round((np.sum(y) / len(y)),3)
x1_moyenne = round((np.sum(x1) / len(x1)),3)
x2_moyenne = round((np.sum(x2) / len(x2)),3)

datasetTemp = dataset
dataset = np.ones((np.size(x1),4))
dataset[:,1] = datasetTemp[:,0]
dataset[:,2] = datasetTemp[:,1]
dataset[:,3] = datasetTemp[:,2]

# X | Y
X = dataset[:,0:3].reshape(-1,3)
Y = dataset[:,3].reshape(-1,1)

# les coefficient B (b0,b1,b2) | ŷi
B = np.linalg.inv(X.T @ X) @ X.T @ Y
b0 = round(B[0][0],3)
b1 = round(B[1][0],3)
b2 = round(B[2][0],3)
y_predict_x1_x2 = []

i = 0
while i < len(x1):
    y_predict_x1_x2.append(b0 + (b1 * x1[i]) + (b2 * x2[i]))
    i += 1
y_predict_x1_x2 = np.array(y_predict_x1_x2).reshape(-1,1)

# Residues | SCR | SCE | SCT | R²
residues = np.subtract(y,y_predict_x1_x2)
SCR = np.sum(residues ** 2)
SCE = np.sum(np.subtract(y_predict_x1_x2,y_moyenne) ** 2)
SCT = SCR + SCE
S = SCR / (len(Y) - 3)
R = 1 - (SCR / SCT)

# function de régression
def regression(x1,x2):
    predict = b0 + (b1 * x1) + (b2 * x2)
    return predict



print(f"y = { b0 } + { b1 }x1 + { b2 }x2")
print(f"SCR: { SCR }")
print(f"SCE: { SCE }")
print(f"SCT: { SCT }")
print(f"R²: { R }")
















