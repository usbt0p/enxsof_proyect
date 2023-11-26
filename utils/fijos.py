"""
import unittest

class Thing():
    def __init__(self, x, y, element_name, position_change, manipulation):
        self.x = x
        self.y = y
        self.element_name = element_name
        self.position_change = position_change
        self.manipulation = manipulation
    
    @property
    def element_name(self):
        return self.element_name

    @element_name.setter
    def element_name(self, value):
        self.element_name = value

    @property
    def position_change(self):
        return self.position_change

    @position_change.setter
    def position_change(self, value):
        self.position_change = value

    @property
    def manipulation(self):
        return self.manipulation

    @manipulation.setter
    def manipulation (self, value):
        self.manipulation = value
        

class Fijo(Thing):
    def __init__(self, x, y, element_name, position_change, manipulation):
        super().__init__(x, y, element_name, position_change, manipulation)

class Movible(Thing):
    def __init__(self, x, y, element_name, position_change, manipulation):
        super().__init__(x, y, element_name, position_change, manipulation)

    def mover(self, nueva_posicion):
        self.posicion = nueva_posicion

        if self.position_change == "Up":
            self.y =+ 1
        elif self.position_change == "Down":
            self.y =- 1
        elif self.position_change == "Left":
            self.x =- 1
        elif self.position_change == "Right":
            self.x =+ 1

class Abrible(Thing):
    def __init__(self, x, y, element_name, position_change, manipulation):
        super().__init__(x, y, element_name, position_change, manipulation)

class Mixto(Thing):
    def __init__(self, x, y, element_name, position_change, manipulation):
        super().__init__(x, y, element_name, position_change, manipulation)

    def mover(self, nueva_posicion, new_state):
        self.posicion = nueva_posicion
        self.state = new_state

        if self.position_change == "Up" and self.state == True:
            self.y =+ 1
            self.state = "Open"
            return self.y, self.state
        
        elif self.position_change == "Up" and self.state == False:
            self.y =+ 1
            self.state = "Closed"
        

if __name__=='__main__':
    
    #Se crean diferentes objetos de acorde a las caracteristicas presentadas en clase de cada objeto
    #El objeto fijo no se puede mover ni manipular
    #El objeto movible se puede mover pero no manipular
    #El objeto abrible no se puede mover pero si manipular
    #El objeto mixto se puede mover y manipular

    objeto_fijo = Fijo(0, 0, 'fijo', False, False)
    objeto_movible = Movible(0, 0, 'movible', True, False)
    objeto_abrible = Abrible(0, 0, 'abrible', False, True)
    objeto_mixto = Mixto(0, 0, 'mixto', True, True)

"""