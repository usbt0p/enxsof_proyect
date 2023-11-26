import sys
sys.path.insert(0, '.')

import threading
import tkinter as tk
import src.mvc.model as model
import src.mvc.view as view
from src.mvc.observer import Observer


class Controller(Observer):
    def __init__(self, model, view):
        self.model = model
        self.view = view
        
        self.view.set_controller(self)
        self.model.attach(self)
        self.model.attach(self.view)
        print("test")

        # Start a thread for handling terminal inputs
        threading.Thread(target=self.handle_terminal_input, daemon=True).start()

    def handle_terminal_input(self):
        while True:
            user_input = input("Enter commands as requested: ")
            # Process the input and update model or view
            self.process_input(user_input)

    def process_input(self, user_input):
        # Implement logic based on input
        if user_input == 'open door':
            # Example: Update model and view
            self.model.open_door()  # Assuming this method exists in the model
            # Schedule a GUI update in the main thread
            self.view.after(0, self.view.update_view)  # Assuming update_view method in view
    
    def update(self, message):
        pass

    # Other controller methods to interact with model and view
    # ...

# Usage example (ensure that model and view are correctly instantiated)


# Start the Tkinter main loop (if this is the entry point of your application)
