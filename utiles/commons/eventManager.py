import sys
sys.path.insert(0, '.')

from utiles.commons.event import Event

class EventManager:
    def __init__(self):
        self.event_queue = []
        self.agents = []

    def register_agent(self, agent) -> None:
        self.agents.append(agent)

    def unregister_agent(self, agent) -> None:
        self.agents.remove(agent)

    def add_event(self, event) -> None:
        self.event_queue.append(event)

    def dispatch_events(self, controller) -> None:
        while self.event_queue:
            event = self.event_queue.pop(0)
            for agent in controller.model.agents:
                if agent.name == event.destination_agent:
                    print("EventManager: Sending event {} to agent {}".format(event.event_type, agent.name))
                    agent.handle_event(event, controller)
