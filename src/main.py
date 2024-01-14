import sys
sys.path.insert(0, '.')

from src.mvc import (model, view, controller)
from utiles.agents import (owner, nurse, agent, waiter, delivery)

from utiles.commons.eventManager import EventManager

def create_menu():
    """Creates a menu that asks for the size of the room."""

    print("Choose a map to load!")
    print("1. x = 16, y = 16")
    print("2. x = 10, y = 10")
    print("3. x = 16, y = 10")
    print("4. x = 24, y = 18")
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        x, y = 16, 16
    elif choice == "2":
        x, y = 10, 10
    elif choice == "3":
        x, y = 16, 10
    elif choice == "4":
        x, y = 24, 18
    else:
        print("Invalid choice. Using default values 16x16.")
        x, y = 16, 16

    return x, y

# Create a menu that asks for the size of the room
X_SIZE, Y_SIZE = create_menu()

# Define constants
height = Y_SIZE * 40
width = X_SIZE * 40

# Create the model and specify the size of the room and its configuration file
room = model.Model(X_SIZE, Y_SIZE)
file_path = 'assets/default_{}x{}_room.json'.format(X_SIZE, Y_SIZE)
room.populate_room(file_path)

# Create an agent and add it to the room
propietario = owner.Owner("Owner", 7, 7)
nurse1 = nurse.Nurse("Enfermera", 13, 13, 5, 5)
nurse2 = nurse.Nurse("Enfermera 2", 3, 11, 6, 6)
gato = agent.Agent("Gato", 11, 3)
auxiliar = waiter.Waiter("Auxiliar", 11, 7)
#repartidor = delivery.Delivery("Repartidor", 11, 11)
room.agents_random_spawn(propietario, nurse1, nurse2, gato, auxiliar)



event_manager = EventManager()


# Create a view
view = view.View('view', height, width)

# Initalize controller and start vital constants thread
main_controller = controller.Controller(room, view, event_manager)
main_controller.vital_threading()


# Send initial state to the view
room.notify(view, agents=room.agents, matrix=room.matrix)

# Start the main event loop
view.mainloop()

    
    