import sys
sys.path.insert(0, '.')

from src.mvc.observer import Observer
import time
import utiles.commons.vitalsGenerator as VG
import threading
from utiles.commons.eventManager import EventManager
from utiles.commons.event import Event


class Controller(Observer):

    abnormal_chance = 0
    abnormal_shift = 0

    def __init__(self, model, view, event_manager):
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
        self.default_agents = None

        self.event_manager = event_manager
        # Register agents with the event manager
        self.register_agents_with_event_manager()
        self.view.after(1000, self.update_events())  # Schedule event updates every 1000 milliseconds

    
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
                            #print("path: ", path)
                            #print(path)
                        self.move_randomly(path, value, path[0])


    def move_randomly(self, path, agent_index, previous):
        print(self.model.agents[agent_index].name, path)
        self.model.agents[agent_index].x = path[0][0]
        self.model.agents[agent_index].y = path[0][1]

        current_agent = self.model.agents[agent_index]

        self.model.notify(self.view, agents=self.model.agents)


        # Define offsets for adjacent and diagonal positions
        # (up, down, left, right, upper-left, upper-right, lower-left, lower-right)
        offsets = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        '''
        # Check each adjacent and diagonal position for a door
        for dx, dy in offsets:
            adjacent_y, adjacent_x = current_agent.x + dx, current_agent.y + dy
            # Ensure the position is within the bounds of the matrix if necessary
            if (0 <= adjacent_y < len(self.model.matrix) and
                0 <= adjacent_x < len(self.model.matrix[0])):
                if (self.model.matrix[adjacent_y][adjacent_x] != 0 and 
                    self.model.matrix[adjacent_y][adjacent_x]._literal_name == "Door"):
                    if self.model.matrix[adjacent_y][adjacent_x].isOpen == True:
                        self.model.matrix[adjacent_y][adjacent_x].close()
                        self.model.notify(self.view, matrix=self.model.matrix)
        '''
        #NO BORRAR AUN HASTA QUE SE COMPRUEBE QUE NO HAY BUGS EN LA VERSION NUEVA (ABAJO)


        # Check each adjacent and diagonal position for a door
        for dx, dy in offsets:
            adjacent_x, adjacent_y = current_agent.x + dx, current_agent.y + dy
            # Ensure the position is within the bounds of the matrix if necessary
            if (0 <= adjacent_y < len(self.model.matrix) and
                0 <= adjacent_x < len(self.model.matrix[0])):
                if ((self.model.matrix[adjacent_y][adjacent_x] != 0 and self.model.matrix[adjacent_y][adjacent_x] != 2) and 
                    self.model.matrix[adjacent_y][adjacent_x]._literal_name in ("Door", "Door_main")):
                    if self.model.matrix[adjacent_y][adjacent_x].isOpen == True:
                        self.model.matrix[adjacent_y][adjacent_x].close()
                        self.model.notify(self.view, matrix=self.model.matrix)


        if self.model.matrix[previous[1]][previous[0]] != 0 and\
              self.model.matrix[previous[1]][previous[0]]._literal_name in ("Door", "Door_main"):
            
            if self.model.matrix[previous[1]][previous[0]].isOpen == True:
                self.model.matrix[previous[1]][previous[0]].close()
                self.model.notify(self.view, matrix=self.model.matrix)
        
        if len(path) > 1:
            if self.model.matrix[path[1][1]][path[1][0]] != 0 and\
                  self.model.matrix[path[1][1]][path[1][0]]._literal_name in ("Door", "Door_main"):
                
                if self.model.matrix[path[1][1]][path[1][0]].isOpen == False:
                    self.model.matrix[path[1][1]][path[1][0]].open()
                    self.model.notify(self.view, matrix=self.model.matrix)

            # Schedule the next step in the animation
            self.animation_ids[agent_index] = self.view.after(
                self.animation_speed, self.move_randomly, path[1:], agent_index, path[0])
        else:
            if agent_index in self.animation_ids:
                del self.animation_ids[agent_index]
            if not self.animation_ids:
                self.animation_running = False


    def concrete_move(self, path, agent_index, previous):
        self.move_randomly(path, agent_index, previous)
        

    def add_agent(self, agent_name:str, x, y ) -> None:
        """
        Adds a new agent to the model and updates the view.

        Args:
            agent_name: The name of the agent to be added.
            position: The position to place the new agent.
        """
        ag = self.model.create_agent(agent_name, x, y)
        self.model.generate_agents(ag)
        
        self.model.notify(self.view, agents=self.model.agents)
    
    def add_object(self, object_instance, x, y ) -> None:
        """
        Adds a new object to the model and updates the view.

        Args:
            object_instance: The object to be added.
            position: The position to place the new object.
        """
        self.model.matrix[y][x] = object_instance
        self.model.notify(self.view, matrix=self.model.matrix)

    def despawn_object(self, x, y) -> None:
        """
        Removes an object from the model and updates the view.

        Args:
            position: The position of the object to be removed.
        """
        self.model.matrix[y][x] = 0
        self.model.notify(self.view, matrix=self.model.matrix)


    def remove_agent(self, agent_name:str) -> None:
        """
        Removes an agent from the model and updates the view.

        Args:
            agent_name: The name of the agent to be removed.
        """
        self.model.remove_agent(agent_name)
        self.view.update_view()


    
    def controller_generate_vital(self):
        while True:
            time.sleep(1)
            global abnormal_chance, abnormal_shift
            vital_constants = VG.generate_vital(self.abnormal_chance, self.abnormal_shift)
            self.model.agents[0].vitals_setter(vital_constants[0], vital_constants[1], vital_constants[2], vital_constants[3], vital_constants[4], vital_constants[5])
            
            self.model.notify(self.view, vitals=self.model.agents[0].vitals)
        
    # Create and start the thread
    def vital_threading(self):
        thread = threading.Thread(target=self.controller_generate_vital)
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
        def check_numeric_arguments(num_args, start_index_for_non_matching_args):
            
            assert len(command) == num_args, "Invalid number of arguments"
            for i in range(start_index_for_non_matching_args, num_args):
                assert command[i].isnumeric(), "Coordinates must be integers"

        command = command.strip().lower().replace("  ", " ").split(" ")

        match command[0]:
            
            case 'speed':
                assert command[1].isnumeric(), "Speed must be an integer"
                self.animation_speed = int(command[1])
                print(f"Animation speed set to {self.animation_speed}")

            case 'tp':
                # assert no hacer tp out of bounds
                check_numeric_arguments(5, 1)
                
                self.model.object_teleport(int(command[1]), int(command[2]), int(command[3]), int(command[4]))
                self.model.notify(self.view, matrix=self.model.matrix)

            case 'spawn':
                if self.default_agents == None:
                            self.default_agents = len(self.model.agents)

                match command[1]:
                    case 'agent':
                        command[1] = 'Gato' #FIXME harcodeado para qu no spawnee un agente sin sprite
                        self.spawn_agent(command, check_numeric_arguments)
                    case 'owner':
                        self.spawn_agent(command, check_numeric_arguments)
                    case 'enfermera':
                        self.spawn_agent(command, check_numeric_arguments)
                    case 'fridge':
                        self.spawn_object(command, check_numeric_arguments)
                    case 'table':
                        self.spawn_object(command, check_numeric_arguments)
                    case 'door':
                        self.spawn_object(command, check_numeric_arguments)
                    case 'sofa':
                        self.spawn_object(command, check_numeric_arguments)
                    case 'wall':
                        self.spawn_object(command, check_numeric_arguments)
                    case 'cama':
                        self.spawn_object(command, check_numeric_arguments)
                    case 'cama_g':
                        self.spawn_object(command, check_numeric_arguments)
                    case 'aramario':
                        self.spawn_object(command, check_numeric_arguments)
                    case 'juego_g':
                        self.spawn_object(command, check_numeric_arguments)
                    case 'juego':
                        self.spawn_object(command, check_numeric_arguments)
                    case 'silla1_g':
                        self.spawn_object(command, check_numeric_arguments)
                    case 'silla1':
                        self.spawn_object(command, check_numeric_arguments)
                    case 'silla2_g':
                        self.spawn_object(command, check_numeric_arguments)
                    case 'silla2':
                        self.spawn_object(command, check_numeric_arguments)
                    case 'silla_oficina':
                        self.spawn_object(command, check_numeric_arguments)
                    case 'silla_oficina_g':
                        self.spawn_object(command, check_numeric_arguments)
                    case 'planta1':
                        self.spawn_object(command, check_numeric_arguments)
                    case 'planta2':
                        self.spawn_object(command, check_numeric_arguments)
                    case 'planta3':
                        self.spawn_object(command, check_numeric_arguments)
                    case 'vater':
                        self.spawn_object(command, check_numeric_arguments)
                    case 'reset' | 'r':
                        assert len(command) == 2, "Invalid number of arguments"
                        
                        self.model.agents = self.model.agents[0:self.default_agents]
                        self.model.notify(self.view, agents=self.model.agents)

            case 'despawn' | 'des':
                check_numeric_arguments(3, 1)
                self.despawn_object(int(command[1]), int(command[2]))

            case 'delivery':
                check_numeric_arguments(3, 1)
                self.trigger_delivery(int(command[1]), int(command[2]))

    def spawn_agent(self, command, check_numeric_arguments):
        """
        Spawns a new agent with the given parameters.

        Args:
            command (list): The command containing the agent details.
            check_numeric_arguments (function): A function to check if the arguments are numeric.

        Returns:
            None
        """
        check_numeric_arguments(4, 2)          
        self.add_agent(command[1].capitalize(), int(command[2]), int(command[3]))

    def spawn_object(self, command, check_numeric_arguments):
            """
            Spawns a new object in the model based on the given command.

            Args:
                command (list): A list containing the command parameters.
                check_numeric_arguments (function): A function to check the numeric arguments.

            Returns:
                None
            """
            check_numeric_arguments(4, 2)
            ob = self.model.create_object(int(command[2]), int(command[3]), command[1].capitalize())           
            self.add_object(ob, int(command[2]), int(command[3]))

   

    def register_agents_with_event_manager(self):
        """
        Register all agents with the event manager.
        """
        for agent in self.model.agents:
            self.event_manager.register_agent(agent)


    def update_events(self):
        """
        Update method to dispatch events and schedule the next update.
        """
        self.event_manager.dispatch_events(self)
        self.view.after(1000, self.update_events)  # Schedule the next update


    """EJEMPLO DE COMO USAR EL EVENTO.
    def trigger_movement(self):
        # Determine the new position (this could come from various sources)
        new_position = (x, y)  # Replace with actual logic to determine the new position

        # Create a move event
        move_event = Event('move', new_position)

        # Add the event to the event manager's queue
        self.event_manager.add_event(move_event)

        # The event will be processed in due course by the event manager
    """




    def trigger_movement(self, x, y):
        # Determine the new position (this could come from various sources)
        new_position = (x, y)  # Replace with actual logic to determine the new position

        # Create a move event
        move_event = Event('Repartidor', 'move', new_position)

        # Add the event to the event manager's queue
        self.event_manager.add_event(move_event)

        # The event will be processed in due course by the event manager

    def trigger_delivery(self):
        # Determine the main door position (this could come from various sources)
        found = False
        # Iterate through each row and column in the matrix
        for i, row in enumerate(self.model.matrix):
            for j, element in enumerate(row):
                # Check if the element has the 'name' attribute
                if hasattr(element, 'name'):
                # Check if the 'name' attribute matches the target name
                    if element.name == "Main_Door":
                        # Return the position of the element
                        main_door_position = (i, j)
                        found = True
                        break
            if found:
                break

        delivery_event = Event('Repartidor', 'delivery', main_door_position)
        self.event_manager.add_event(delivery_event)