import sys
sys.path.insert(0, '.')

class Event:
    def __init__(self, destination_agent, event_type, data=None):
        self.destination_agent = destination_agent
        self.event_type = event_type
        self.data = data  # This could be coordinates for a move, etc.
