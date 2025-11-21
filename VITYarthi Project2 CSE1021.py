# --- GUI Desktop Calculator (Tkinter) ---

import tkinter as tk
from tkinter import messagebox

class CalculatorApp:
    """
    Represents the main calculator application and handles all UI and logic.
    """
    def __init__(self, master):
        self.master = master
        master.title("Advanced GUI Calculator")
        master.configure(bg="#2E4053")
        
        # Current expression displayed on the screen
        self.expression = ""
        
        # 1. Display/Input Field
        self.display = tk.Entry(
            master, 
            width=25, 
            font=('Arial', 24), 
            bd=5, 
            relief=tk.SUNKEN,
            justify='right',
            bg="#ECF0F1", 
            fg="#2C3E50"  
        )
        # Span the display across all columns (4) and add padding
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=20)
        
        # 2. Define Buttons Layout
        # Tuple of (text, row, col, color)
        buttons = [
            ('C', 1, 0, '#E74C3C'), ('%', 1, 1, '#2ECC71'), ('**', 1, 2, '#2ECC71'), ('/', 1, 3, '#E67E22'),
            ('7', 2, 0, '#BDC3C7'), ('8', 2, 1, '#BDC3C7'), ('9', 2, 2, '#BDC3C7'), ('*', 2, 3, '#E67E22'),
            ('4', 3, 0, '#BDC3C7'), ('5', 3, 1, '#BDC3C7'), ('6', 3, 2, '#BDC3C7'), ('-', 3, 3, '#E67E22'),
            ('1', 4, 0, '#BDC3C7'), ('2', 4, 1, '#BDC3C7'), ('3', 4, 2, '#BDC3C7'), ('+', 4, 3, '#E67E22'),
            ('0', 5, 0, '#BDC3C7'), ('.', 5, 1, '#BDC3C7'), ('=', 5, 2, '#3498DB'), ('(', 6, 0, '#2ECC71'),
            (')', 6, 1, '#2ECC71'), 
        ]
        
        # 3. Create and Place Buttons
        row_offset = 1 
        for (text, r, c, color, *span) in buttons:
            colspan = span[0] if span else 1
            
            # Use lambda to pass button text to the handler function
            action = lambda x=text: self.button_click(x)
            
            btn = tk.Button(
                master, 
                text=text, 
                padx=20, 
                pady=20, 
                font=('Arial', 16, 'bold'), 
                bg=color,
                fg="#FFFFFF", # White text
                relief=tk.RAISED,
                command=action
            )
            
            # Handle the equal button separately for stretching
            if text == '=':
                btn.grid(row=r, column=c, columnspan=2, padx=5, pady=5, sticky="nsew")
            else:
                btn.grid(row=r, column=c, padx=5, pady=5, sticky="nsew")

            # Make the grid cells expand nicely
            master.grid_columnconfigure(c, weight=1)
            master.grid_rowconfigure(r, weight=1)


    def button_click(self, text):
        """Handles button clicks and updates the display/expression."""
        if text == 'C':
            # Clear the expression and display
            self.expression = ""
            self.display.delete(0, tk.END)
        elif text == '=':
            # Evaluate the expression
            self.calculate()
        elif text == '**':
            # Insert the power operator (Python standard)
            self.expression += "**"
            self.display.insert(tk.END, "**")
        else:
            # Append number or standard operator
            self.expression += str(text)
            self.display.insert(tk.END, text)

    def calculate(self):
        """Evaluates the mathematical expression using eval() and handles errors."""
        try:
            # Use Python's built-in eval() for expression evaluation (supports PEMDAS/BODMAS)
            result = str(eval(self.expression))
            
            # Clear the display and show the result
            self.display.delete(0, tk.END)
            self.display.insert(0, result)
            
            # Set the new result as the base for the next calculation
            self.expression = result
            
        except ZeroDivisionError:
            self.display.delete(0, tk.END)
            self.display.insert(0, "Error: Divide by Zero")
            self.expression = ""
        except SyntaxError:
            self.display.delete(0, tk.END)
            self.display.insert(0, "Error: Invalid Expression")
            self.expression = ""
        except Exception:
            self.display.delete(0, tk.END)
            self.display.insert(0, "Error")
            self.expression = ""

# Run the application
if __name__ == '__main__':
    # Create the main window
    root = tk.Tk()
    
    # Initialize the Calculator class
    app = CalculatorApp(root)
    
    # Start the Tkinter event loop
    root.mainloop()