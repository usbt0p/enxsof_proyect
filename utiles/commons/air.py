from utiles.commons.thing import Thing

class Air(Thing):
    def __init__(self, x, y, literal_name="Air", interactive=False, collision=False):
        super().__init__(x, y, literal_name, interactive, collision)      