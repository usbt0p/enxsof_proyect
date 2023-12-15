import sys
sys.path.insert(0, '.')

from abc import ABC
from copy import deepcopy
import random
import heapq

class Movements(ABC):
    
    def is_position_occupied(self, x, y) -> bool:
        """
        Checks if a position is occupied by an object.
        Parameters:
        - position (tuple): The position to check.
        Returns:
        - bool: True if the position is occupied, False otherwise.
        """
        return self.matrix[y][x] != 0
    
    def object_teleport(self, origin_x, origin_y, new_position_x, new_position_y) -> None:
        """
        Moves an object to a new position.
        Parameters:
        - origin (tuple): The position of the object to move.
        - new_position (tuple): The new position of the object.        
        Returns:
        None
        """
        if not self.is_position_occupied(new_position_x, new_position_y):
            new = deepcopy(self.matrix[origin_y][origin_x])
            new.x = new_position_x # Asegura que las coordenadas del objeto se actualizan cuando se mueve
            new.y = new_position_y
            self.matrix[new_position_y][new_position_x] = new
            self.matrix[origin_y][origin_x] = 0
        


class pathPlanning(ABC):
    @staticmethod
    def generate_random_position(max_x, max_y):
        """Generate a random position within the given boundaries."""
        new_x = random.randint(0, max_x)
        new_y = random.randint(0, max_y)
        print("random position: ", new_x, new_y)
        return new_x, new_y

    
    def is_valid_position(self, x, y, max_x, max_y):
        """Check if the position is valid (within boundaries and not occupied)."""
        # Check boundaries
        if (x < 0 or x >= max_x) or (y < 0 or y >= max_y):
            return False
        # Check if position is occupied (assuming is_position_occupied is defined)
        return not self.is_position_occupied(x, y)
    
    

    def calculate_random_path(self, agent_x, agent_y, max_x, max_y):
        """Move the agent to a valid random position."""
        new_x, new_y = self.generate_random_position(max_x, max_y)
        if self.is_valid_position(new_x, new_y, max_x, max_y):
            return self.a_star_search((agent_x,agent_y),(new_x, new_y), self.matrix) 
        else:
            # Optionally, try again or handle invalid move
            print("There is no valid position to move to!")


    def path_generator(self, agent_index):
        origin_x = self.agents[agent_index].y # Por tema de matriz transpuesta, esto va al reves
        origin_y = self.agents[agent_index].x # Por tema de matriz transpuesta, esto va al reves
        return self.calculate_random_path(origin_x, origin_y, self.x_size, self.y_size)
        
    # Simplified version of path finding
    """
    def find_path(start, end, matrix):
        path = []
        x, y = start
        target_x, target_y = end

        # Move horizontally until aligned with the target on x-axis
        while x != target_x:
            if matrix[y][x] == 0:  # Assuming 0 represents a free space
                path.append((x, y))
                x += 1 if target_x > x else -1
            else:  # Obstacle encountered
                break

        # Move vertically until aligned with the target on y-axis
        while y != target_y:
            if matrix[y][x] == 0:
                path.append((x, y))
                y += 1 if target_y > y else -1
            else:  # Obstacle encountered
                break

        return path
        """
    
    @staticmethod
    def heuristic(a, b):
            """
            Calculate the heuristic value for A* pathfinding.

            This function computes the Manhattan distance between two points, 
            which is used as a heuristic in the A* algorithm. The Manhattan distance 
            is the sum of the absolute differences of their Cartesian coordinates. 
            It is a suitable heuristic for grid-based pathfinding where only 
            4-directional movement is allowed (up, down, left, right).

            Args:
                a (tuple): The current node position as a tuple (x, y).
                b (tuple): The goal node position as a tuple (x, y).

            Returns:
                int: The Manhattan distance between the current node and the goal node.
            """

            # Calculate and return the Manhattan distance.
            # Manhattan distance is the sum of the horizontal and vertical distances.
          
            manhattan = abs(a[0] - b[0]) + abs(a[1] - b[1])
            
            return manhattan


    def a_star_search(self, start, goal, grid):
        """
        Perform A* search algorithm to find the shortest path from the start node to the goal node on a grid.

        Args:
            start (tuple): The starting node position as a tuple (x, y).
            goal (tuple): The goal node position as a tuple (x, y).
            grid (list): The grid representing the environment, where 0 represents an obstacle and any other value represents a valid node.

        Returns:
            list or bool: The path from the start node to the goal node as a list of node positions (tuples), or False if no path is found.
        """

        # Initialize the neighbors for 4-directional movement on the grid.
        # Each tuple represents a relative movement direction (up, right, down, left).
        neighbors = [(0, -1), (1, 0), (0, 1), (-1, 0)]

        # Initialize sets and dictionaries for managing nodes during search.
        close_set = set()  # Set to keep track of nodes that have already been evaluated.
        came_from = {}  # Dictionary to store the parent node of each visited node.
        gscore = {start: 0}  # Dictionary to store the cost of the cheapest path from start to each node.
        fscore = {start: self.heuristic(start, goal)}  # Dictionary to store the estimated total cost from start to goal through each node.

        # Initialize a priority queue (min-heap) to manage nodes to be visited, starting with the start node.
        open_heap = []
        heapq.heappush(open_heap, (fscore[start], start))

        # Main loop of the A* algorithm.
        while open_heap:
            # Pop the node with the lowest f-score from the priority queue.
            current = heapq.heappop(open_heap)[1]

            # Check if the current node is the goal. If so, reconstruct and return the path found.
            if current == goal:
                path = []
                while current in came_from:
                    path.append(current)
                    current = came_from[current]
                return path[::-1]  # Return the path in correct order, from start to goal.

            # Add the current node to the set of evaluated nodes.
            close_set.add(current)

            # Evaluate all neighboring nodes of the current node.
            for i, j in neighbors:
                # Calculate the position of the neighbor node.
                neighbor = current[0] + i, current[1] + j

                # Calculate the tentative g-score of the neighbor node.
                tentative_g_score = gscore[current] + self.heuristic(current, neighbor)

                # Check if the neighbor node is within the grid boundaries and not an obstacle.
                
                if (((0 <= neighbor[0]) and (neighbor[0] < len(grid))) and ((0 <= neighbor[1]) and (neighbor[1] < len(grid[0])))):
                    if ((grid[neighbor[0]][neighbor[1]] != 0) and (grid[neighbor[0]][neighbor[1]]._literal_name != "Door")):  # '0' represents NOT an obstacle.
                        continue

                # Skip the neighbor node if it has already been evaluated with a lower g-score.
                if neighbor in close_set and tentative_g_score >= gscore.get(neighbor, 0):
                    continue

                # If this path to the neighbor node is better, update its scores and parent node.
                if tentative_g_score < gscore.get(neighbor, 0) or neighbor not in [i[1]for i in open_heap]:
                    came_from[neighbor] = current
                    gscore[neighbor] = tentative_g_score
                    fscore[neighbor] = tentative_g_score + self.heuristic(neighbor, goal)
                    heapq.heappush(open_heap, (fscore[neighbor], neighbor))

        # Return False if no path is found from the start to the goal.
        return False





