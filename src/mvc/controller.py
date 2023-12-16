import sys
sys.path.insert(0, '.')

from src.mvc.observer import Observer
import time
import random
import utiles.commons.vitalsGenerator as VG
import threading


class Controller(Observer):
    def __init__(self, model, view):
        self.model = model
        self.view = view
        
        self.view.set_controller(self)
        self.model.attach(self.view)
        self.model.attach(self)
        

        self.animation_running = False
        self.animation_ids = {}
        self.animation_id = None
        self.previous_event = None
        self.animation_speed = 800
    
    def updateFromNotification(self, *new_state, **kwargs):
        NOTIFY_KEYS = ('agent_move_right', 'random_movement')
        path=False
        print(kwargs)
        for key, value in kwargs.items():
            if key not in NOTIFY_KEYS:
                raise KeyError(f"Invalid key: {key}")
            else:        
                match key:
                    case 'agent_move_right':
                        self.model.agent_move_right(value)
                    case 'random_movement':
                    # random movement necesita el indice del agente (del que luego se saca su posicion)
                    # value es una tupla con indices de agentes
                        while path == False or path == None or path == []: #No hay camino / el destino no es valido / Origen == Destino
                            path = self.model.path_generator(value)
                            print(path)
                        self.move_randomly(path, value, path[0])


    def move_randomly(self, path, agent_index, previous):
        print(self.model.agents[agent_index].name, path)
        self.model.agents[agent_index].y = path[0][0]
        self.model.agents[agent_index].x = path[0][1]

        current_agent = self.model.agents[agent_index]

        self.model.notify(self.view, agents=self.model.agents)


        # Define offsets for adjacent and diagonal positions
        # (up, down, left, right, upper-left, upper-right, lower-left, lower-right)
        offsets = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

        # Check each adjacent and diagonal position for a door
        for dy, dx in offsets:
            adjacent_y, adjacent_x = current_agent.y + dy, current_agent.x + dx
            # Ensure the position is within the bounds of the matrix if necessary
            if (0 <= adjacent_y < len(self.model.matrix) and
                0 <= adjacent_x < len(self.model.matrix[0])):
                if (self.model.matrix[adjacent_y][adjacent_x] != 0 and 
                    self.model.matrix[adjacent_y][adjacent_x]._literal_name == "Door"):
                    if self.model.matrix[adjacent_y][adjacent_x].isOpen == True:
                        self.model.matrix[adjacent_y][adjacent_x].close()
                        self.model.notify(self.view, matrix=self.model.matrix)

        if self.model.matrix[previous[0]][previous[1]] != 0 and\
              self.model.matrix[previous[0]][previous[1]]._literal_name == "Door":
            
            if self.model.matrix[previous[0]][previous[1]].isOpen == True:
                self.model.matrix[previous[0]][previous[1]].close()
                self.model.notify(self.view, matrix=self.model.matrix)
        
        if len(path) > 1:
            if self.model.matrix[path[1][0]][path[1][1]] != 0 and\
                  self.model.matrix[path[1][0]][path[1][1]]._literal_name == "Door":
                
                if self.model.matrix[path[1][0]][path[1][1]].isOpen == False:
                    self.model.matrix[path[1][0]][path[1][1]].open()
                    self.model.notify(self.view, matrix=self.model.matrix)

            # Schedule the next step in the animation
            self.animation_ids[agent_index] = self.view.after(
                self.animation_speed, self.move_randomly, path[1:], agent_index, path[0])
        else:
            if agent_index in self.animation_ids:
                del self.animation_ids[agent_index]
            if not self.animation_ids:
                self.animation_running = False
        

    def add_agent(self, agent_name:str, position:tuple) -> None:
        """
        Adds a new agent to the model and updates the view.

        Args:
            agent_name: The name of the agent to be added.
            position: The position to place the new agent.
        """
        new_agent = self.model.generate_agents(agent_name, position)
        self.model.add_agent(new_agent)
        self.view.update_view()


    def remove_agent(self, agent_name:str) -> None:
        """
        Removes an agent from the model and updates the view.

        Args:
            agent_name: The name of the agent to be removed.
        """
        self.model.remove_agent(agent_name)
        self.view.update_view()


    
    def generate_vital(self):
        while True:
            time.sleep(1)
            vital_constants = VG.generate_vital()
            self.model.agents[0].vitals_setter(vital_constants[0], vital_constants[1], vital_constants[2], vital_constants[3], vital_constants[4], vital_constants[5])
            self.model.notify(self.view, vitals=self.model.agents[0].vitals)
        
    # Create and start the thread
    def vital_threading(self):
        thread = threading.Thread(target=self.generate_vital)
        thread.daemon = True  # This makes the thread exit when the main program exits
        thread.start()     

    def handle_click(self, event, *args):
        """
        Handles the click event and initiates the corresponding animation based on the event type.

        Parameters:
        - event (str): The type of event triggered by the click.

        Returns:
        None
        """

        # Cancel all running animations
        if self.animation_running:
            print("Stopping all current animations")
            for agent_index, anim_id in self.animation_ids.items():
                try:
                    self.view.after_cancel(anim_id)
                except ValueError:
                    print(f"Animation for agent {agent_index} was invalid or already cancelled")
            
            self.animation_ids.clear()  # Clear all animation identifiers
            self.animation_running = False
            if event == self.previous_event:
                return

        self.previous_event = event
        
        match event:
            case "movement":
                print("\n/////////////// TEST START ///////////////")
                for index in range(len(self.model.agents)):
                    # Check if a movement animation is already running for this agent
                    if index in self.animation_ids and event in self.animation_ids[index]:
                        print(f"Movement animation is already running for agent {index}.")
                    else:
                        # Start a new movement animation for this agent
                        self.updateFromNotification(random_movement=index)
                        # The logic in updateFromNotification should handle setting up the animation_id
                        self.animation_running = True

    def parse_command(self, command:str):
        """
        Parses the command string and returns the corresponding command.

        Parameters:
        - command (str): The command string to be parsed.

        Returns:
        The command to be executed.
        """

        command = command.strip().lower().split(" ")

        match command[0]:
            case 'speed':
                assert command[1].isnumeric(), "Speed must be an integer"
                self.animation_speed = int(command[1])
                print(f"Animation speed set to {self.animation_speed}")

            case 'tp':
                # assert no hacer tp out of bounds
                assert len(command) == 5, "Invalid number of arguments"
                for i in range(1, 5):
                    assert command[i].isnumeric(), "Coordinates must be integers"
                
                self.model.object_teleport(int(command[1]), int(command[2]), int(command[3]), int(command[4]))
                self.model.notify(self.view, matrix=self.model.matrix)
        

   





