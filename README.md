# SIM_COVID_19_BUAP
## Simulator of Covid-19 epidemic.

This repository contains the project developed during Artificial Intelligence course of Master in Electronics Engineering from Benemérita Universidad Autónoma de Puebla (Mexico).

Here is presented a simulator of spread behavior due to Covid-19 pandemic, disease cataloged as a severe acute illness and determined as a pandemic by WHO on March 2020.

The aim of this work is to provide a resource based on real factors like the main comorbidities detected in Mexico and the most supplied vaccine. This simulator was designed as an agent-based model, in which the interaction instructions are defined in Python language and controlled by a Main code.

## Simulador de epidemia por Covid-19

Este repositorio contiene el código desarrollado para el curso Inteligencia Artificial de la Maestría en Ingeniería Electrónica de la Benemérita Universidad Autónoma de Puebla.

Se presenta un simulador del comportamiento de contagios debido a la pandemia por Covid-19, que es catalogada como una enfermedad aguda severa y que desde Marzo de 2020 fue catalogada por la Organización Mundial de la Salud como pandemia.

El propósito de este trabajo es proporcionar una herramienta basada en factores reales de las principales comorbilidades en México, así como vacunas aplicadas en la misma región. Este simulador se basa en un modelo multiagente en donde las reglas de interacción son definidas en lenguaje Python y controladas por una entidad principal (Main).

# ¿Cómo usarlo?
Este simulador utiliza algunos factores que funcionan como configuración inicial para la representación de diversos escenarios bajo los cuales la enfermedad Covid-19 puede afectar a un grupo de personas (agentes).

Al descargar el paquete de archivos, los archivos importantes del simulador son:

- *app.py*
- *AgentePlusPlus.py*
- *controlador.py*

Se debe ejecutar el archivo *app.py* para iniciar el simulador como un Host Local. Al ejecutar este archivo desde un IDE para lenguaje Python, en la consola se mostrará una URL que deberá ser colocada en el navegador de preferencia. De esta manera se desplegará el simulador, pero el código debe manterese en ejecución, por lo que no se recomienda cerrar el IDE utilizado. Para detener la ejecución se debe presionar la combinación de teclas **Ctrl + c** dentro de la consola del IDE.

Dentro del paquete de archivos se encuentran diversas carpetas que contienen elementos necesarios para la ejecución correcta de todo el código. Se recomienda **no eliminar o editar el nombre de ninguna de estas carpetas**. Las carpetas de importancia son:

- Static
- Templates

En ellas se encuentran los archivos para ejecución en JavaScript para la página web y el archivo en HTML, respectivamente.


El desarrollo de las reglas de interacción se encuentra definido en los archivos *AgentePlusPlus.py*, *controlador.py*, *utilidades.py* y *paths.py*. El primero de estos archivos en Python corresponde al código del agente, donde se definen y ciertos estados esenciales. El siguiente archivo corresponde al Main de las reglas de interacción que controla a todos los agentes instanciados. Los archivos *utilidades.py* y *paths.py* son códigos auxiliares para ejecución de eventos aleatorios y el movimiento del agente.

Cuando se ejecuta el simulador, en el menú lateral izquierdo se deben configurar los parámetros iniciales como son el número total de agentes a desplegar en la interfaz, el número de agentes infectados iniciales, el número de agentes con comorbilidades, así como los que cuentan con una vacuna. Finalmente se definen los días de simulación. Cada uno de los parámetros son seleccionados con las barras de tipo slider.

Para iniciar la ejecución del simulador basta con presionar el botón Configurar dentro del mismo menú. Para cerrar el menú se debe presionar el indicador de las barras horizontales.

# ¿Cómo funciona?
El agente se basa en un algoritmo bajo el cual puede padecer alguno de los estados principales como infectado, inmunidad, deceso y susceptibilidad. Estos últimos son estados implícitos ya que no se encuentran directamente definidos dentro del algoritmo. 

En las siguientes tablas se presentan las propiedades del agente y sus variables de memoria. También se presentan las variables que utiliza el simulador, así como variables auxiliares de importancia para la descripción del funcionamiento del simulador.

