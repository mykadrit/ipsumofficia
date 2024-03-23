import tkinter as tk

last_window = None

def create_window(title, width, height):
    global last_window
    if last_window is not None:
        last_window.destroy()
    last_window = tk.Tk()
    last_window.title(title)
    last_window.geometry(f"{width}x{height}")
    return last_window

# Example usage
window = create_window("My Window", 500, 300)
window.mainloop()
