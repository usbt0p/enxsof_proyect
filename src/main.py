import sys
sys.path.insert(0, '.')

from src.mvc import (model, view, controller)
from utiles.agents import (owner, nurse, agent)
import unittest

# Define constants for matrix size and window size
X_SIZE, Y_SIZE = 16, 16
activate_superspeed = False

height = 40 * X_SIZE
width = 40 * Y_SIZE

# Create the model and specify the size of the room and its configuration file
room = model.Model(X_SIZE, Y_SIZE)
file_path = 'assets/default_{}x{}_room.json'.format(X_SIZE, Y_SIZE)
room.populate_room(file_path)

# Create an agent and add it to the room
propietario = owner.Owner("Owner", 7, 7)
nurse1 = nurse.Nurse("Enfermera", 13, 13, 5, 5)
nurse2 = nurse.Nurse("Enfermera 2", 3, 11, 6, 6)
gato = agent.Agent("Gato", 11, 3)
room.agents_random_spawn(propietario, nurse1, nurse2, gato)

# Create a view
view = view.View('view', height, width)

# Initalize controller and start vital constants thread
main_controller = controller.Controller(room, view)
if activate_superspeed:
    main_controller.animation_speed = 50
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
    