## PROPIEDADES DEL AGENTE

| NOMBRE | SIGNIFICADO | TIPO DE VARIABLE |
| ------------- | ------------- |------------- |
| Infectado | Agente con enfermedad Covid-19 | Booleano |
| Inmunidad | Agente recuperado y con inmunidad a Covid-19 | Booleano |
| Asintomático | Agente con estado infectado que pasa a Inmunidad | Booleano |
| Vivo | Agente con estado vivo | Booleano |
| COM | Comorbilidades: estado que influye en probabilidad de recuperación | Booleano |
| Vacunado | Estado que influye en la probabilidad de infección del agente | Booleano |
| msnInf | Mensaje de infección recibido al entrar en el radio de acción de otro agente | Booleano |
| x | Posición en eje x | Numérico flotante |
| y | Posición en eje y | Numérico flotante |

## MEMORIA DEL AGENTE

| NOMBRE | SIGNIFICADO | TIPO DE VARIABLE |
| ------------- | ------------- |------------- |
| TE | Tiempo de Enfermedad | Numérico entero |
| TI | Tiempo de inmunidad | Numérico entero |
| evRec | Evento aleatorio para recuperación | Numérico flotante |
| evInf | Evento aleatorio para infección | Numérico flotante |

## PROPIEDADES DEL SIMULADOR

| NOMBRE | SIGNIFICADO | TIPO DE VARIABLE |
| ------------- | ------------- |------------- |
| numAg | Número de agentes totales | Numérico entero |
| numInf | Número de agentes infectados | Numérico entero |
| numCOM | Número de agentes con comorbilidades | Numérico entero |
| numVac | Número de agentes vacunados | Numérico entero |
| Días | Número de días de simulación | Numérico entero |
| numAgInf | Número actual de agentes infectados | Numérico entero |
| numAgDec | Número actual de agentes fallecidos | Numérico entero |
| i, k, h | Variables auxiliares para ciclos | Numérico entero |

El código principal que controla la ejecución del simulador se presenta en el siguiente diagrama de flujo:

<img src="https://github.com/MPCHe18/SIM_COVID_19_BUAP/blob/main/static/images/principal.jpeg" width="400" >

El ciclo de creación de agentes se encarga de asignar estados iniciales para que cada uno de los agentes instanciados comience con información definida. Este ciclo se repite para cada agente hasta llenar una Lista de Agentes que funciona como elemento para comunicar los estados de los agentes hacia el servidor web.

A través de eventos aleatorios es posible determinar si un agente tendrá como parámetro inicial el estado de infección, vacuna y comorbilidad dependiendo la disponibilidad. Dentro del caso de infección, el agente podrá poseer un subestado que es Asintomático, el cual genera que el agente se recupere sin importar otros factores, sin embargo, éste podrá contagiar a otros agentes susceptibles.

<img src="https://github.com/MPCHe18/SIM_COVID_19_BUAP/blob/main/static/images/Crea_agentes.jpeg" width="600" >

El siguiente paso al finalizar la creación de agentes es la evaluación de los mismos por cada día (tick) de simulación.

El proceso inicia al evaluar si el agente actual está vivo, ya que de lo contrario, si el agente fallece por la enfermedad éste deja de operar de la misma manera, cambiando su indicador de color a negro y permaneciendo estático, por lo que el resto de procesos no se evalúan.

Si el agente está vivo, se evalúa el estado de infección o de inmunidad. Si el agente no cuenta con ninguno de estos estados, más sin embargo, está vivo, se determina que el agente se encuentra en el estado susceptible, que es un estado implícito del simulador. En este caso solo se evalúa si el agente recibe un mensaje de infección cuando entra en el radio de acción de un agente infectado.

El mensaje de infección desencadena un proceso de evaluación basado en la probabilidad de infección por la vacuna. Se utiliza como factor esencial el porcentaje de inmunidad de la vacuna AstraZeneca, que es del 79%. Si la probabilidad de infección es del 100%, al restar la inmunidad de la vacuna y eliminar el porcentaje, se compara un número aleatorio asignado en la variable de evento de infección y se determina si existe un cambio de estado.

