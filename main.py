import tkinter as tk
from card import Card # Import the custom card widget.
from goal_panel import GoalPanel # Import the custom goal panel widget.


"""
TO DO: Fix goal panel not appearing.
"""


# Root element.
root = tk.Tk()
root.title("Twenty One") # Set title.
root.resizable(False, False) # Make the window unresizable.



# Main container. Might be able to get rid of this and just use the root widget.
main = tk.Frame(root)
main.pack(padx=20,pady=20)
main.grid_columnconfigure(0,weight=1)
main.grid_columnconfigure(1,weight=11)


# Goal container label.
goal_label = tk.Label(main, text="GOAL", font=("Helvetica", 20))
goal_label.grid(row=0, column=0, pady=(0,4))

# Goal panel.
goal_panel = GoalPanel(main)
goal_panel.grid(row=1, column=0)

# Cards container.
cards_container = tk.Frame(main, pady=4)
cards_container.grid(row=1, column=1)

# Cards container label.
cards_label = tk.Label(main, text="CARDS", font=("Helvetica", 20))
cards_label.grid(row=0, column=1, columnspan=11, pady=(4,0))


# Instantiate list to hold cards.
cards = []

# Create cards 1-11.
for i in range(1,12):
    card = Card(cards_container, i, "white")
    cards.append(card)
    card.grid(row=1, column=i-1, padx=4, pady=4)
    



root.mainloop()