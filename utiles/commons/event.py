import sys
sys.path.insert(0, '.')

class Event:
    def __init__(self, event_type, data):
        self.event_type = event_type
        self.data = data  # This could be coordinates for a move, etc.
