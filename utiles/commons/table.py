from utiles.commons.obstacle import Obstacle

class Table(Obstacle):
    def __init__(self, x, y, literal_name="Table", interactive=False, collision=True):
        super().__init__(x, y, literal_name, interactive, collision)