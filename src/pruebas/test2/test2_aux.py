class Agent:
    def __init__(self, name, position=(0,0)):
        self.name = name
        self.position = position
        self.inventory = []

class Object:
    def __init__(self, name, position=(0,0)):
        self.name = name
        self.position = position

class Environment:
    def __init__(self):
        self.agents = {}
        self.objects = {}

    def add_agent(self, agent):
        self.agents[agent.name] = agent

    def add_object(self, obj):
        self.objects[obj.name] = obj

    def move_agent(self, agent_name, new_position):
        if agent_name in self.agents:
            self.agents[agent_name].position = new_position
            return True
        return False

    def agent_pick_object(self, agent_name, object_name):
        if agent_name in self.agents and object_name in self.objects:
            agent = self.agents[agent_name]
            obj = self.objects[object_name]
            if agent.position == obj.position:
                agent.inventory.append(obj)
                del self.objects[object_name]
                return True
        return False

    def update_percepts(self):
        for agent_name, agent in self.agents.items():
            # Reset agent's percepts
            agent.percepts = []
            # Check for objects at agent's position
            for obj in self.objects.values():
                if obj.position == agent.position:
                    agent.percepts.append(f"Object {obj.name} is at {obj.position}")

# Example usage
env = Environment()
robot = Agent('robot', position=(1, 1))
env.add_agent(robot)

beer = Object('beer', position=(2, 2))
env.add_object(beer)

# Robot moves towards the beer
env.move_agent('robot', (2, 2))

# Robot picks up the beer
env.agent_pick_object('robot', 'beer')

# Update percepts after actions
env.update_percepts()

# Display the updated state
for agent in env.agents.values():
    print(f"Agent {agent.name} is at {agent.position} with inventory: {agent.inventory}")