<img src="https://github.com/MPCHe18/SIM_COVID_19_BUAP/blob/main/static/images/Evalua_agentes.jpeg" width="600" >

Si el agente presenta el estado de infectado, se hace un chequeo por cada tick de simulación durante la evaluación de agentes. El chequeo inicia con la evaluación de tiempo de enfermedad (TE) que es asignado de manera aleatoria. Si el tiempo es mayor a cero, entonces se ejecuta un sub-ciclo en el que se buscan a los agentes que se encuentran dentro del radio de acción del agente actual; a los agentes que se encuentran cerca se les asigna un mensaje de infección.

En caso de que el tiempo de enfermedad haya finalizado, entonces se evalúa una transición de estados ya que el agente puede pasar al estado de inmunidad o fallecer.

<img src="https://github.com/MPCHe18/SIM_COVID_19_BUAP/blob/main/static/images/Infeccion.jpeg" width="400" >

La transición de estados está influenciada primeramente por el estado de asintomático del agente, ya que en caso de tenerlo, su estado pasa a inmunidad de manera automática; el comportamiento de la enfermedad Covid-19 describe esta decisión.

Si el agente no es asintomático, entonces se asigna un número aleatorio en su variable de evento de recuperación y posteriormente de evalúa si el agente cuenta con comorbilidades. Se utilizan las principales comorbilidades presentadas en México, y sus porcentajes de incidencia durante la pandemia por Covid-19. Si el agente no cuenta con comorbilidades, su probabilidad de recuperarse, dado el evento aleatorio, es mayor en comparación con un agente que si posee comorbilidades.

<img src="https://github.com/MPCHe18/SIM_COVID_19_BUAP/blob/main/static/images/Estados.jpeg" width="400" >

Finalmente, dentro del ciclo de evaluación de agentes, si el agente presenta inmunidad, se evalúa únicamente el tiempo de inmunidad, asignado de manera aleatoria, ya que estos agentes solo pueden moverse pero no pueden ser contagiados hasta que su tiempo finaliza.

<img src="https://github.com/MPCHe18/SIM_COVID_19_BUAP/blob/main/static/images/Inmunidad.jpeg" width="400" >

Cuando un agente muere a causa de la enfermedad, cambia su color a negro y se convierte en un agente estático, ya que deja de moverse. Los agentes de color verde corresponden al estado de susceptibilidad, mientras que el color azul representa a los agentes con inmunidad. Finalmente, los de color rojo son agentes infectados sintomáticos y los de color amarillo son asintomáticos.

Para los casos de agentes verdes y azules, solo se desplazan a lo largo del cuadro central, sin embargo, los agentes con inmunidad no pueden ser contagiados durante su periodo de tiempo definido de manera aleatoria.

Los agentes infectados, para ambos casos, tienen la capacidad de contagiar a otros agentes susceptibles. Cuando su tiempo de enfermedad termina, se evalúa si cambio de estado dependiendo de si cuenta con comorbilidades o no. Para el caso de los agentes susceptibles, cuando entran en contacto con un agente infectado, se evalúa la probabilidad de infección de acuerdo al factor de vacuna.

# Resultados
Durante la ejecución del simulador, los agentes instanciados se moverán dentro del cuadro central de manera aleatoria. En cuanto un agente susceptible entra en el radio de acción de un agente infectado, se evalúa un evento aleatorio y basado en una probabilidad por vacuna. Los cambios de color suceden con cada tick de ejecución.

En la parte inferior del cuadro principal se presentan una serie de gráficos que presentan los cambios de estados en tiempo real. De esta manera se presentan caso activos, recuperados, susceptibles y decesos por cada día de ejecución.

En la parte superior del cuadro principal se encuentra una barra azul que indica el avance del tiempo de simulación configurado. Para reiniciar el simulador es necesario recargar la página desde el navegador.

