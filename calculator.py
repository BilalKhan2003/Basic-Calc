import tkinter as tk

def on_click(char):
    current = display_var.get()
    display_var.set(current + str(char))

def clear_display():
    display_var.set("")

def calculate_result():
    try:
        # Evaluate the math expression in the display
        result = str(eval(display_var.get()))
        display_var.set(result)
    except Exception:
        display_var.set("Error")

# Initialize main window
root = tk.Tk()
root.title("Calculator")
root.geometry("320x450")
root.configure(bg="#1e1e24")
root.resizable(False, False)

# Display Screen
display_var = tk.StringVar()
display = tk.Entry(
    root, 
    textvariable=display_var, 
    font=('Helvetica', 28, 'bold'), 
    bg="#1e1e24", 
    fg="#ffffff", 
    bd=0, 
    justify="right"
)
display.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=25, pady=10, sticky="nsew")

# Styling configurations
button_style = {"font": ('Helvetica', 16, 'bold'), "bd": 0, "fg": "white", "height": 2, "width": 5}
color_num = "#2d2d3a"
color_op = "#ff9500"
color_clear = "#ff453a"
color_active = "#4a4a5e"

# Button Layout Matrix
buttons = [
    ('7', 1, 0, color_num), ('8', 1, 1, color_num), ('9', 1, 2, color_num), ('/', 1, 3, color_op),
    ('4', 2, 0, color_num), ('5', 2, 1, color_num), ('6', 2, 2, color_num), ('*', 2, 3, color_op),
    ('1', 3, 0, color_num), ('2', 3, 1, color_num), ('3', 3, 2, color_num), ('-', 3, 3, color_op),
    ('C', 4, 0, color_clear), ('0', 4, 1, color_num), ('.', 4, 2, color_num), ('+', 4, 3, color_op)
]

# Generate Buttons
for (text, row, col, bg_color) in buttons:
    action = clear_display if text == 'C' else lambda t=text: on_click(t)
    
    btn = tk.Button(
        root, 
        text=text, 
        bg=bg_color, 
        activebackground=color_active,
        activeforeground="white",
        command=action, 
        **button_style
    )
    btn.grid(row=row, column=col, padx=4, pady=4)

# Equal Button (Spans full width)
equal_btn = tk.Button(
    root, 
    text="=", 
    bg=color_op, 
    activebackground="#d97a00",
    activeforeground="white",
    command=calculate_result, 
    **button_style
)
equal_btn.grid(row=5, column=0, columnspan=4, sticky="nsew", padx=4, pady=4)

# Configure row/column weights for proper spacing
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

root.mainloop()