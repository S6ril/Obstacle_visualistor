# Obstacle Visualisator

Obstacle visualisator permet placer les capteurs sur le robot et de voir en temps réels les obstacles sur la carte.

<table style="width:100%" >
  <tr>
    <th>
    <img width="100%" src="images\Affichage_table.gif" alt="Simulation de la detection d'obstacle du robot">
    </th>
    <th>
    <img width="100%" src="images\Affichage_capteur.gif" alt="Simulation de la detection d'obstacle du robot">
    </th>
  </tr>
  <tr>
    <th>Affichage de la table avec le robot et les obstacles detectés</td>
    <th>Affichage du robot avec ses capteurs, leur direction et les obstacles detectés</td>
  </tr>
</table> 

## Sommaire

  * [Prérequis](#prerequis)
  * [Contexte](#contexte)
  * [Utilisation](#utilisation)
    + [Affichage de la table avec le robot](#affichage-de-la-table-avec-le-robot)
    + [Affichage spécifique au robot](#affichage-sp-cifique-au-robot)
    + [Placement des axes](#placement-des-axes)
      - [De la table](#de-la-table)
      - [Du robot](#du-robot)
  * [Intégration avec des capteurs réels](#int-gration-avec-des-capteurs-r-els)
  * [Auteurs](#auteurs)


## Prérequis

L'utilisation de ce projet nécessite les bibliothèques suivantes:
* numpy
* matplotlib
* pyyaml
* pyserial

Installation sous Windows :
```
py -m pip install numpy matplotlib pyyaml pyserial
```


## Contexte

L'association Valrobotik de l'INSA HDF développe un robot pour participer à la coupe de France de Robotique.

On recherche alors à placer et à utiliser facilement les capteurs du robot. 

## Utilisation

Il existe alors deux programme :
- un programme pour afficher le robot, ainsi que les obstacles sur la table. 
- un programme spécifique à l'affichage du robot, des capteurs et des obstacles mesurés.

### Affichage de la table avec le robot

Le programme `affichage_table.py` permet d'afficher la table avec le robot et les obstacles mesurés (voir premier GIF).

On configure dans un premier temps les dimensions de la table avec le fichier `table_config.yaml`. Il suffit d'entré les dimensions de la table (exemple avec une table carré) :

```yaml
point_table:
  p1:
    x: 0
    y: 0
  p2:
    x: 0
    y: 2000
  p3:
    x: 3000
    y: 2000
  p4:
    x: 3000
    y: 0
```
Puis il faut configurer le robot, notamment sa forme et l'emplacement des différents capteurs (voir section suivante pour la configuration).

### Affichage spécifique au robot

Pour cet affichage, nous nous plaçons dans le repère du robot. `affichage_robot.py` permet d'afficher les capteurs, leur direction et la distance qu'ils mesurent (voir deuxième GIF).

Nous utilisons le fichier `robot_config.yaml`. 
Dans un premier temps, on inscrit la forme du robot :
```yaml
point_robot:  # Création des différents points pour former le robot
  p1:
    x: -150
    y: 50
  p2:
    x: 150
    y: 50
  p3:
    x: 150
    y: -50
...
```
Les noms `p1`, `p2`, ... ne sot pas important, ils permettent seulement de distinguer les points du robot.

Puis on ajoute les différents capteurs à la suite du fichier :

```yaml
ultrason1:
  type: ultrason
  x: 20 # position suivant x en mm
  y: 50 # position suivant y en mm
  theta: -30 #angle en degrès

ultrason2:
  type: ultrason
  x: -30 # position suivant x en mm
  y: -50 # position suivant y en mm
  theta: -190 #angle en degrès
...
```

De même, le nom `ultrason1` n'est pas important, il permet seulement de distinguer les capteurs.

<p align="center">
❗ Deux points, ou deux capteurs ❗<br>❗ ne doivent pas avoir le même nom ❗
</p>

### Placement des axes

#### De la table

Ci dessous on représente la définition des axes utilisés dans ces algorithmes pour le table.

<p align="center">
<img width="75%" src="images\Repère_table_robot.png" alt="Positionnement des axes du robot">
</p>

La table est positionnée à l'horizontal pour mieux être affiché sur un écran d'ordinateur en 21/9.

#### Du robot

Ci dessous on représente la définition des axes utilisés dans ces algorithmes pour le robot.

<p align="center">
<img width="75%" src="images\Repère_robot_capteur.png" alt="Positionnement des axes du robot">
</p>



## Intégration avec des capteurs réels

Il est possible d'interfacer ces affichages avec des capteurs réels. 

J'ai alors créer une surcharge de la fonction `update_data()`. En ajoutant l'argument `carte`, on affiche les distances mesurées par le capteur réel.

Dans un premier temps, il faut créer cet objet carte avec son port série et son bauderate :
```python
from sensor_board.CarteDetecteurObstacle import CarteDetecteurObstacle

# Definition de la carte de capteur
carte = CarteDetecteurObstacle(portserial = "COM8", bauderate = 9600)
```

Puis dans la boucle principale, il suffit de remplacer la fonction `update_data(dist_sensors)` par la fonction `update_data(dist_sensors, carte)` :

```python 
while True:
    # update_data(dist_sensors)
    update_data(dist_sensors, carte)
    ...
```
De cette manière l'affichage affiche les données mesurées en temps réel par la carte des capteurs de distance.

❗❗ Il doit y avoir le même nombre de capteurs inscrits dans le fichier `robot_configuration.yaml` que de capteurs réels sur la carte de detection d'obstacle ❗❗

## Auteurs

 <table style="width:100%" >
  <tr>
    <th>
    <a href="https://github.com/S6ril/">
      <img width=30% src="https://avatars.githubusercontent.com/u/58038125?v=4" />
    </a>
    </th>
    <th>
    <a href="https://github.com/Starfunx">
      <img width=30% src="https://avatars.githubusercontent.com/u/7883804?v=4" />
    </a>
    </th>
  </tr>
  <tr>
    <th>S6ril</td>
    <th>Starfunx</td>
  </tr>
</table> 


<p align="center">
<img width="10%" src="https://avatars.githubusercontent.com/u/39584742?v=4" alt="Logo Valrob">
</p>







