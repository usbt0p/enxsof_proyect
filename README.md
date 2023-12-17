# SIMULACIÓN DE UN ENTORNO DOMOTIZADO

El propósito fundamental de este proyecto es diseñar e implementar un sistema que permita simular la interacción fluida de diversos agentes. Estos agentes estarán destinados a satisfacer las necesidades diarias de los residentes, haciendo especial énfasis en la usabilidad y la eficiencia.

Este programa ofrece un entorno domótico interactivo que se actualiza en tiempo real, centrado en simplificar y controlar las acciones necesarias para mantener un estilo de vida saludable. Algunas de las acciones y características destacadas del programa incluyen: 

Visualización en tiempo real: El entorno domótico proporciona una representación visual en tiempo real de la casa, incluyendo objetos y movimientos de los robots asistentes.

Control de robots asistentes: Permite el control y la coordinación de las acciones de los robots asistentes en el entorno doméstico.

Registro de movimientos y acciones: Registra y presenta información detallada sobre los movimientos y acciones realizadas por los robots asistentes, proporcionando una visión completa de actividades en la casa.

Monitorización de suministros: Informa sobre el nivel de suministros en la casa, abarcando alimentos, medicamentos y otros elementos esenciales para el cuidado de la salud. 

Visualización de constantes vitales: El entorno domótico ofrece la capacidad de poder visualizar constantes vitales como la temperatura o la tensión arterial o la frecuencia cardíaca para una interacción más inmersiva y realista del usuario. 



## Instalación del Proyecto

Para asegurar el correcto funcionamiento del proyecto en cualquier equipo, es esencial contar con el intérprete de Python 3 instalado.

Se puede acceder a la web oficial de Python para descargar el intérprete con la versión necesaria para la ejecución del programa desarrollado. A continuación, se dispone del link: https://www.python.org/downloads/


Se recomienda tener Visual Studio Code instalado en el equipo para facilitar la ejecución del proyecto (su instalación, como se ha comentado, es opcional). A continuación, se dispone del link para proceder a su descarga según el sistema operativo de preferencia del usuario: https://code.visualstudio.com/download 


Para la ejecución correcta del programa, se precisa de la instalación de las siguientes dependencias o módulos de Python (estas mismas se pueden observar dentro del archivo requirements.txt) junto a su versión correspondiente que se presentan a continuación: 

    asttokens == 2.4.1
    colorama == 0.4.6
    contourpy == 1.2.0
    cycler == 0.12.1
    executing == 2.0.1
    fonttools == 4.46.0
    icecream == 2.1.3
    kiwisolver == 1.4.5
    matplotlib == 3.8.2
    numpy == 1.26.2
    packaging == 23.2
    Pillow == 10.1.0
    Pygments == 2.17.2
    pyparsing == 3.1.1
    python-dateutil == 2.8.2
    six == 1.16.0


## Pasos para poner en Funcionamiento el Programa
Descargar el archivo.zip que contiene el proyecto. 
Descomprime el archivo descargado en la carpeta Documentos en tu dispositivo. 

Ejecución desde la terminal: 
Abre la terminal de tu dispositivo.
Navega hasta la ruta donde se encuentra el archivo descomprimido.
Ejecuta el siguiente comando: 
`python3 <ruta donde se ha descomprimido el archivo>/execute.py`


Ejecución en Visual Studio Code:
Abre Visual Studio Code.
Importa el proyecto o abre el archivo correspondiente.
Ejecuta el archivo del proyecto.

## Future features
- Algoritmo procedural de generación de mapas.
- Inclusión de nuevos objetos con sprites propios.
- Añadir un log por salida del sistema para eventos de agentes.
- Añadir la opción de tener múltiples pisos.
- Easter eggs de bailoteo y agentes de relleno.
- Animar ciclos de movimiento para agentes.
- Eliminar colisiones entre agentes de forma dinámica (dos agentes no pueden ocupar una misma casilla, arreglar paso simultáneo por puertas, por pasillos estrechos, etc.)
- Añadir un widget a la vista que permita la entrada de comandos por parte del usuario.
- Transformación lineal de la matriz de (y, x) a (x, y), y consiguiente refactorización del código.
- Añadir textura al suelo.
- Permitir interacción con el ratón sobre elementos del modelo (agentes, objetos)
- Mejorar la GUI para tener una apariencia más moderna.
- Dibujar objetos individualmente en la interfaz gráfica en vez de repintar la interfaz entera.
- Arreglar bug en el que los agentes se pueden colocar sobre una puerta abierta al asignar un lugar aleatorio al que moverse.
- Añadir comando para mandar a un agente ir a un cierto sitio.

