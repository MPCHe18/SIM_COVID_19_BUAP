"""
Este archivo pertenece al proyecto Simulador de contagios por pandemia de Covid-19, desarrollado 
por alumnos de la Facultad de Ciencias de la Electrónica, de la Benemérita Universidad Autónoma de Puebla. 
El proyecto fue desarrollado para la materia Inteligencia Artificial del programa de 
Maestría en Ingeniería Electrónica, opción Instrumentación Electrónica, del periodo Otoño 2021.
La motivación para el desarrollo de este simulador parte de la pandemia que se vive actualmente 
desde Marzo de 2020 provocada por la enfermedad Covid-19, causada por el nuevo coronavirus SARS-CoV-2. 
Esta enfermedad es catalogada como aguda severa que ataca al sistema respiratorio principalmente.
Una de las principales características de esta enfermedad es la rápida propagación mediante 
gotículas de saliva expulsadas por la boca al estornudar, toser, hablar o gritar.
El comportamiento de contagio es muy acelerado, y aún más con la aparición de nuevas cepas. 
Bajo estos términos, se desarrolló este simulador con la finalidad de proyectar de manera 
generalizada la propagación del virus.
El simulador se basa en el paradigma multiagente donde se define un código principal que controla
la ejecución general y el código del agente, que se encuentra encapsulado. Su desarrollo se basa 
en el lenguaje Python, mientras que el diseño de la página web es realizado mediante la 
herramienta Flask.
Para el correcto funcionamiento del simulador se recomienda tener en la misma carpeta que 
este archivo, el resto del proyecto. Todo el proyecto se puede encontrar en el repositorio 
de GitHub en https://github.com/MPCHe18/SIM_COVID_19_BUAP. 
Así mismo, es necesario instalar algunas bibliotecas como Flask y random. Al ejecutar el 
archivo app.py se muestra en consola una URL que debe ser insertada en el navegador de su 
preferencia. No se requiere conexión a Internet ya que se ejecuta desde el PC como un Local Host.

This file belongs to the Covid-19 pandemic contagion simulator project, developed by students 
from the Faculty of Electronics Sciences of the Benemérita Universidad Autónoma de Puebla. 
The project was developed for the Artificial Intelligence subject of the Master's program in Electronic Engineering, 
Electronic Instrumentation option, of the Autumn 2021 period.
The motivation for the development of this simulator stems from the pandemic that is currently 
being experienced since March 2020 caused by the Covid-19 disease, caused by the new SARS-CoV-2 
coronavirus. This disease is classified as severe acute that mainly attacks the respiratory 
system. One of the main characteristics of this disease is the rapid spread by droplets of saliva
 expelled from the mouth when sneezing, coughing, talking or screaming.
The contagion behavior is very accelerated, and even more so with the appearance of new strains.
Under these terms, this simulator was developed in order to project the spread of the virus in a 
generalized way.
The simulator is based on the multiagent paradigm where a main code is defined that controls the 
general execution and the agent code, which is encapsulated. Its development is based on the 
Python language, while the web page is designed using the Flask tool.
For the correct functioning of the simulator, it is recommended to have the rest of the project 
in the same folder as this file. The entire project can be found in the GitHub repository 
at https://github.com/MPCHe18/SIM_COVID_19_BUAP.
Likewise, it is necessary to install some libraries such as Flask and random. When executing 
the app.py file, a URL is displayed on the console that must be inserted in the browser of your 
choice. No internet connection is required as it runs from the PC as a Local Host.
"""
import csv

RUTAS = ["static/paths/rutas-0.csv", "static/paths/rutas-1.csv", "static/paths/rutas-2.csv"
        , "static/paths/rutas-3.csv", "static/paths/rutas-4.csv", "static/paths/rutas-5.csv"
        , "static/paths/rutas-6.csv", "static/paths/rutas-7.csv", "static/paths/rutas-8.csv"]

class Paths:
    def __init__(self):
        self.god_list = []
        for archivo in RUTAS:
            with open(archivo) as file:
                reader = csv.reader(file)
                granma_list = []
                mother_list = []
                temp_list = []
                for row in reader:
                    if row[0] == '':
                        mother_list.append(temp_list)
                        temp_list = []
                    elif row[0] == 'X':
                        pass
                    else:
                        temp_list.append(row)
                mother_list.append(temp_list)
                temp_list = []
                #crear lista con punto de inicio y final
                for way in mother_list:
                    temp_list.append(self.get_point_start_end(way[0]))
                    temp_list.append(self.get_point_start_end(way[len(way)-1]))
                    temp_list.append(way)
                    granma_list.append(temp_list)
                    temp_list = []
                #print("granma list")
                #print(granma_list)
            self.god_list.append(granma_list)
        #print("god list")
        #print(self.god_list)


        #print("mother list")
        #print(mother_list)
    
    def get_god_list(self):
        return self.god_list

    
    def get_point_start_end(self, point):
        #print("get_point_start_end: ", point)
        if point[0] == "3":
            if point[1] == "3":
                return 2
            elif point[1] == "7":
                return 1
            elif point[1] == "13":
                return 0
            else:
                return 0
        elif point[0] == "13":
            if point[1] == "3":
                return 3
            elif point[1] == "7":
                return 8
            elif point[1] == "13":
                return 7
            else:
                return 0
        elif point[0] == "23":
            if point[1] == "3":
                return 4
            elif point[1] == "7":
                return 5
            elif point[1] == "13":
                return 6
            else:
                return 0
