"""
import tkinter as tk


class Objeto:
    def __init__(self, canvas, forma, color, posicion):
        self.canvas = canvas
        self.forma = forma
        self.color = color
        self.posicion = posicion
        self.objeto = None

    def dibujar(self):
        self.objeto = self.canvas.create_rectangle(self.posicion[0], self.posicion[1], self.posicion[0] + 30, self.posicion[1] + 30, fill=self.color)

    def desplazarse(self, nueva_posicion):
        self.posicion = nueva_posicion
        self.canvas.coords(self.objeto, self.posicion[0], self.posicion[1], self.posicion[0] + 30, self.posicion[1] + 30)

#Onjeto que no cambia ni de estado ni se mueve
class ObjetoFijo(Objeto):
    def __init__(self, canvas, forma, color, posicion):
        super().__init__(canvas, forma, color, posicion)
        self.dibujar()

    def caracteristica(self):
        print("Soy un objeto fijo y no puedo desplazarme.")

#Objeto que se mueve pero no cambia de estado
class ObjetoMovil(Objeto):
    def __init__(self, canvas, forma, color, posicion):
        super().__init__(canvas, forma, color, posicion)
        self.dibujar()

    def desplazarse(self, nueva_posicion):
        self.posicion = nueva_posicion
        self.canvas.coords(self.objeto, self.posicion[0], self.posicion[1], self.posicion[0] + 30, self.posicion[1] + 30)
        print("Objeto móvil desplazándose a:", nueva_posicion)

#Objeto que no se mueve pero cambia de estado
class ObjetoAbrible(Objeto):
    def __init__(self, canvas, forma, color, posicion):
        super().__init__(canvas, forma, color, posicion)
        self.abierto = False
        self.dibujar()

    def cambiar_estado(self):
        if self.abierto:
            self.abierto = False
            print("Objeto abrible cerrado.")
        else:
            self.abierto = True
            print("Objeto abrible abierto.")

#Objeto que se mueve y cambia de estado
class ObjetoMixto(ObjetoMovil, ObjetoAbrible):
    def __init__(self, canvas, forma, color, posicion):
        ObjetoMovil.__init__(self, canvas, forma, color, posicion)
        ObjetoAbrible.__init__(self, canvas, forma, color, posicion)


# Crear la interfaz gráfica
root = tk.Tk()
root.title("Objetos con Características")

canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

# Crear objetos
objeto_fijo = ObjetoFijo(canvas, "rect", "blue", (50, 50))
objeto_movil = ObjetoMovil(canvas, "oval", "red", (150, 50))
objeto_abrible = ObjetoAbrible(canvas, "rectangle", "green", (250, 50))
objeto_mixto = ObjetoMixto(canvas, "oval", "purple", (50, 150))

# Mover el objeto móvil y cambiar el estado del objeto abrible
objeto_movil.desplazarse((350, 100))
objeto_abrible.cambiar_estado()

# Mantener la ventana abierta
root.mainloop()

#Realizacion de tests unitarios para comprobar el funcionamiento del programa

"""