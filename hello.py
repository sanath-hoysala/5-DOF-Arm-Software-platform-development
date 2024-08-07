import tkinter as tk
from tkinter import ttk
import serial


def send_command():
    try:
        x_h = int(x_high.get(), 16)
        x_l = int(x_low.get(), 16)
        y_h = int(y_high.get(), 16)
        y_l = int(y_low.get(), 16)
        z_h = int(z_high.get(), 16)
        z_l = int(z_low.get(), 16)
        s_h = int(s_high.get(), 16)
        s_l = int(s_low.get(), 16)

        hex_values = [0xff, 0xfe, x_h, x_l, y_h, y_l, z_h, z_l, s_h, s_l]
        command = bytes(hex_values)
        SerialObj.write(command)
        result_label.config(text="Command sent successfully :)")

    except ValueError:
        result_label.config(text="Invalid hexadecimal input :(")


def on_closing():
    SerialObj.close()
    root.destroy()


root = tk.Tk()
root.title("Hexadecimal Command Sender")
root.geometry("400x300")

label = ttk.Label(master=root, text="Enter the coordinates")
label.pack()

input_frame = ttk.Frame(root)
input_frame.pack(pady=10)

x_label = ttk.Label(input_frame, text="X:")
x_label.grid(row=0, column=0, padx=5)
x_high = ttk.Entry(input_frame, width=4)
x_high.grid(row=0, column=1, padx=2)
x_low = ttk.Entry(input_frame, width=4)
x_low.grid(row=0, column=2, padx=2)

y_label = ttk.Label(input_frame, text="Y:")
y_label.grid(row=1, column=0, padx=5)
y_high = ttk.Entry(input_frame, width=4)
y_high.grid(row=1, column=1, padx=2)
y_low = ttk.Entry(input_frame, width=4)
y_low.grid(row=1, column=2, padx=2)

z_label = ttk.Label(input_frame, text="Z:")
z_label.grid(row=2, column=0, padx=5)
z_high = ttk.Entry(input_frame, width=4)
z_high.grid(row=2, column=1, padx=2)
z_low = ttk.Entry(input_frame, width=4)
z_low.grid(row=2, column=2, padx=2)

speed_label = ttk.Label(input_frame, text="Speed:")
speed_label.grid(row=3, column=0, padx=5)
s_high = ttk.Entry(input_frame, width=4)
s_high.grid(row=3, column=1, padx=2)
s_low = ttk.Entry(input_frame, width=4)
s_low.grid(row=3, column=2, padx=2)

send_button = ttk.Button(root, text="Send", command=send_command)
send_button.pack(pady=10)

result_label = ttk.Label(root, text="")
result_label.pack()
# Serial communication
SerialObj = serial.Serial('COM7', 115200)  # Replace 'COM1' with your actual port and set the correct baud rate

# root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()