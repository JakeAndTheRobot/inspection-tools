import tkinter as tk
import pyautogui

def get_mouse_info():
    x, y = pyautogui.position()
    pixel_color = pyautogui.screenshot().getpixel((x, y))
    hex_color = '#{:02x}{:02x}{:02x}'.format(*pixel_color)
    label_x.config(text='X: {}'.format(x))
    label_y.config(text='Y: {}'.format(y))
    label_rgb.config(text='RGB: {}'.format(pixel_color))
    label_hex.config(text='Hex: {}'.format(hex_color))
    canvas.config(bg=hex_color)
    root.after(100, get_mouse_info)

root = tk.Tk()
label_x = tk.Label(root, text='X:')
label_x.pack()
label_y = tk.Label(root, text='Y:')
label_y.pack()
label_rgb = tk.Label(root, text='RGB:')
label_rgb.pack()
label_hex = tk.Label(root, text='Hex:')
label_hex.pack()
canvas = tk.Canvas(root, width=128, height=128)
canvas.pack()
get_mouse_info()
root.mainloop()

