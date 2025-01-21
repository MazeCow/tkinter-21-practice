import tkinter
from tkinter import ttk
from tkinter import ttk
import sv_ttk


# This is where the magic happens


root = tkinter.Tk()
root.title("Tkinter Practice #1")


class MyWidget(ttk.Frame):
    def __init__(self, parent, label_text):
        super().__init__(master=parent)
        
        # Set up grid configuration for the main widget.
        self.rowconfigure(0, weight=1)
        self.columnconfigure((0, 1), weight=1)

        # Add a label.
        ttk.Label(self, text=label_text, font=("Helvetica", 24)).grid(row=0, column=0)
        
        # Create a frame for player buttons.
        player_buttons = ttk.Frame(self)
        player_buttons.grid(row=1, column=0, sticky="nsew")  # Place the frame.
        
        # Configure columns within the player buttons frame.
        player_buttons.columnconfigure(0, weight=1)
        player_buttons.columnconfigure(1, weight=1)
        player_buttons.columnconfigure(2, weight=1)
        
        # Add buttons to the player buttons frame.
        btn_user = ttk.Button(player_buttons, text="U", width=3)
        btn_user.grid(row=0, column=0)
        
        btn_none = ttk.Button(player_buttons, text="N", width=3)
        btn_none.grid(row=0, column=1)
        
        btn_enemy = ttk.Button(player_buttons, text="E", width=3)
        btn_enemy.grid(row=0, column=2)

        # Pack the main widget.
        self.pack()

        
        
        

# button = ttk.Button(root, text="Click me!")
# button.pack()



m = MyWidget(root, "1")
m.pack()


root.mainloop()