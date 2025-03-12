import tkinter as tk
from tkinter import ttk

class ColorPicker:
    def __init__(self, root):
        # Initialize the main window
        self.root = root
        self.root.title("Color Picker")
        self.root.geometry("500x400")
        self.root.configure(bg='#f0f0f0')
        
        # Create title
        title = ttk.Label(root, text="Interactive Color Picker",
                         font=('Arial', 18, 'bold'))
        title.pack(pady=15)
        
        # Create frame for sliders
        self.slider_frame = ttk.Frame(root)
        self.slider_frame.pack(pady=20, padx=30, fill='x')
        
        # RGB values
        self.red_val = tk.IntVar()
        self.green_val = tk.IntVar()
        self.blue_val = tk.IntVar()

        
        
        # Create RGB sliders
        self.create_slider("Red", self.red_val, '#ff0000')
        self.create_slider("Green", self.green_val, '#00ff00')
        self.create_slider("Blue", self.blue_val, '#0000ff')
        
        # Create color display frame
        self.color_display = tk.Frame(root, width=200, height=100,
                                    relief='solid', bd=1)
        self.color_display.pack(pady=20)
        
        # Create hex color label
        self.hex_label = ttk.Label(root, text="#000000",
                                  font=('Arial', 14))
        self.hex_label.pack(pady=10)
        
        # Create copy button
        copy_button = ttk.Button(root, text="Copy Hex Code",
                               command=self.copy_hex_code)
        copy_button.pack(pady=10)
        
        # Initialize color display
        self.update_color()

    def create_slider(self, color_name, variable, slider_color):
        # Create frame for each slider set
        frame = ttk.Frame(self.slider_frame)
        frame.pack(fill='x', pady=5)
        
        # Create label
        label = ttk.Label(frame, text=f"{color_name}:",
                         font=('Arial', 10))
        label.pack(side='left', padx=5)
        
        # Create slider
        slider = ttk.Scale(frame, from_=0, to=255,
                          orient='horizontal', variable=variable,
                          command=lambda _: self.update_color())
        slider.pack(side='left', fill='x', expand=True, padx=10)
        
        # Create value label
        value_label = ttk.Label(frame, textvariable=variable,
                               font=('Arial', 10))
        value_label.pack(side='left', padx=5)

    def update_color(self):
        # Get current RGB values
        r = self.red_val.get()
        g = self.green_val.get()
        b = self.blue_val.get()
        
        # Create hex color code
        hex_color = f'#{r:02x}{g:02x}{b:02x}'
        
        # Update color display
        self.color_display.configure(bg=hex_color)
        self.hex_label.configure(text=hex_color.upper())

    def copy_hex_code(self):
        # Copy hex code to clipboard
        hex_code = self.hex_label.cget("text")
        self.root.clipboard_clear()
        self.root.clipboard_append(hex_code)
        
        # Show temporary feedback
        original_text = self.hex_label.cget("text")
        self.hex_label.configure(text="Copied!")
        self.root.after(1000, lambda: self.hex_label.configure(text=original_text))

def main():
    root = tk.Tk()
    app = ColorPicker(root)
    root.mainloop()

if __name__ == "__main__":
    main() 