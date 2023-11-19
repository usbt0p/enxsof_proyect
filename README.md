# enxsof_proyect
Repositorio para el proyecto de Enxeñaría De Software del Grupo 1.2 para el desarrollo de un entorno domótico simulado.

> [!NOTE]  
> For correct usage now the user should add the project > directory to the environment variable PYTHONPATH so that Python knows where to search for the executable files.

One way of doing it is this, do the following after downoading the project:

    Go, through command line, to the root directory in which the project was downloaded in your PC. For example if you downloaded it to C:\user\documents, go to C:\user\documents\fasta_project.

    Once there, you must add the path to the environment variable. In Windows, type the followng command: $env:PYTHONPATH = '.' On Linux, type: export PYTHONPATH=.

    Of course, the same would work if '.' is substituted with the absolute path of the directory.

    This must be done each time the terminal is opened to use the project, since the environment variable dissapears after closing it.




Documentación del Proyecto de Entorno Domótico
Tabla de Contenidos
•	[Resumen del Proyecto](https://github.com/usbt0p/enxsof_proyect/issues/19#resumen-del-proyecto)
•	[Requisitos del Sistema](https://github.com/usbt0p/enxsof_proyect/issues/19#requisitos-del-sistema)
•	[Arquitectura del Sistema](https://github.com/usbt0p/enxsof_proyect/issues/19#arquitectura-del-sistema)
•	[Componentes del Sistema](https://github.com/usbt0p/enxsof_proyect/issues/19#componentes-del-sistema)
o	[Entorno (Environment)](https://github.com/usbt0p/enxsof_proyect/issues/19#entorno-environment)
o	[Agentes (Agent)](https://github.com/usbt0p/enxsof_proyect/issues/19#agentes-agent)
o	[Objetos (Object)](https://github.com/usbt0p/enxsof_proyect/issues/19#objetos-object)
o	[Acciones (Action)](https://github.com/usbt0p/enxsof_proyect/issues/19#acciones-action)
•	[Interfaz Gráfica](https://github.com/usbt0p/enxsof_proyect/issues/19#interfaz-gr%C3%A1fica)
o	[Características de la Interfaz Gráfica](https://github.com/usbt0p/enxsof_proyect/issues/19#caracter%C3%ADsticas-de-la-interfaz-gr%C3%A1fica)
•	[Uso del Código](https://github.com/usbt0p/enxsof_proyect/issues/19#uso-del-c%C3%B3digo)
•	[Ejecución de Pruebas](https://github.com/usbt0p/enxsof_proyect/issues/19#ejecuci%C3%B3n-de-pruebas)
•	[Licencia](###Licencia)


---

### Resumen del Proyecto

Este proyecto tiene como objetivo desarrollar un entorno domótico con el propósito de recrear y analizar interacciones entre agentes autónomos encargados de desempeñar distintos roles específicos en un entorno doméstico. El sistema se apoya en la aplicación del patrón de diseño Modelo-Vista-Controlador (MVC), una elección que no solo implica la organización estructural del código sino que también imparte un enfoque modular para mejorar la interacción y comunicación entre los agentes y los objetos dentro de este entorno simulado.

### Requisitos del Sistema
Los requisitos del sistema definen las funcionalidades y características que el software debe cumplir:
**Funcionales**

_•	Creación Dinámica de Agentes y Objetos:_ El sistema debe permitir la creación dinámica de agentes y objetos, ofreciendo flexibilidad en la configuración del entorno. Los usuarios pueden agregar agentes y objetos en cualquier momento durante la ejecución del sistema, sin interrupciones significativas.
•	_Interacciones Complejas de agentes:_  Además de movilidad, los agentes deben poder realizar interacciones más complejas, como la colaboración para realizar tareas específicas. Podrán realizar acciones como abrir armarios, entregar y recoger objetos... Los agentes pueden coordinarse para ejecutar acciones conjuntas, mejorando así la simulación de escenarios realistas.
•	_Acciones Contextuales:_  Los agentes deben realizar acciones contextuales basadas en la presencia de otros agentes u objetos de su entorno. Por ejemplo, un agente puede decidir recoger un objeto solo si otro agente está cerca, lo que refleja comportamientos más sofisticados.
•	_Automatización de Tareas:_  Se debe permitir la automatización de ciertas tareas, donde los agentes pueden ejecutar secuencias predefinidas de acciones. Los usuarios pueden programar secuencias de acciones para que los agentes las ejecuten de manera autónoma.

**No Funcionales**

•	_Rendimiento en Tiempo Real Mejorado._  El sistema debe no solo responder en tiempo real, sino hacerlo de manera eficiente incluso cuando el número de agentes y objetos aumenta. El rendimiento del sistema se mantienen constante incluso con entornos complejos y gran cantidad de interacciones.
•	_Escalabilidad Avanzada._  La arquitectura del sistema debe ser altamente escalable, permitiendo la incorporación de nuevos tipos de agentes y objetos de manera transparente. La adición de nuevos componentes no afecta negativamente la estabilidad y funcionalidad del sistema.
•	_Mantenibilidad Documentada:_  La documentación del código no solo debe ser clara, sino que también debe incluir explicaciones detalladas sobre la lógica interna y la relación entre los diferentes módulos. Los desarrolladores pueden comprender fácilmente el código y realizar mejoras sin riesgo de introducir errores.
•	_Adaptabilidad a Cambios de Configuración_  El sistema debe ser capaz de adaptarse a cambios dinámicos en la configuración del entorno, como la adición o eliminación de agentes u objetos. Los cambios en la configuración se reflejan de manera coherente en el comportamiento del sistema sin requerir reinicios.

### Arquitectura del Sistema

La sección "Arquitectura del Sistema" proporciona una visión detallada de la estructura organizativa y los principios subyacentes que rigen el diseño del entorno domótico simulado. Este análisis arquitectónico es esencial para que desarrolladores y contribuyentes comprendan la disposición interna del sistema y facilita la colaboración en futuras mejoras. A continuación, se detallan los aspectos clave de esta sección:

**Fundamentación en el Patrón MVC**

•	La arquitectura del sistema se basa en el patrón de diseño Modelo-Vista-Controlador (MVC).
•	Se proporciona una explicación detallada de cómo este patrón organiza el código en tres componentes 

**interconectados: Modelo, Vista y Controlador.**

•	Destaca los beneficios de la separación de responsabilidades para mejorar la claridad estructural, el mantenimiento y la escalabilidad.

**Componentes Interconectados**

•	Se describen cada uno de los componentes del patrón MVC y su papel en el entorno domótico:
•	_Modelo (Environment):_  Gestiona el estado global del entorno, almacenando información sobre agentes, objetos, percepciones y acciones.
•	_Vista (Interfaz Gráfica):_  Utiliza tkinter para proporcionar una representación visual interactiva del entorno, mejorando la experiencia del usuario y permitiendo una comprensión intuitiva.
•	_Controlador:_  Facilita la comunicación entre el Modelo y la Vista, gestionando las interacciones y acciones en el entorno.

**Estructura Modular y Escalabilidad**

•	La arquitectura se enfoca en la modularidad para facilitar el desarrollo, mantenimiento y escalabilidad del entorno domótico.
•	La separación de los componentes permite la adición de nuevas funcionalidades o la modificación de existentes sin afectar otras partes del sistema.
•	La estructura escalonada fomenta la incorporación transparente de nuevos tipos de agentes, objetos u otras expansiones.

**Ventajas de MVC**

•	Se destacan las ventajas específicas de la elección del patrón MVC para la arquitectura:
•	Organización Estructural: Claridad en la organización del código.
•	Modularidad: Facilita la adición y modificación de componentes.
•	Escalabilidad: Permite el crecimiento del sistema sin comprometer su estabilidad.
•	Interconexión Clara: Mejora la comunicación entre los diferentes aspectos del sistema.

**Mejoras en la Interacción y Comunicación**

•	Se explica cómo la arquitectura MVC mejora la interacción y comunicación entre agentes y objetos en el entorno simulado.
•	La estructura organizativa promueve una gestión más efectiva de las acciones, percepciones y cambios en el estado global.

En resumen, la Arquitectura del Sistema ofrece una comprensión profunda de cómo la elección del patrón MVC y la organización modular contribuyen a la eficiencia, escalabilidad y mantenibilidad del entorno domótico. Este análisis 
arquitectónico sienta las bases para el desarrollo continuo y la expansión del proyecto.

### Componentes del Sistema


**Agentes (Agent)**

Representa las entidades autónomas que interactúan con el entorno. Cada agente tiene una identificación única, una posición en el entorno y un inventario de objetos.

**Atributos**

•	name: Identificador único del agente.
•	position: Posición actual del agente en el entorno.
•	inventory: Objetos que el agente lleva.

**Objetos (Object)**

Define los elementos con los que los agentes pueden interactuar en el entorno. Cada objeto tiene un identificador único y una posición en el entorno.

**Atributos**

•	name: Identificador único del objeto.
•	position: Posición actual del objeto en el entorno.

**Acciones (Action)**

Define las operaciones que los agentes pueden realizar en el entorno. Cada acción tiene un tipo y argumentos específicos asociados.

**Estructura**

•	action_type: Tipo de acción que el agente desea llevar a cabo.
•	kwargs: Argumentos específicos asociados a la acción.

### Interfaz Gráfica

Utiliza la bilblioteca tkinter para ofrecer una representación visual interactiva del entorno y sus componentes. Esto facilita la creación de elementos de interfaz permitiendo la representación gráfica intuitiva del estado del entorno. La interfaz gráfica no solo mejora la experiencia del usuario al proporcionar una visualización en tiempo real, sino que también sirve como herramienta didáctica para comprender las interacciones y dinámicas del sistema de manera más accesible.

**Características de la Interfaz Gráfica**

•	_Representación Visual:_  La interfaz gráfica presenta visualmente la disposición del entorno, incluyendo la posición de agentes y objetos. Los elementos visuales se actualizan dinámicamente para reflejar los cambios en el entorno en tiempo real.
•	_Controles Interactivos:_  La interfaz incluye controles interactivos que permiten a los usuarios interactuar directamente con el entorno. Por ejemplo, se pueden incorporar determinados elementos para ejecutar acciones específicas o cambiar la configuración del entorno.
•	_Indicadores de Estado:_ Se incorporan indicadores visuales para representar el estado actual de los agentes y objetos.
•	_Información Contextual:_  La interfaz gráfica puede proporcionar información contextual adicional, como mensajes 
de estado, registro de acciones y notificaciones para resaltar eventos significativos en el entorno.

### Uso del Código

La sección "Uso del Código" proporciona ejemplos claros y detallados sobre cómo interactuar con el sistema a través del código fuente del proyecto de entorno domótico. Este recurso sirve como guía práctica tanto para desarrolladores que deseen comprender la implementación interna como para usuarios que buscan utilizar eficazmente las funcionalidades ofrecidas. Aquí se presentan los aspectos clave de esta sección:

**Inicialización del Entorno**

•	Se proporciona un ejemplo detallado sobre cómo inicializar el entorno domótico antes de realizar cualquier interacción.
•	Incluye la configuración inicial, como la definición de agentes, objetos y percepciones iniciales.
•	Facilita a los usuarios y desarrolladores una comprensión rápida de los pasos necesarios para poner en marcha el sistema.

**Adición de Agentes y Objetos**

•	Se presentan ejemplos que ilustran cómo agregar dinámicamente agentes y objetos durante la ejecución del sistema.
•	Destaca la flexibilidad del entorno para permitir la incorporación de nuevos elementos sin interrupciones significativas.
•	Proporciona casos de uso comunes para la creación dinámica de entidades en el entorno domótico.

**Ejecución de Acciones**

•	Ofrece ejemplos específicos de cómo los agentes pueden ejecutar acciones en el entorno domótico.
•	Cubre acciones simples y complejas, destacando la variedad de interacciones posibles.
•	Proporciona claridad sobre la sintaxis y la lógica detrás de la ejecución de acciones dentro del sistema.

**Actualización de Percepciones**

•	Describe cómo se actualizan las percepciones en respuesta a cambios en el entorno.
•	Proporciona ejemplos que demuestran cómo las percepciones individuales y globales evolucionan con las interacciones de los agentes.
•	Facilita la comprensión de cómo el sistema mantiene un estado coherente en tiempo real.
Ejemplos Prácticos
•	Incluye ejemplos prácticos y casos de uso típicos para ayudar a los usuarios a comprender la aplicación real del código.
•	Estos ejemplos pueden abordar situaciones específicas de entornos domésticos simulados, mostrando cómo el sistema responde a escenarios comunes.

En general, la sección de "Uso del Código" se presenta como una guía integral para que los desarrolladores y usuarios comprendan y utilicen efectivamente el sistema domótico. Los ejemplos detallados y los casos de uso prácticos garantizan una comprensión profunda de la implementación y fomentan el uso adecuado de las funcionalidades proporcionadas por el proyecto.

### Ejecución de Pruebas

Las pruebas unitarias son un componente esencial en el desarrollo de software que garantiza la robustez y fiabilidad del código. En el contexto de Python, el módulo unittest proporciona una estructura sólida para la creación y ejecución de pruebas unitarias. Este documento aborda la implementación de pruebas unitarias para clases en Python, centrándose específicamente en clases que representan objetos en un sistema.

**Objetivo:**

El propósito principal de las pruebas es asegurar que cada componente del software, en este caso, clases, funcione como se espera. Las pruebas (test) se diseñan para validar el comportamiento de las clases en diversas situaciones, garantizando que los métodos, propiedades y funcionalidades específicas sean coherentes y produzcan resultados correctos.

**Estructura Básica de las Pruebas:**

1.	_Configuración Inicial (setUp):_
•	Cada conjunto de pruebas comienza con un método setUp, que se encarga de la configuración inicial necesaria para las pruebas. Esto puede incluir la creación de instancias de las clases que se van a probar u otras inicializaciones necesarias.
2.	_Pruebas Individuales:_
•	Cada método de prueba individual, que comienza con la palabra clave test, se centra en una funcionalidad específica de la clase bajo prueba.
•	Las pruebas evalúan la inicialización de la clase con valores predeterminados y personalizados, así como la manipulación de propiedades y comportamientos específicos.
3.	_Assertions:_
•	Se utilizan afirmaciones (assert) para verificar que los resultados esperados coincidan con los resultados reales. Si una afirmación falla, la prueba se considera no válida y se genera una notificación.
La implementación de pruebas unitarias proporciona una base sólida para el desarrollo de software, mejorando la confianza en la calidad y el rendimiento del código. Al incorporar pruebas unitarias para clases en Python, se facilita la detección temprana de posibles problemas  y  garantizar la robustez y confiabilidad del entorno domótico simulado. Lo que fomenta un desarrollo más eficiente y sostenible.


### Licencia

Esta proporciona información detallada sobre los términos y condiciones bajo los cuales se distribuye el proyecto de entorno domótico. Estos detalles legales son cruciales para garantizar la transparencia en el uso y la colaboración, brindando a los usuarios y colaboradores una comprensión clara de sus derechos y responsabilidades. A continuación, se presentan los elementos clave de esta sección:

**Tipo de Licencia**

•	Se especifica claramente el tipo de licencia bajo el cual se distribuye el software (por ejemplo, MIT, GPL, Apache, etc.).
•	Los términos y restricciones asociados con la licencia se presentan de manera concisa para una fácil comprensión.

**Derechos y Restricciones**

•	Se detallan los derechos otorgados a los usuarios y colaboradores, como la libertad para usar, modificar y distribuir el software.
•	Las restricciones, si las hay, se explican para establecer límites claros sobre la responsabilidad y el uso adecuado.

**Cláusulas Específicas**

•	Se incluyen cláusulas específicas relacionadas con la distribución, garantías y responsabilidades.
•	Pueden abordarse aspectos como la inclusión de avisos de copyright, la ausencia de garantías y las limitaciones de responsabilidad.

**Reconocimiento de Contribuciones Externas**

•	Se especifica cómo se reconocen las contribuciones externas al proyecto.
•	Puede incluir detalles sobre cómo se incorporan los créditos y la atribución a los colaboradores.

**Cambios en la Licencia**

•	Se informa sobre cómo los cambios en la licencia se manejarán y comunicarán.
•	Puede incluir detalles sobre el proceso de actualización de la licencia en versiones futuras del software.

**Cumplimiento de Normativas**

•	Se destaca el compromiso del proyecto de cumplir con las regulaciones y normativas legales relevantes.
•	Esto garantiza la conformidad del proyecto con estándares legales y éticos.

**Aceptación de Términos**

•	Se indica claramente que el uso o contribución al proyecto implica la aceptación de los términos de la licencia.
•	Esto establece un acuerdo formal entre el usuario o colaborador y el proyecto.

La licencia no solo cumple un papel legal sino que también contribuye a la construcción de una comunidad transparente y ética alrededor del proyecto de entorno domótico. Proporciona la base para la colaboración abierta y el uso responsable del software desarrollado.



