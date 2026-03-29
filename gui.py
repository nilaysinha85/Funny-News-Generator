import random
import tkinter as tk

# Data
subjects = [
    "Nilay Sinha", "Aryan", "Anand", "Harsh", "Rishi",
    "a Mumbai cat", "a mysterious man", "Shah Rukh Khan",
    "Nirmala Sitharaman", "Virat Kohli", "Prime Minister Modi"
]

actions = [
    "launches", "rides", "drinks", "sees", "jumps on",
    "cancels", "dances", "eats", "declares war",
    "orders", "celebrates"
]

places = [
    "at Red Fort", "in Mumbai", "his watch", "a buffalo",
    "Mercury", "ripe orange juice", "wax", "fresh lemon",
    "on the Moon", "in Pakistan", "for heaven", "IPL win"
]

# Function to generate headline
def generate_headline():
    subject = random.choice(subjects)
    action = random.choice(actions)
    place = random.choice(places)

    headline = f"BREAKING NEWS:\n{subject} {action} {place}"
    label.config(text=headline)

# GUI Window
root = tk.Tk()
root.title("Funny Headline Generator")
root.geometry("400x300")

# Heading
title = tk.Label(root, text="📰 Funny Headline Generator", font=("Arial", 16))
title.pack(pady=10)

# Button
btn = tk.Button(root, text="Generate Headline", command=generate_headline)
btn.pack(pady=10)

# Output Label
label = tk.Label(root, text="", wraplength=350, font=("Arial", 12))
label.pack(pady=20)

# Run app
root.mainloop()