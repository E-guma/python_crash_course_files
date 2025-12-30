# color_picker.py
import tkinter as tk
from tkinter import colorchooser

def pick_color():
    root = tk.Tk()
    root.withdraw()  # hide main window
    result = colorchooser.askcolor(title="Choose a color")
    root.destroy()
    if result[0] is None:
        print("No color chosen")
    else:
        rgb, hex_color = result
        print(f"RGB: {tuple(int(v) for v in rgb)}")
        print(f"HEX: {hex_color}")

if __name__ == "__main__":
    pick_color()