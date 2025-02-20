# Régression Linéaire Multiple Exemple

On cherche à modéliser la relation entre poids des bébés à naissance et l’âge, le
poids et le statut tabagique de la mère durant la grossesse. On pose :
- y = poids de naissance en grammes (bwt),
- x1 = âge de la mère (age),
- x2 = poids de la mère en kilos (weight),
- x3 = statut tabagique de la mère pendant la grossesse (smoke) codée
1=oui et 0=non.
On suppose que cette relation est linéaire de la forme :
    
$$y = β_0 + β_1x_1 + β_2x_2 + β_3x_3$$

On veut **estimer** cette relation avec un modèle de **régression multiple**.
On utilise un échantillon de **n = 1174** (bwt age weight smoke) naissances pour lesquelles le poids
du bébé, l’âge, le poids et le statut tabagique de la mère, ont été mesurés.

## 1. Le modèl 

On cherche à modéliser la relation entre plus de 2 variables quantitatives.
Un modèle de régression linéaire multiple est de la forme suivante :


$$y = β0 + \sum_{j=1}^p β_j x_j + \mathcal{E} $$

où:

  - $y$ est la <a style="color :#4caf50">variable à expliquer</a>  (à valeurs dans $\mathbb{R}$) ;
  - $x_1$, . . . , $x_p$ sont les <a style="color :  #03a9f4">variables explicatives</a> (à valeurs dans $\mathbb{R}$) ;
  - $\mathcal{E}$ est le <a style="color : #e91e63">terme d’erreur</a> aléatoire du modèle ;
  - $β_0, β_1, . . . , β_p$ sont les **paramètres à estimer**.


> - La désignation <a style="color : lightskyblue">multiple</a>  fait référence au fait qu’il y a plusieurs variables
> explicatives xj pour expliquer y.
> - La désignation <a style="color : lightskyblue">linéaire</a>  correspond au fait que le modèle (1) est linéaire.

Pour <a style="color : #e91e63">n observations</a> , on peut écrire le modèle de régression linéaire multiple
sous la forme :

$$y_i = β_0 + \sum_{j=1}^pβ_jx_{ij} + \mathcal{E}_i $$ pour i = 

Dans ce chapitre, on suppose que :
- $\mathcal{E}_i$ est une variable aléatoire, non observée,
- $x_{ij}$ est observé et non aléatoire,
- $y_i$ est observé et aléatoire.

<a style="color : lightskyblue">text</a> 


















