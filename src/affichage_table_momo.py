from robot_package.data_robot_creator import data_robot_creator
from utils.get_table_point import get_table_point

import matplotlib.pyplot as plt
import numpy as np

from robot_package.Robot import Robot



def init_plot(ax, table, robot):
    # Liste des futurs objets à actualiser sur le plot
    data2plot = []

    # Affichage objet fixe, et définition du plot
    ax.plot(table[0], table[1])
    ax.grid()
    ax.axis('equal')
    

    ### Affichage objet mouveant
    # Du robot
    point_robot = robot.get_robot_point()
    plot_robot, = ax.plot(point_robot[0], point_robot[1])
    data2plot.append(plot_robot)


    return data2plot


def update_data(robot):
    robot.update_position() 


def update_plot(data2plot, robot):
    point_robot = robot.get_robot_point()
    data2plot[0].set_data(point_robot[0], point_robot[1])



####################################################################
# MAIN PROGRAM

# Creation des points de la table
fichier_table = './table_config.yaml'
point_table = get_table_point(fichier_table)

# Creation des points capteurs et point robot
fichier_robot = './robot_config.yaml'
point_robot, dist_sensors = data_robot_creator(fichier_robot)

# creation de l'objet robot
robot = Robot(1500, 1000, np.pi/3)
robot.define_robot_shape(np.array(point_robot))

############################
# Affichage
##############################
# Création et initialisation du plot
fig, ax = plt.subplots(1, 1)
data2plot = init_plot(ax, point_table, robot)

# Boucle d'animation
x = 0 # data x pour simuler les capteurs et le déplacement du robot.
while True:
    update_data(robot)
    update_plot(data2plot, robot)
    
    plt.pause(1.0/30)



