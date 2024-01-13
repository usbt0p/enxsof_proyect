import sys
sys.path.insert(0, '.')

from utiles.commons.event import Event

class EventManager:
    def __init__(self):
        self.event_queue = []
        self.agents = []

    def register_agent(self, agent):
        self.agents.append(agent)

    def unregister_agent(self, agent):
        self.agents.remove(agent)

    def add_event(self, event):
        self.event_queue.append(event)

    def dispatch_events(self, model):
        while self.event_queue:
            event = self.event_queue.pop(0)
            for agent in self.agents:
                
                if agent.name == event.destination_agent:
                    print(agent)
                    print('hey')
                    agent.handle_event(event, model)
