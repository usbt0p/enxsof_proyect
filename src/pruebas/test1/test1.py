# Crear el resto del código para el entorno, excluyendo la vista gráfica.
# Esta clase Environment gestionará las percepciones y las acciones de los agentes.

class Environment:
    def __init__(self):
        # Inicializar el estado del entorno con un diccionario para representar las posiciones de los objetos y agentes
        self.state = {
            'agents': {},
            'objects': {}
        }

    def init(self, agents, objects):
        """Inicializa el entorno con agentes y objetos."""
        for agent in agents:
            self.state['agents'][agent['name']] = agent['position']
        for obj in objects:
            self.state['objects'][obj['name']] = obj['position']

    def add_percept(self, agent_name, percept):
        """Añade una percepción para un agente específico."""
        if agent_name in self.state['agents']:
            self.state['agents'][agent_name]['percepts'].append(percept)

    def remove_percept(self, agent_name, percept):
        """Elimina una percepción específica de un agente."""
        if agent_name in self.state['agents']:
            self.state['agents'][agent_name]['percepts'].remove(percept)

    def clear_percepts(self, agent_name=None):
        """Limpia las percepciones de todos los agentes o de uno específico."""
        if agent_name:
            self.state['agents'][agent_name]['percepts'] = []
        else:
            for agent in self.state['agents'].values():
                agent['percepts'] = []

    def get_percepts(self, agent_name):
        """Obtiene las percepciones de un agente específico."""
        return self.state['agents'][agent_name]['percepts']

    def execute_action(self, agent_name, action, params):
        """Ejecuta una acción de un agente."""
        # Esta es una simplificación. En un sistema real, las acciones podrían incluir moverse, recoger un objeto, etc.
        if action == 'move':
            # Mover al agente a una nueva posición
            self.state['agents'][agent_name]['position'] = params['new_position']
            return True
        elif action == 'pick':
            # Recoger un objeto
            object_name = params['object']
            if self.state['objects'].get(object_name) == self.state['agents'][agent_name]['position']:
                self.state['agents'][agent_name]['inventory'].append(object_name)
                # Eliminar el objeto del entorno
                del self.state['objects'][object_name]
                return True
        # Más acciones podrían ser añadidas aquí
        return False

# Ejemplo de cómo inicializar y usar la clase Environment:
env = Environment()

# Supongamos que tenemos dos agentes y dos objetos en el entorno
agents = [
    {'name': 'robot', 'position': (0, 0), 'percepts': [], 'inventory': []},
    {'name': 'human', 'position': (4, 4), 'percepts': [], 'inventory': []}
]
objects = [
    {'name': 'beer', 'position': (2, 2)},
    {'name': 'medkit', 'position': (3, 3)}
]

# Inicializar el entorno con los agentes y objetos
env.init(agents, objects)

# Ejecutar algunas acciones
env.execute_action('robot', 'move', {'new_position': (1, 1)})
env.execute_action('human', 'pick', {'object': 'medkit'})

# Imprimir el estado actual del entorno para verificar las acciones
print(env.state)
