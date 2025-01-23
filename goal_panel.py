import tkinter as tk


class GoalPanel(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, width=300)
        
        # Set properties.
        self.goal = 21
        
        # Set grid weights.
        self.rowconfigure((0, 1), weight=1)
        self.columnconfigure((0, 1), weight=1)
        
        # Create goal buttons.
        btn_17 = tk.Button(self, text="17", font=("Helvetica", 20), bg="white", command=lambda:self.click_btn(btn_17))
        btn_21 = tk.Button(self, text="21", font=("Helvetica", 20), bg="black", fg="white", command=lambda:self.click_btn(btn_21))
        btn_24 = tk.Button(self, text="24", font=("Helvetica", 20), bg="white", command=lambda:self.click_btn(btn_24))
        btn_27 = tk.Button(self, text="27", font=("Helvetica", 20), bg="white", command=lambda:self.click_btn(btn_27))

        # Place the buttons in the goal buttons container.
        btn_17.grid(column=0, row=0, padx=4, pady=4)
        btn_21.grid(column=1, row=0, padx=4, pady=4)
        btn_24.grid(column=0, row=1, padx=4, pady=4)
        btn_27.grid(column=1, row=1, padx=4, pady=4)
        
        # A dictionary mapping values to buttons.
        self.buttons = {
            "17": btn_17,
            "21": btn_21,
            "24": btn_24,
            "27": btn_27
        }
        
        
    def click_btn(self, event: tk.Button) -> None:
        # Reset all button colors.
        for key in self.buttons:
            self.buttons[key].configure(bg="white", fg="black")
            
        # Set the clicked button's bg color to gray.
        event.configure(bg="black", fg="white")
        
        # Get the value of the clicked button.
        value = event.cget("text")
        
        # Set the goal property.
        self.goal = int(value)

