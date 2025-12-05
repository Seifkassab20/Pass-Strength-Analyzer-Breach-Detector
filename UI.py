import tkinter as tk
from tkinter import messagebox, scrolledtext

# Import your feature modules
import password              # Feature C — Password Generator
import breach                # Feature B — Breach Detector
import PSA                   # Feature A — Strength Analyzer
import password_store        # Feature D — Secure Storage

# -------------------------------------------
# FEATURE A — Check Password Strength
# -------------------------------------------

def check_strength():
    pwd = entry_password.get()
    if not pwd:
        messagebox.showwarning("Input Error", "Please enter a password.")
        return

    result = PSA.password_strength(pwd)   # FIXED

    strength_output.delete("1.0", tk.END)
    strength_output.insert(tk.END, f"Strength: {result['strength']}\n")
    strength_output.insert(tk.END, f"Score: {result['score']}\n\n")
    strength_output.insert(tk.END, "Suggestions:\n")
    for s in result["suggestions"]:
        strength_output.insert(tk.END, f"- {s}\n")

# -------------------------------------------
# FEATURE B — Breach Detector
# -------------------------------------------

def check_breach():
    pwd = entry_password.get()
    if not pwd:
        messagebox.showwarning("Input Error", "Please enter a password.")
        return

    breached = breach.is_breached(pwd)    # must exist in breach.py

    if breached:
        messagebox.showerror("BREACHED", "⚠ Password found in known breached datasets!")
    else:
        messagebox.showinfo("Safe", "✓ Password NOT found in breach lists.")

# -------------------------------------------
# FEATURE C — Secure Password Generator
# -------------------------------------------

def generate_password():
    new_pwd = password.generate_password(16, True, True, True, True)  # FIXED
    entry_generated.delete(0, tk.END)
    entry_generated.insert(0, new_pwd)

# -------------------------------------------
# FEATURE D — Hash & Store Password
# -------------------------------------------

def store_password():
    pwd = entry_password.get()
    if not pwd:
        messagebox.showwarning("Input Error", "Please enter a password first.")
        return

    hashed = password_store.hash_password(pwd)
    password_store.store_password(hashed)

    messagebox.showinfo("Stored", "Password hashed & stored securely!")

# -------------------------------------------
# UI Layout
# -------------------------------------------

app = tk.Tk()
app.title("Password Security Toolkit")
app.geometry("650x600")
app.resizable(False, False)

lbl_title = tk.Label(app, text="Password Security Toolkit", font=("Arial", 20, "bold"))
lbl_title.pack(pady=10)

# Input field
tk.Label(app, text="Enter Password:", font=("Arial", 12)).pack()
entry_password = tk.Entry(app, width=40, show="*")
entry_password.pack(pady=5)

# Buttons
tk.Button(app, text="Check Strength", width=20, command=check_strength).pack(pady=5)
tk.Button(app, text="Check Breach", width=20, command=check_breach).pack(pady=5)
tk.Button(app, text="Store Password Securely", width=25, command=store_password).pack(pady=5)

tk.Label(app, text="Strength Analysis Output:", font=("Arial", 12)).pack()
strength_output = scrolledtext.ScrolledText(app, width=70, height=10)
strength_output.pack(pady=10)

# Generator
tk.Label(app, text="Generated Strong Password:", font=("Arial", 12)).pack()
entry_generated = tk.Entry(app, width=40)
entry_generated.pack(pady=5)

tk.Button(app, text="Generate Password", width=20, command=generate_password).pack(pady=5)

app.mainloop()
