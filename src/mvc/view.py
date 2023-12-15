import sys
sys.path.insert(0, '.')

import tkinter as tk
import src.mvc.model as model
from utiles.commons import *
from src.mvc.observer import Observer
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.animation as animation
import numpy as np
import itertools

class View(tk.Tk, Observer):

    currentVitals = []

    def __init__(self, name, height, width): # matrix, agent_list, 

        tk.Tk.__init__(self)
        Observer.__init__(self, name)

    
        self.controller = None

        self.height = height
        self.min_height = height 
        self.width = width
        self.min_width = width 
        self.CELL_SIZE = 40 
        self.title("Entorno Domótico")
        self.geometry(str(width) + "x" + str(height+30))
        self.minsize(self.min_width, self.min_height)

        frame = tk.Frame(self)
        frame.pack(fill=tk.BOTH, expand=True)

        
        button1 = tk.Button(frame, text="Click to move agents", 
                            command=self.button1_clicked, bg='grey', font=("Cascadia Code", 12), border=2)
        button1.grid(row=0, column=1, sticky='nsew')


        new_window_button = tk.Button(frame, text="Health Monitor", command=self.open_monitor_window,
                                      bg='grey', font=("Cascadia Code", 12), border=2)
        new_window_button.grid(row=0, column=2, sticky='nsew')

        """
        button2 = tk.Button(frame, text="Collision Test (16x16)", command=self.button2_clicked)
        button2.grid(row=0, column=1, sticky='nsew')

        button3 = tk.Button(frame, text="Door Test (16x16 Room Size ONLY)", command=self.button3_clicked)
        button3.grid(row=0, column=2, sticky='nsew')
        """

        # Configure the columns to distribute extra space equally
        frame.columnconfigure(0, weight=1)
        frame.columnconfigure(1, weight=1)
        frame.columnconfigure(2, weight=1)

        #It defines the srpites for each object's representation
        self.wall_image = tk.PhotoImage(file="./assets/sprites/wall.png")
        self.sofa_image = tk.PhotoImage(file="./assets/sprites/sofa.png")
        self.table_image = tk.PhotoImage(file="./assets/sprites/table.png")
        self.door_image = tk.PhotoImage(file="./assets/sprites/door.png")
        self.door_open_image = tk.PhotoImage(file="./assets/sprites/door_open.png")
        self.fridge_image = tk.PhotoImage(file="./assets/sprites/fridge.png")
        self.agent_image = tk.PhotoImage(file="./assets/sprites/gato.png")
        self.owner_image = tk.PhotoImage(file="./assets/sprites/owner1.png")
        self.enfermera_image = tk.PhotoImage(file="./assets/sprites/enfermera2.png")
        
        

        #Links the skins with the object literal name
        self.img_dict = {"Wall": self.wall_image, "Sofa": self.sofa_image, "Gato": self.agent_image, 
                          "Table": self.table_image, "Door_Closed": self.door_image, 
                          "Door_Open": self.door_open_image, "Fridge": self.fridge_image,
                          "Owner": self.owner_image, "Enfermera": self.enfermera_image,
                          }

        #Initialices the model with all the atributes
        self.canvas= tk.Canvas(self, bg='white', height=height, width=width)
        self.canvas.pack(expand=True, fill='both')

        self.update() #Show view
        self.draw_grid(width, height) #Draw Grid
        self.attributes('-topmost', True) #Show Window on Top of other Windows

        # Configure the new column
        frame.columnconfigure(3, weight=1)


    def resize_window(self):
        """
        Resizes the window to fit the required width and height.
        """
        self.update_idletasks()
        width = self.winfo_reqwidth()
        height = self.winfo_reqheight()
        self.geometry(f"{width}x{height+30}")
        self.minsize(self.min_width, self.min_height)


    def set_controller(self, controller):
        """
        Set the controller for the view.

        Parameters:
        - controller: The controller object to be set.

        Returns:
        None
        """
        self.controller = controller

    def draw_grid(self, width:int, height:int):
        """
        Draws grid lines on the canvas.
        """
        
        for i in range(0, width, self.CELL_SIZE):
            self.canvas.create_line([(i, 0), (i, height)], tag='grid_line', fill='grey')

        for i in range(0, height, self.CELL_SIZE):
            self.canvas.create_line([(0, i), (width, i)], tag='grid_line', fill='grey')

    
    def updateFromNotification(self, *args, **kwargs):
        """
        Update the view based on the notification.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            None
        """
        NOTIFY_KEYS = ('agents', 'matrix', 'vitals')

        for key, value in kwargs.items():
            if key not in NOTIFY_KEYS:
                raise KeyError(f"Invalid key: {key}")
            else:        
                match key:
                    case 'agents':
                        self.draw_agents(value)
                    case 'matrix':
                        self.draw_map(value)
                    case 'vitals':
                        self.currentVitals.clear()
                        self.currentVitals.extend(value)


                            
    def draw_map(self, map, grid = True):
        """
        Representents a new view

        Updates the view by clearing the canvas and redrawing objects based on the model.
        You can specify which objects you want to delete. For example, fixed objects like walls,
        do not need to be deleted and redrawn.
        """

        
        self.canvas.delete("object")
        
        # Draw the objects
        for row in map:
            for object in row:
                if object == 0:
                    continue
                elif object.literal_name != "Door":
                    img = self.img_dict.get(object.literal_name)
                else:
                    if object.isOpen:
                        img = self.img_dict.get("Door_Open")
                    elif object.isOpen == False:
                        img = self.img_dict.get("Door_Closed")
                
                # Paints the image of the object based on it's sprite PNG.
                self.canvas.create_image(
                    object.x * 40, object.y * 40, image=img, anchor='nw' , tags="object"
                )

        if grid:
            self.draw_grid(self.width, self.height)

        self.update()

    def draw_agents(self, agents):
        
        # Draw the agents
        self.canvas.delete("agent")
        
        for agent in agents:
            img_agent = self.img_dict.get(agent.name)

           
            self.canvas.create_image(
                agent.x * 40, agent.y * 40, image=img_agent, anchor='nw', tags="agent"
            )

        self.update()

    
    def button1_clicked(self):
        """
        Handle the click event for button1.

        If a controller is available, call its handle_click method with the argument "movement".
        """
        if self.controller:
            self.controller.handle_click("movement")

    '''
    def button2_clicked(self):
        """
        Handle the click event for button2.

        If a controller is set, call its handle_click method with the argument "collision".
        """
        if self.controller:
            self.controller.handle_click("collision")

    def button3_clicked(self):
        """
        Handle the click event for button3.

        If a controller is available, call its handle_click method with the argument "door".
        """
        if self.controller:
            self.controller.handle_click("door")
    '''




    def open_monitor_window(self):
        """
        Opens a new independent window.
        """

        # Create a new Toplevel window
        new_window = tk.Toplevel(self)
        new_window.title("Vital Constants Monitor")
        new_window.geometry("800x600")
        new_window.attributes('-topmost', True)

        #close_button = tk.Button(new_window, text="Close", command=new_window.destroy)
        #close_button.pack(pady=10)

        

        # Initialize the main window using Tkinter
        # Create a frame for displaying the vital signs labels
        label_frame = ttk.Frame(new_window)
        label_frame.pack(pady=10)

        # Labels for displaying various vital signs
        heart_rate_label = tk.Label(label_frame, text="Heart Rate: -- bpm", font=("Helvetica", 16))
        heart_rate_label.grid(row=0, column=0, padx=10)

        blood_pressure_label = tk.Label(label_frame, text="Blood Pressure: --/--", font=("Helvetica", 16))
        blood_pressure_label.grid(row=0, column=1, padx=10)

        temperature_label = tk.Label(label_frame, text="Body Temperature: --°C", font=("Helvetica", 16))
        temperature_label.grid(row=1, column=0, padx=10)

        respiratory_rate_label = tk.Label(label_frame, text="Respiratory Rate: -- bpm", font=("Helvetica", 16))
        respiratory_rate_label.grid(row=1, column=1, padx=10)

        oxygen_saturation_label = tk.Label(label_frame, text="Oxygen Saturation: --%", font=("Helvetica", 16))
        oxygen_saturation_label.grid(row=2, column=0, padx=10)

        gcs_label = tk.Label(label_frame, text="Glasgow Coma Scale: --", font=("Helvetica", 16))
        gcs_label.grid(row=2, column=1, padx=10)

        # Creating a matplotlib figure with two subplots for heart rate and ECG
        fig = Figure(dpi=110)
        ax1 = fig.add_subplot(211)
        ax2 = fig.add_subplot(212)

        # Setting titles and labels for the subplots
        ax1.set_title("Heart Rate Over Time")
        ax1.set_xlabel("Time (s)")
        ax1.set_ylabel("Heart Rate (bpm)")

        ax2.set_title("ECG Waveform")
        ax2.set_xlabel("Time (s)")
        ax2.set_ylabel("Amplitude")

        # Initializing data lists for the plots
        xdata1, ydata1 = [], []  # Data for heart rate plot
        xdata2, ydata2 = [], []  # Data for ECG plot

        # Styling for ax1 - Heart Rate plot
        ax1.set_facecolor('#f0f8ff')  # Set background color to light azure
        ax1.grid(which='major', linestyle='-', linewidth='0.5', color='blue')  # Major grid lines
        ax1.minorticks_on()
        ax1.grid(which='minor', linestyle=':', linewidth='0.2', color='blue')  # Minor grid lines
        ax1.set_xticks(np.arange(0, 60, 5))  # Major ticks every 5 seconds
        ax1.set_xticks(np.arange(0, 60, 1), minor=True)  # Minor ticks every 1 second
        ax1.set_yticks(np.arange(50, 150, 10))  # Major ticks every 10 bpm
        ax1.set_yticks(np.arange(50, 150, 2), minor=True)  # Minor ticks every 2 bpm

        # Styling for ax2 - ECG plot
        ax2.set_facecolor('#FFF0F0')  # Set background color to light pink (ECG paper style)
        ax2.grid(which='major', linestyle='-', linewidth='0.5', color='red')  # Major grid lines
        ax2.set_xticks(np.arange(0, 2, 0.2))  # 0.2s intervals for x-axis
        ax2.set_yticks(np.arange(-1, 1.5, 0.5))  # 0.5mV intervals for y-axis
        ax2.grid(which='minor', linestyle=':', linewidth='0.2', color='red')  # Minor grid lines
        ax2.set_xticks(np.arange(0, 2, 0.04), minor=True)  # 0.04s intervals for x-axis
        ax2.set_yticks(np.arange(-1, 1.5, 0.1), minor=True)  # 0.1mV intervals for y-axis

        # Line plots for heart rate and ECG
        ln1, = ax1.plot([], [], color='#FF6848', linestyle='-', label='Heart Rate', animated=True)
        ln2, = ax2.plot([], [], 'r-', label='ECG', animated=True)

        # Adding legends to the plots
        ax1.legend(loc="upper right")
        ax2.legend(loc="upper right")

        # Ensuring proper layout of the plots within the figure
        fig.tight_layout()

        def init():
            """
            Initialize the plot limits and return the line objects for animation.
            
            Returns:
            tuple: A tuple of line objects (ln1, ln2).
            """
            ax1.set_xlim(0, 50)  # Set initial x-axis limit for heart rate plot
            ax1.set_ylim(50, 150)  # Set y-axis limits for heart rate plot
            ax2.set_xlim(0, 2)  # Set initial x-axis limit for ECG plot
            ax2.set_ylim(-1, 1)  # Set y-axis limits for ECG plot
            return ln1, ln2
        


        def update_vital(frame):

            """
            Update function for vital signs animation. Generates random data for vitals and updates the graph.

            Args:
            frame (int): The current frame number in the animation.

            Returns:
            tuple: A tuple containing the updated line object (ln1).
            """


            # Formatting values for display
            formatted_heart_rate = f"{self.currentVitals[0]:03}"
            formatted_gcs_score = f"{self.currentVitals[5]:02}"

            # Update the labels with new values
            heart_rate_label.config(text=f"Heart Rate: {formatted_heart_rate} bpm")
            blood_pressure_label.config(text=f"Blood Pressure: {self.currentVitals[1]}")
            temperature_label.config(text=f"Body Temperature: {self.currentVitals[2]}°C")
            respiratory_rate_label.config(text=f"Respiratory Rate: {self.currentVitals[3]} bpm")
            oxygen_saturation_label.config(text=f"Oxygen Saturation: {self.currentVitals[4]}%")
            gcs_label.config(text=f"Glasgow Coma Scale: {formatted_gcs_score}")

            # Update heart rate graph
            xdata1.append(frame)
            ydata1.append(self.currentVitals[0])
            ln1.set_data(xdata1, ydata1)

            # Adjust x-axis limits for scrolling effect
            if len(xdata1) > 50:
                ax1.set_xlim(frame - 50, frame)

            # Maintain a fixed buffer size for the data
            buffer_length = 500
            if len(xdata1) > buffer_length:
                xdata1.pop(0)
                ydata1.pop(0)

            return (ln1,)



        def create_ecg_cycle(t, heart_rate):
            """
            Create a single ECG cycle based on time 't' and heart rate.

            Args:
            t (float): The time variable.
            heart_rate (int): The heart rate in beats per minute.

            Returns:
            float: The ECG waveform value at time 't'.
            """
            T = 60 / heart_rate  # Total time for one heart beat in seconds
            p_duration = 0.25 * T  # Duration of P wave
            qrs_duration = 0.1 * T  # Duration of QRS complex
            t_duration = 0.4 * T  # Duration of T wave

            # ECG waveform components (P wave, QRS complex, T wave)
            p_wave = 0.1 * np.sin(2 * np.pi * t / p_duration) if t % T < p_duration else 0
            qrs_complex = 0.5 * np.sin(2 * np.pi * (t - p_duration) / qrs_duration) if p_duration <= t % T < p_duration + qrs_duration else 0
            t_wave = 0.2 * np.sin(2 * np.pi * (t - p_duration - qrs_duration) / t_duration) if p_duration + qrs_duration <= t % T < T else 0

            return p_wave + qrs_complex + t_wave

        
        def update_ecg(frame):
            """
            Update function for the ECG waveform animation. Generates ECG waveform based on heart rate.

            Args:
            frame (int): The current frame number in the animation.

            Returns:
            tuple: A tuple containing the updated line object (ln2).
            """
            

            # Continuous time variable for ECG
            t = frame / 50

            # Generate ECG waveform data
            y = create_ecg_cycle(t, self.currentVitals[0]) #Hearth Rate
            xdata2.append(t)
            ydata2.append(y)

            # Maintain a fixed buffer size for the data
            buffer_length = 500
            if len(xdata2) > buffer_length:
                xdata2.pop(0)
                ydata2.pop(0)

            # Update ECG line plot
            ln2.set_data(xdata2, ydata2)

            # Adjust x-axis limits for a scrolling effect
            if t > ax2.get_xlim()[1]:  
                ax2.set_xlim(ax2.get_xlim()[0] + 1.6, ax2.get_xlim()[1] + 1.6)

            return (ln2,)

        # Embedding the matplotlib figure in the Tkinter window
        canvas = FigureCanvasTkAgg(fig, master=new_window)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.pack(fill=tk.BOTH, expand=True)

        # Creating animations for vital signs and ECG waveform
        self.ani1 = animation.FuncAnimation(fig, update_vital, interval=500, frames=itertools.count(), init_func=init, blit=True, cache_frame_data=False)
        self.ani2 = animation.FuncAnimation(fig, update_ecg, interval=20, frames=itertools.count(), init_func=init, blit=True, cache_frame_data=False)





