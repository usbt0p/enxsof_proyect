import sys
sys.path.insert(0, '.')

from src.mvc.observer import Observer
import time
import random


class Controller(Observer):
    def __init__(self, model, view):
        self.model = model
        self.view = view
        
        self.view.set_controller(self)
        self.model.attach(self)
        self.model.attach(self.view)

        self.animation_running = False
        self.animation_id = None
        self.previous_event = None
    
    
    def update_observer(self, *new_state):
        """
        Update the observer with the new state and schedule the view to be updated.

        Args:
            *new_state: Variable number of arguments representing the new state.

        Returns:
            None
        """
        self.view.after(0, self.view.update_view)


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

        

    def move_agent(self, agent, new_position) -> None:
        """
        Moves an agent to a new position and updates the view.

        Args:
            agent_name: The name of the agent to be moved.
            new_position: The new position to move the agent to.
        """
        agent.position(new_position)

    # Test function for agent movement, not part of the final product
    def animate_movement(self, agent, movements, index=0):
        """
        Animates the movement of an agent based on a list of positions.

        Args:
            agent (Agent): The agent to animate.
            movements (list): A list of positions representing the movements.
            index (int, optional): The current index in the movements list. Defaults to 0.
        """
        agent.x = 7
        agent.y = 7
        if index < len(movements):
            pos = movements[index]
            self.move_agent(agent, pos)
            self.view.update_view()

        if index >= len(movements):
            print("\n/////////////// TEST END ///////////////")
            self.animation_running = False
            return
            # Programa el siguiente movimiento después de un segundo
        self.animation_id = self.view.after(1000, lambda: self.animate_movement(agent, movements, index + 1))

    # Test function for agent movement, not part of the final product
    def animate_movement_collision(self, agent, movements, index=0):
        """
        Animates the movement of the agent and checks for collisions with objects in the model.

        Args:
            agent (Agent): The agent object to be moved.
            movements (list): A list of positions representing the movements to be animated.
            index (int, optional): The current index of the movements list. Defaults to 0.
        """
        agent.x = 7
        agent.y = 7
        if index < len(movements):
            pos = movements[index]
            eval_object = self.model.is_position_occupied(pos)
            # If the new position is occupied, stop the animation
            if ((not eval_object.interactive) and eval_object.movable and eval_object.literal_name != "Air"):
                print("\nI can maybe try to move this obstacle... but I'm not sure if I can do it alone, I'm just a cat!")
                print("\n/////////////// TEST END ///////////////")
                return
            elif ((eval_object.interactive) and (eval_object.movable)):
                print("\nI like to jump on the sofa or the fridge!\n")
            elif ((eval_object.collision) and not (eval_object.movable)):
                print("\nOoops! It looks like there is an obstacle in the way!\n")
                print("\n/////////////// TEST END ///////////////")
                return

            self.move_agent(agent, pos)
            self.view.update_view()

            if index >= len(movements):
                print("\n/////////////// TEST END ///////////////")
                self.animation_running = False
                return
        
            # Programa el siguiente movimiento después de un segundo
            self.animation_id = self.view.after(1000, lambda: self.animate_movement_collision(agent, movements, index + 1))

    # Test function for agent movement, not part of the final product
    def animate_movement_door(self, agent, movements, index=0):
        """
        Animates the movement of the agent and interacts with doors along the way.

        Args:
            agent (Agent): The agent object.
            movements (list): List of positions representing the agent's movements.
            index (int, optional): The current index in the movements list. Defaults to 0.
        """
        agent.x = 5
        agent.y = 3

        if index < len(movements):
            pos = movements[index]

            eval_object = self.model.is_position_occupied(pos)


            if eval_object.literal_name == "Door":
                print("\nIs the door open? ", eval_object.isOpen)
                time.sleep(3)

                if not(eval_object.isOpen):
                    eval_object.open()
                    print("\nI'm opening the door\n")
                    time.sleep(2)

                elif eval_object.isOpen:
                    eval_object.close()
                    print("\nI'm closing the door\n")
                    time.sleep(2)

            self.move_agent(agent, pos)
            self.view.update_view()

            if index >= len(movements):
                print("\n/////////////// TEST END ///////////////")
                self.animation_running = False
                return

            # Programa el siguiente movimiento después de un segundo
            self.animation_id = self.view.after(1000, lambda: self.animate_movement_door(agent, movements, index + 1))
       
    def handle_click(self, event):
        """
        Handles the click event and initiates the corresponding animation based on the event type.

        Parameters:
        - event (str): The type of event triggered by the click.

        Returns:
        None
        """
        if self.animation_running:
            print("Stopping current animation")
            try:
                self.view.after_cancel(self.animation_id)
            except ProcessLookupError:
                print("Animation crashed or already stopped")
            self.animation_running = False
            if event == self.previous_event:
                return

        self.previous_event = event
        
        print("\n/////////////// TEST START ///////////////")
        if event == "movement":
            self.animation_running = True
            self.animation_id = self.test_movement(self.model.agents[0])
        elif event == "collision":
            self.animation_running = True
            self.animation_id = self.test_collision(self.model.agents[0])
        elif event == "door":
            self.animation_running = True
            self.animation_id = self.test_door(self.model.agents[0])

    # Test function for agent movement, not part of the final product
    def test_movement(self, agent):
        movements = [[[7,7],[7,6],[7,5],[7,4],[8,4],[9,4],[9,3],[10,3],[11,2],[12,1],[12,3],[12,4],[14,4],[15,5]],
        [[7,7],[5,7],[3,7],[3,8],[3,9],[4,10],[5,10],[6,10],[5,11],[4,13],[4,14],[5,13],[6,12],[8,12],[9,12],[10,12],[12,11]],
        [[7,7],[5,7],[2,7],[2,6],[2,5],[2,4],[2,3],[3,2],[2,2],[1,4],[2,5],[2,6],[2,8],[3,9],[3,11],[2,12],[1,13],[3,13]],
        [[7,7],[9,8],[9,10],[9,12],[10,12],[11,12],[11,11],[11,10],[12,9],[12,8],[12,7],[12,6],[12,5],[11,4],[11,3],[10,3],[9,2],[8,1],[8,0]]]
    
        random_index = random.randint(0, len(movements) - 1)

    # Inicia la animación después de un segundo
        self.view.after(1000, lambda: self.animate_movement(agent, movements[random_index]))

        
    # Test function for agent movement, not part of the final product
    def test_collision(self, agent):
        movements = [[[7,7],[7,6],[7,5],[7,4],[8,4],[9,4],[9,3],[10,3],[11,2],[12,1],[12,3],[12,4],[14,4],[15,5]],
        [[7,7],[5,7],[3,7],[3,8],[3,9],[4,10],[5,10],[6,10],[5,11],[4,13],[4,14],[5,13],[6,12],[8,12],[9,12],[10,12],[12,11]],
        [[7,7],[5,7],[2,7],[2,6],[2,5],[2,4],[2,3],[3,2],[2,2],[1,4],[2,5],[2,6],[2,8],[3,9],[3,11],[2,12],[1,13],[3,13]],
        [[7,7],[9,8],[9,10],[9,12],[10,12],[11,12],[11,11],[11,10],[12,9],[12,8],[12,7],[12,6],[12,5],[11,4],[11,3],[10,3],[9,2],[8,1],[8,0]]]
    
        random_index = random.randint(0, len(movements) - 1)
    
    # Inicia la animación después de un segundo
        self.view.after(1000, lambda: self.animate_movement_collision(agent, movements[random_index]))


    # Test function for agent movement, not part of the final product
    def test_door(self, agent):
        self.model.matrix[9][3].open()
        movements = [[5,3],[6,3],[7,3],[8,3],[9,3],[10,3],[11,3],[12,3],[13,3],[14,3],[13,3],[12,3],[11,3],[10,3],[9,3],[8,3],[7,3],[6,3],[5,3],
                     [5,4],[5,5],[5,6],[5,7],[5,8],[4,8],[3,8],[3,9],[3,10],[3,11]]
    # Inicia la animación después de un segundo
        self.view.after(1000, lambda: self.animate_movement_door(agent, movements))





