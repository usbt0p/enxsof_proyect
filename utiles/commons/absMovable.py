import sys
sys.path.insert(0, '.')

from abc import ABC, abstractmethod
import random
import heapq

class AbstractMovable(ABC):
    """Abstract class for movable objects."""
    
    def move_up(self):
        assert self.y > 0, "You can't move there!"
        self.y -= 1

    def move_down(self):
        #TODO cambiar esto para cuando esté el mapa
        #assert self.y < len(self.grid) - 1, "You can't move there!"
        self.y += 1

    def move_left(self):
        assert self.x > 0, "You can't move there!"
        self.x -= 1

    def move_right(self):
        #TODO cambiar esto para cuando esté el mapa
        # assert self.x < len(self.grid[0]) - 1, "You can't move there!"
        self.x += 1



    def generate_random_position(self, max_x, max_y):
        """Generate a random position within the given boundaries."""
        new_x = random.randint(0, max_x - 1)
        new_y = random.randint(0, max_y - 1)
        return new_x, new_y

    def is_valid_position(self, x, y, max_x, max_y):
        """Check if the position is valid (within boundaries and not occupied)."""
        # Check boundaries
        if x < 0 or x >= max_x or y < 0 or y >= max_y:
            return False
        # Check if position is occupied (assuming is_position_occupied is defined)
        return not is_position_occupied(x, y)
    
    def move_randomly(self, max_x, max_y):
        """Move the agent to a valid random position."""
        new_x, new_y = self.generate_random_position(max_x, max_y)
        if self.is_valid_position(new_x, new_y, max_x, max_y):
            self.position((new_x, new_y))
        else:
            # Optionally, try again or handle invalid move
            pass

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
    
    def heuristic(self, a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    
    def a_star_search(self, start, goal, grid):
        neighbors = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 4-directional movement
        close_set = set()
        came_from = {}
        gscore = {start: 0}
        fscore = {start: self.heuristic(start, goal)}
        open_heap = []

        

        heapq.heappush(open_heap, (fscore[start], start))
        
        while open_heap:
            current = heapq.heappop(open_heap)[1]

            if current == goal:
                path = []
                while current in came_from:
                    path.append(current)
                    current = came_from[current]
                return path[::-1]

            close_set.add(current)
            for i, j in neighbors:
                neighbor = current[0] + i, current[1] + j            
                tentative_g_score = gscore[current] + self.heuristic(current, neighbor)
                if 0 <= neighbor[0] < len(grid) and 0 <= neighbor[1] < len(grid[0]):
                    if grid[neighbor[0]][neighbor[1]] == 1:  # Assuming 1 is an obstacle
                        continue
                if neighbor in close_set and tentative_g_score >= gscore.get(neighbor, 0):
                    continue
                    
                if tentative_g_score < gscore.get(neighbor, 0) or neighbor not in [i[1]for i in open_heap]:
                    came_from[neighbor] = current
                    gscore[neighbor] = tentative_g_score
                    fscore[neighbor] = tentative_g_score + self.heuristic(neighbor, goal)
                    heapq.heappush(open_heap, (fscore[neighbor], neighbor))
        
        return False  # No path found