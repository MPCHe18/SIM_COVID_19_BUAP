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
from flask import Flask, render_template, request, flash
from flask.json import jsonify
import random
from controlador import *

app = Flask(__name__)

controlador = None

@app.route('/', methods=['POST','GET'])
def home():
    return render_template('principal.html')

@app.route('/sendInfo', methods=['POST','GET'])
def getInfo():
    global controlador
    #print("Entra a sendInfo")
    if request.method == 'POST':
        #print("Es un POST")
        request_data2 = str(request.data)
        request_data = request_data2[3:-2]
        parts = request_data.split(",")
        #print("Data", request_data)
        #Obtener los datos del json
        numAgentes = parts[0].split(":")[1]
        numAgentes = numAgentes[1:-1]
        NumInfectados = parts[1].split(":")[1]
        NumInfectados = NumInfectados[1:-1]
        NumVacunados = parts[2].split(":")[1]
        NumVacunados = NumVacunados[1:-1]
        NumComorbilidades = parts[3].split(":")[1]
        NumComorbilidades = NumComorbilidades[1:-1]
        NumTiempo = parts[4].split(":")[1]
        NumTiempo = NumTiempo[1:-1]
        #NumTiempo = NumTiempo[:-1]
        print("numAgentes: ",numAgentes)
        print("NumInfectados: ",NumInfectados)
        print("NumVacunados: ",NumVacunados)
        print("NumComorbilidades: ",NumComorbilidades)
        print("NumTiempo: ",NumTiempo)
        controlador = Controlador(int(numAgentes), int(NumInfectados), int(NumVacunados), int(NumComorbilidades))
        #return jsonify(estado="creado")
        return controlador.showInfoAgentes()

@app.route('/tick', methods=['POST','GET'])
def getTick():
    global controlador
    if request.method == 'GET':
        print("GET Tick")
        res = controlador.tick()
        #convertir a json
        return res
        #return json.dumps(res)
##Incio del servidor
if __name__ == '__main__':
    app.run(debug = False)
