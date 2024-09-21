import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk


# Function to simulate image loading for molecules
def load_image(path, size=(100, 100)):
    img = Image.open(path)
    img = img.resize(size)
    return ImageTk.PhotoImage(img)


# Simple function to display an unbalanced or balanced chemical equation
def update_equation_display():
    # Update the visual representation based on current coefficients
    reactant_label.config(text=f"{coef_h2.get()} H2 + {coef_o2.get()} O2")
    product_label.config(text=f"{coef_h2o.get()} H2O")

    # Check if the equation is balanced
    if (2 * coef_h2.get() == 2 * coef_h2o.get()) and (2 * coef_o2.get() == coef_h2o.get()):
        balance_status.config(text="Balanced!", fg="green")
    else:
        balance_status.config(text="Unbalanced", fg="red")


# Function to balance the equation automatically
def balance_equation():
    coef_h2.set(2)
    coef_o2.set(1)
    coef_h2o.set(2)
    update_equation_display()
    messagebox.showinfo("Balanced", "The equation has been automatically balanced.")


# Create main window
root = tk.Tk()
root.title("Chemical Equation Balancer (Visual)")

# Load images for H2, O2, H2O molecules
h2_image = load_image("h2.png")
o2_image = load_image("o2.png")
h2o_image = load_image("h2o.png")

# Create Tkinter variables for coefficients
coef_h2 = tk.IntVar(value=1)
coef_o2 = tk.IntVar(value=1)
coef_h2o = tk.IntVar(value=1)

# Display molecule images
tk.Label(root, image=h2_image).grid(row=0, column=0, padx=10)
tk.Label(root, image=o2_image).grid(row=0, column=2, padx=10)
tk.Label(root, image=h2o_image).grid(row=0, column=4, padx=10)

# Labels to display the chemical equation
reactant_label = tk.Label(root, text="1 H2 + 1 O2", font=("Arial", 16))
reactant_label.grid(row=1, column=0, columnspan=3)

tk.Label(root, text="->", font=("Arial", 16)).grid(row=1, column=3)

product_label = tk.Label(root, text="1 H2O", font=("Arial", 16))
product_label.grid(row=1, column=4)

# Buttons to manually increase/decrease coefficients
tk.Button(root, text="Increase H2", command=lambda: coef_h2.set(coef_h2.get() + 1)).grid(row=2, column=0, pady=10)
tk.Button(root, text="Decrease H2", command=lambda: coef_h2.set(max(1, coef_h2.get() - 1))).grid(row=3, column=0,
                                                                                                 pady=10)

tk.Button(root, text="Increase O2", command=lambda: coef_o2.set(coef_o2.get() + 1)).grid(row=2, column=2, pady=10)
tk.Button(root, text="Decrease O2", command=lambda: coef_o2.set(max(1, coef_o2.get() - 1))).grid(row=3, column=2,
                                                                                                 pady=10)

tk.Button(root, text="Increase H2O", command=lambda: coef_h2o.set(coef_h2o.get() + 1)).grid(row=2, column=4, pady=10)
tk.Button(root, text="Decrease H2O", command=lambda: coef_h2o.set(max(1, coef_h2o.get() - 1))).grid(row=3, column=4,
                                                                                                    pady=10)

# Status label to show if the equation is balanced
balance_status = tk.Label(root, text="Unbalanced", font=("Arial", 16), fg="red")
balance_status.grid(row=4, column=0, columnspan=5, pady=10)

# Button to auto-balance the equation
tk.Button(root, text="Balance Equation", command=balance_equation).grid(row=5, column=0, columnspan=5, pady=20)

# Monitor changes in coefficients and update display
coef_h2.trace_add("write", lambda *args: update_equation_display())
coef_o2.trace_add("write", lambda *args: update_equation_display())
coef_h2o.trace_add("write", lambda *args: update_equation_display())

# Start Tkinter event loop
root.mainloop()