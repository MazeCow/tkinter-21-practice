import tkinter as tk

class Card(tk.Frame):
    def __init__(self, parent, value: int, bg_color:str = "white"):
        # Run the constructor.
        super().__init__(master=parent, bg=bg_color, highlightthickness=2, highlightbackground="black", padx=3, pady=3, width=100, height=140)
        
        # Set up grid configuration for the main widget.
        self.rowconfigure(0, weight=1)
        self.columnconfigure((0, 1), weight=1)

        # Add a label.
        self._num_label = tk.Label(self, text=str(value), font=("Helvetica", 40), bg=bg_color)
        self._num_label.grid(row=0, column=0)
        
        # Set properties.
        self.value: int = value
        self.bg_color: str = bg_color
        
        # Disable grid propogation.
        self.grid_propagate(False)
        
        # Create a frame for player buttons.
        player_buttons = tk.Frame(self)
        player_buttons.grid(row=1, column=0, sticky="nsew")  # Place the frame.
        
        # Create ownership buttons.
        btn_user = tk.Button(player_buttons, text="U", width=3, bg=bg_color, command=lambda:self.btn_click(btn_user))
        btn_none = tk.Button(player_buttons, text="N", width=3, bg=bg_color, command=lambda:self.btn_click(btn_none))
        btn_enemy = tk.Button(player_buttons, text="E", width=3, bg=bg_color, command=lambda:self.btn_click(btn_enemy))
        
        # Place the buttons horizontally in a grid.
        btn_user.grid(row=0, column=0)
        btn_none.grid(row=0, column=1)
        btn_enemy.grid(row=0, column=2)
        
    def update_bg_color(self) -> None:
        # All widgets that need their background color changed.
        colored_widgets:list[tk.Widget] = [self, self._num_label] 
        
        # Iterate through all the widgets and change their background colors.
        for widget in colored_widgets:
            widget.configure(bg=self.bg_color)
            
    @property
    def bg_color(self) -> str:
        return self._bg_color
            
    @bg_color.setter
    def bg_color(self, bg_color: str) -> None:
        self._bg_color = bg_color
        self.update_bg_color()
        
            
    def btn_click(self, event: tk.Button) -> None:
        # Get the text of the button.
        btn_text = event.cget("text")
        
        # Background color dictionary mapping button text to colors.
        bg_colors = {
            "U": "green",
            "N": "white",
            "E": "red"
        }
        
        # Get the background color that matches the button pressed.
        bg_color = bg_colors[btn_text]
        
        # Update background color property.
        self.bg_color = bg_color
        