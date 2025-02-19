import numpy as np
import matplotlib.pyplot as plt
import math

tab = np.genfromtxt('./maison.txt',delimiter=',')

# donnés réelles
x = tab[:,0].reshape((-1,1))
y = tab[:,1].reshape((-1,1))

x_moyenne = np.ones((np.size(x),1))
y_moyenne = np.ones((np.size(y),1))
x_moyenne[:,0] = (np.sum(x, None, dtype=np.float128) / len(x))
y_moyenne[:,0] = (np.sum(y, None, dtype=np.float128) / len(y))

ecart_moyenne_x = np.subtract(x, x_moyenne)
ecart_moyenne_y = np.subtract(y, y_moyenne)

# coéfficient de corrélation
# sum[(xi-x_moyenne)(yi-y_moyenne)]
r1 = np.sum((ecart_moyenne_x * ecart_moyenne_y))
# sqrt[sum[sqr(xi-x_moyenne)]*sum[sqr(yi-y_moyenne)]]
r2 = math.sqrt( (np.sum((ecart_moyenne_x ** 2))) * (np.sum((ecart_moyenne_y ** 2))))
# coefficient de correlation linéaire
r = r1 / r2
print(f"r = { r }")

b1 = r1 / (np.sum((ecart_moyenne_x ** 2)))
b0 = (y_moyenne[0] - (b1 * x_moyenne[0]))[0]
b1 = round(b1,4)
b0 = round(b0,4)    

print(f"Y = F(X) = { b1 }X + { b0 }") #  Y = F(X) = 134.5253X + 71270.4924

x_abscisse = x.reshape((1,-1)).tolist()[0]
y_abscisse = y.reshape((1,-1)).tolist()[0]

# nuage de point pour les données réelles
plt.title("Répresentation Graphique")
plt.scatter(x_abscisse,y_abscisse,s=40,alpha=0.6,color='blue',label='donnés réelles')

y_prix_predict_by_x = []
x_surface = []
i = 800
while i <= 5000:
    y_prix_predict_by_x.append((b1 * i) + b0)
    x_surface.append(i)
    i += 10

# répresentation graphique de la régression linéaire
plt.plot(x_surface,y_prix_predict_by_x,color='red',label='modèl de régression')
plt.legend()
plt.grid()

# ei | SCR | SCE | SCT
residue_of_observation = np.ones((np.size(x),1))
y_predict = []
i = 0
while i < len(x):
    y_predict.append((b1 * x[i][0]) + b0)
    residue_of_observation[i][0] = y[i][0] - ((b1 * x[i][0]) + b0)
    i += 1
y_predict = np.array(y_predict).reshape((-1,1))
SCR = np.sum(residue_of_observation ** 2)
SCE = np.sum(np.subtract(y_predict,y_moyenne) ** 2)
SCT = SCR + SCE
R = SCE / SCT

print(f"SCR = { SCR }")
print(f"SCE = { SCE }")
print(f"SCT = { SCT }")
print(f"S²  = { SCR / (len(residue_of_observation) - 2) }")
print(f"R²  = { R }")
plt.show()















