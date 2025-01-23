import tkinter as tk


class GoalPanel(tk.Frame):
    def __init__(self, parent):
        super().__init__(master=parent, width=300)
        
        # Set properties.
        self.goal = 21

        # Disable grid propogation.
        self.grid_propagate(False)
        
        self.rowconfigure((0,1), weight=1)
        self.columnconfigure((0, 1), weight=1)
        
        # Buttons dictionary mapping a button value to a button.
        self.buttons = {
            "17": tk.Button(self, text=17, font=("Helvetica", 20), bg="white", command=lambda:self.click_btn(self.buttons["17"])),
            "21": tk.Button(self, text=21, font=("Helvetica", 20), bg="white", command=lambda:self.click_btn(self.buttons["21"])),
            "24": tk.Button(self, text=24, font=("Helvetica", 20), bg="white", command=lambda:self.click_btn(self.buttons["24"])),
            "27": tk.Button(self, text=27, font=("Helvetica", 20), bg="white", command=lambda:self.click_btn(self.buttons["27"]))
        }

        # Place the buttons in the goal buttons container.
        self.buttons["17"].grid(column=0, row=0, padx=4, pady=4)
        self.buttons["21"].grid(column=1, row=0, padx=4, pady=4)
        self.buttons["24"].grid(column=0, row=1, padx=4, pady=4)
        self.buttons["27"].grid(column=1, row=1, padx=4, pady=4)
        
        
        
    def click_btn(self, event: tk.Button) -> None:
        # Reset all button colors.
        for key in self.buttons:
            self.buttons[key].configure(bg="white")
            
        # Set the clicked button's bg color to gray.
        event.configure(bg="gray")
        
        # Get the value of the clicked button.
        value = event.cget("text")
        
        # Set the goal property.
        self.goal = int(value)

