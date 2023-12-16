import sys
sys.path.insert(0, '.')

from src.mvc import (model, view, controller)
from utiles.agents import owner
import unittest

# Define constants for matrix size and window size
X_SIZE = 16
Y_SIZE = 16

height = 40 * X_SIZE
width = 40 * Y_SIZE

# Create the model and specify the size of the room and its configuration file
room = model.Model(X_SIZE, Y_SIZE)
file_path = 'assets/default_16x16_room.json'
room.populate_room(file_path)

# Create an agent and add it to the room
propietario = owner.Owner("Owner", 7, 7)
nurse = owner.Owner("Enfermera", 13, 13)
nurse2 = owner.Owner("Enfermera 2", 3, 11)
gato = owner.Owner("Gato", 11, 3)
room.generate_agents(propietario, nurse, nurse2, gato)

# Create a view
view = view.View('view', height, width)

# Initalize controller and start vital constants thread
main_controller = controller.Controller(room, view)
main_controller.vital_threading()

# Send initial state to the view
room.notify(view, agents=room.agents, matrix=room.matrix)

# Start the main event loop
view.mainloop()




if __name__ == "__main__":

    print('HAY QUE HACER LOS PUTOS TESTS AQUI!!!!!!!!!!!\n\
          HAY QUE HACER LOS PUTOS TESTS AQUI!!!!!!!!!!!\n\
          HAY QUE HACER LOS PUTOS TESTS AQUI!!!!!!!!!!!\n\
          HAY QUE HACER LOS PUTOS TESTS AQUI!!!!!!!!!!!\n')
    