import tkinter as tk
from tkinter import ttk
from datetime import datetime
from tkcalendar import Calendar

class AgeCalculator:
    def __init__(self, root):
        # Initialize the main window
        self.root = root
        self.root.title("Age Calculator")
        self.root.geometry("400x500")
        self.root.configure(bg='#f0f0f0')
        
        # Create and configure style
        style = ttk.Style()
        style.configure('TLabel', font=('Arial', 12), padding=5)
        style.configure('TButton', font=('Arial', 11), padding=5)
        
        # Create header
        header = ttk.Label(root, text="Age Calculator", 
                          font=('Arial', 20, 'bold'))
        header.pack(pady=20)
        
        # Create calendar widget
        self.cal = Calendar(root, selectmode='day',
                          year=2000, month=1, day=1)
        self.cal.pack(pady=20)
        
        # Create calculate button
        calc_button = ttk.Button(root, text="Calculate Age",
                               command=self.calculate_age)
        calc_button.pack(pady=20)
        
        # Create frame for results
        self.result_frame = ttk.Frame(root)
        self.result_frame.pack(pady=20, fill='x', padx=20)
        
        # Labels for displaying results
        self.years_label = ttk.Label(self.result_frame, 
                                    text="Years: 0")
        self.years_label.pack()
        
        self.months_label = ttk.Label(self.result_frame, 
                                     text="Months: 0")
        self.months_label.pack()
        
        self.days_label = ttk.Label(self.result_frame, 
                                   text="Days: 0")
        self.days_label.pack()

    def calculate_age(self):
        # Get selected date from calendar
        birth_date = self.cal.get_date()
        birth_date = datetime.strptime(birth_date, '%m/%d/%y')
        
        # Get current date
        current_date = datetime.now()
        
        # Calculate age
        age_days = (current_date - birth_date).days
        years = age_days // 365
        remaining_days = age_days % 365
        months = remaining_days // 30
        days = remaining_days % 30
        
        # Update labels with calculated age
        self.years_label.config(text=f"Years: {years}")
        self.months_label.config(text=f"Months: {months}")
        self.days_label.config(text=f"Days: {days}")

def main():
    root = tk.Tk()
    app = AgeCalculator(root)
    root.mainloop()

if __name__ == "__main__":
    main() 