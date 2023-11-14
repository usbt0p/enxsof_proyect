class Environment:
    def __init__(self):
        self.state = {
            'agents': {},
            'objects': {}
        }

    def init(self, agents, objects):
        for agent in agents:
            self.state['agents'][agent['name']] = {
                'position': list(agent['position']),  # Almacenar como lista para permitir actualizaciones
                'percepts': [],
                'inventory': []
            }
        for obj in objects:
            self.state['objects'][obj['name']] = list(obj['position'])  # Almacenar como lista

    def add_percept(self, agent_name, percept):
        if agent_name in self.state['agents']:
            self.state['agents'][agent_name]['percepts'].append(percept)

    def remove_percept(self, agent_name, percept):
        if agent_name in self.state['agents']:
            self.state['agents'][agent_name]['percepts'].remove(percept)

    def clear_percepts(self, agent_name=None):
        if agent_name:
            self.state['agents'][agent_name]['percepts'] = []
        else:
            for agent in self.state['agents'].values():
                agent['percepts'] = []

    def get_percepts(self, agent_name):
        return self.state['agents'][agent_name]['percepts']

    def execute_action(self, agent_name, action, params):
        if action == 'move':
            new_position = params['new_position']
            self.state['agents'][agent_name]['position'] = new_position
            return True
        elif action == 'pick':
            object_name = params['object']
            agent_position = self.state['agents'][agent_name]['position']
            object_position = self.state['objects'].get(object_name)
            if object_position and agent_position == object_position:
                self.state['agents'][agent_name]['inventory'].append(object_name)
                del self.state['objects'][object_name]
                return True
        return False

# Ejemplo de cómo inicializar y usar la clase Environment:
env = Environment()

# Supongamos que tenemos dos agentes y dos objetos en el entorno
agents = [
    {'name': 'robot', 'position': (0, 0)},
    {'name': 'human', 'position': (4, 4)}
]
objects = [
    {'name': 'beer', 'position': (2, 2)},
    {'name': 'medkit', 'position': (3, 3)}
]

# Inicializar el entorno con los agentes y objetos
env.init(agents, objects)

# Ejecutar algunas acciones
env.execute_action('robot', 'move', {'new_position': [1, 1]})
env.execute_action('human', 'pick', {'object': 'medkit'})

# Imprimir el estado actual del entorno para verificar las acciones
print(env.state)

