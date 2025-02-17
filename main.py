import numpy as np
import math

tab = np.genfromtxt('./maison.txt',delimiter=',')

x = tab[:,0].reshape((-1,1))
y = tab[:,1].reshape((-1,1))

x_moyenne = np.ones((np.size(x),1))
y_moyenne = np.ones((np.size(y),1))
x_moyenne[:,0] = (np.sum(x, None, dtype=np.float128) / len(x))
y_moyenne[:,0] = (np.sum(y, None, dtype=np.float128) / len(y))

ecart_moyenne_x = np.ones((np.size(x), 1))
ecart_moyenne_y = np.ones((np.size(y), 1))
ecart_moyenne_x = np.subtract(x, x_moyenne)
ecart_moyenne_y = np.subtract(y, y_moyenne)

# sum[(xi-x_moyenne)(yi-y_moyenne)]
r1 = np.sum((ecart_moyenne_x * ecart_moyenne_y))
# sqrt[sum[sqr(xi-x_moyenne)]*sum[sqr(yi-y_moyenne)]]
r2 = math.sqrt( (np.sum((ecart_moyenne_x ** 2))) * (np.sum((ecart_moyenne_y ** 2))))
# coefficient de correlation linéaire
r = r1 / r2
