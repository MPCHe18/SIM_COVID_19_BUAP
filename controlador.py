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
from AgentePlusPlus import *
from utilidades import *
import json
from paths import * 

class Controlador:
    def __init__(self, numAgentes = 5, numInfectados = 2, numVacunados = 3, numComorbilidades = 2):
        self.utilidades = Utilidades()
        #contadores para crear los agentes
        contInfectados = 0
        contVacunados = 0
        contComorbilidades = 0

        #lista de agentes
        self.listaAgentes = []

        #Corroborar que numInfectados + numVacunados = numAgentes
        if numAgentes < numInfectados:
            #regresar error
            print("Error  creando Controlador")
            return

        #Crear los agentes
        for index in range(0,numAgentes):
            featureInfectado = False
            featureVacunado = False
            featureComorbilidad = False
            #checar
            if contInfectados < numInfectados:
                featureInfectado = self.utilidades.get_enabled_feature(contInfectados, numInfectados, index, numAgentes)
                if featureInfectado:
                    contInfectados += 1
            
            if contVacunados < numVacunados:
                featureVacunado = self.utilidades.get_enabled_feature(contVacunados, numVacunados, index, numAgentes)
                if featureVacunado:
                    contVacunados += 1
            
            if contComorbilidades < numComorbilidades:
                featureComorbilidad = self.utilidades.get_enabled_feature(contComorbilidades, numComorbilidades, index, numAgentes)
                if featureComorbilidad:
                    contComorbilidades += 1
            
            #crear al agente y agregarlo a la lista
            #nombre = "X", infectado = False, vacunado = False, conmorbilidad = False
            self.listaAgentes.append(AgentePlusPlus(str(index), featureInfectado, featureVacunado, featureComorbilidad))

            #prueba paths
            paths = Paths()

    def getAgentes(self):
        return self.listaAgentes
    
    def move(self):
        for agente in self.listaAgentes:
            agente.move()
    
    def showInfoAgentes(self):
        infoJson = {}
        print("Agente \t Pos \t\t\t Asi \t Est \t Inf \t Vac \t Con \t Dec \t Rec \t inm \t T.E \t T.I")
        for agente in self.listaAgentes:
            info = agente.info()
            infoJson[agente.nombre] = info
        print("\n")
        return infoJson
    
    def tick(self):
        self.move()
        temp_list = []
        for agente in self.listaAgentes:
            agente.tick()
            agente.search_around(self.listaAgentes)
            temp_list.append(agente)
        self.listaAgentes = temp_list
        # cont = 0
        # while cont < len(self.listaAgentes):
        #     temp_list = self.listaAgentes.copy()
        #     self.listaAgentes[cont].tick()
        #     self.listaAgentes[cont].search_around(temp_list)
        #     cont += 1
        res = self.showInfoAgentes()
        #Aqui deberia regresar el diccionario de diccionarios
        return res

    
    def return_json(self):
        pass
