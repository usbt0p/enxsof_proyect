La clase Environment maneja la mutabilidad de la posición de los agentes, permitiendo que se actualicen sus posiciones. Además, la acción de recoger un objeto ('pick') verifica que el agente esté en la misma posición que el objeto antes de permitir que se añada al inventario del agente.

En el ejemplo proporcionado, el agente 'robot' se ha movido a la nueva posición [1, 1]. El agente 'human' intentó recoger el 'medkit', pero como el agente no está en la misma posición que el 'medkit', la acción no tendría efecto según la lógica actual del método execute_action.

El estado actual del entorno después de ejecutar las acciones es el siguiente:

Agente 'robot' en la posición [1, 1] con su inventario y percepciones vacías.
Agente 'human' en la posición [4, 4] con su inventario y percepciones vacías.
Objetos 'beer' y 'medkit' en sus respectivas posiciones [2, 2] y [3, 3]
