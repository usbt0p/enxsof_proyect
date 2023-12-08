import tkinter as tk
import random
import time

def update_vitals():
    # Simulate heart rate and other vitals
    heart_rate = random.randint(60, 100)
    blood_pressure = f"{random.randint(100, 140)}/{random.randint(60, 90)}"
    
    # Update the labels with new values
    heart_rate_label.config(text=f"Heart Rate: {heart_rate} bpm")
    blood_pressure_label.config(text=f"Blood Pressure: {blood_pressure}")
    
    # Call this function again after 1000 milliseconds
    root.after(1000, update_vitals)

# Create the main window
root = tk.Tk()
root.title("Vital Constants Monitor")

# Create labels for displaying the vitals
heart_rate_label = tk.Label(root, text="Heart Rate: -- bpm", font=("Helvetica", 16))
heart_rate_label.pack(pady=10)

blood_pressure_label = tk.Label(root, text="Blood Pressure: --/--", font=("Helvetica", 16))
blood_pressure_label.pack(pady=10)

# Start updating vitals
update_vitals()

# Run the application
root.mainloop()
