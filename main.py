import numpy as np
import matplotlib.pyplot as plt
import math

tab = np.genfromtxt('./maison.txt',delimiter=',')

x = tab[:,0].reshape((-1,1))
y = tab[:,1].reshape((-1,1))

x_moyenne = np.ones((np.size(x),1))
y_moyenne = np.ones((np.size(y),1))
x_moyenne[:,0] = (np.sum(x, None, dtype=np.float128) / len(x))
y_moyenne[:,0] = (np.sum(y, None, dtype=np.float128) / len(y))

ecart_moyenne_x = np.subtract(x, x_moyenne)
ecart_moyenne_y = np.subtract(y, y_moyenne)

# sum[(xi-x_moyenne)(yi-y_moyenne)]
r1 = np.sum((ecart_moyenne_x * ecart_moyenne_y))
# sqrt[sum[sqr(xi-x_moyenne)]*sum[sqr(yi-y_moyenne)]]
r2 = math.sqrt( (np.sum((ecart_moyenne_x ** 2))) * (np.sum((ecart_moyenne_y ** 2))))
# coefficient de correlation linéaire
r = r1 / r2

b1 = r1 / (np.sum((ecart_moyenne_x ** 2)))
b0 = (y_moyenne[0] - (b1 * x_moyenne[0]))[0]
b1 = round(b1,4)
b0 = round(b0,4)    

print(f" Y = F(X) = { b1 }X + { b0 }") #  Y = F(X) = 134.5253X + 71270.4924

x_abscisse = x.reshape((1,-1)).tolist()[0]
y_abscisse = y.reshape((1,-1)).tolist()[0]

# nuage de point pour le données réelles
plt.title("Répresentation Graphique")
plt.scatter(x_abscisse,y_abscisse,s=40,alpha=0.6,color='blue',label='donées réelles')

y_prix_predict = []
x_surface = []
i = 800
while i <= 5000:
    y_prix_predict.append((b1 * i) + b0)
    x_surface.append(i)
    i += 10

# régrassion linéaire
plt.plot(x_surface,y_prix_predict,color='red',label='modèl de régression')
plt.legend()
plt.grid()
plt.show()