# Ejemplo de uso
if __name__ == '__main__':

    from src.mvc.controller import Controller

    height = 640
    width = 640

    room = model.Model(16, 16)
    file_path = 'assets/default_16x16_room.json'
    room.populate_room(file_path)

    gato1 = owner.Owner("Gato", 7, 7)
    gato2 = owner.Owner("Gato", 13, 13)
    gato3 = owner.Owner("Gato", 3, 11)
    gato4 = owner.Owner("Gato", 11, 3)
    room.generate_agents(gato1, gato2, gato3, gato4)

    view = View('view', height, width)

    main_controller = Controller(room, view)
    main_controller.vital_threading()

    #room.attach(view)
    #print(view.controller)
    #print(room._observers)

    #room.attach(view)
    room.notify(view, agents=room.agents, matrix=room.matrix)
  


    """
    def runtasks(i):
        #room.notify(view, agents=room.agents, matrix=room.matrix)
        #view.after(1000, room.notify(view, vitals=room.agents[0].vitals))
        view.after(1, room.notify(view, vitals=room.agents[0].vitals))
        id = view.after(1000, runtasks, i) 
        return id
    
    task_id = runtasks(0)
    #view.after_cancel(task_id)
    """

    '''
    main_controller.updateFromNotification(agent_move_right=0)
    main_controller.updateFromNotification(agent_move_right=0)
    main_controller.updateFromNotification(agent_move_right=0)
    main_controller.updateFromNotification(agent_move_right=0)
    main_controller.updateFromNotification(agent_move_right=0)
    main_controller.updateFromNotification(agent_move_right=0)
    '''

    # Start the main event loop
    view.mainloop()
    