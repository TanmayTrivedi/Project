import tkinter as tk
from tkinter import ttk
import time

class TickerGUI:
    def __init__(self, root):
        # Initialize the main window
        self.root = root
        self.root.title("Scrolling Ticker")
        self.root.geometry("600x100")
        self.root.configure(bg='#2C3E50')

        # Create a style for the label
        style = ttk.Style()
        style.configure('Ticker.TLabel', 
                       background='#2C3E50',
                       foreground='#ECF0F1',
                       font=('Arial', 24, 'bold'))

        # Create the ticker label
        self.ticker_text = "Welcome to the Ticker Display! * This is a scrolling message * "
        self.ticker_label = ttk.Label(root, 
                                    text=self.ticker_text,
                                    style='Ticker.TLabel')
        self.ticker_label.pack(pady=30)

        # Initialize position and animation
        self.position = 0
        self.animate_ticker()

    def animate_ticker(self):
        # Update the text position
        self.position = (self.position + 1) % len(self.ticker_text)
        display_text = self.ticker_text[self.position:] + self.ticker_text[:self.position]
        self.ticker_label.config(text=display_text)
        
        # Schedule the next animation frame
        self.root.after(100, self.animate_ticker)

def main():
    root = tk.Tk()
    app = TickerGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main() 