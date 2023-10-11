import tkinter as tk


def update_total(total_label, total):
    total_label.config(text="Total: {}".format(total))


class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.total = 0
        self.current_number = ""
        self.entry_var = tk.StringVar()
        self.create_widgets()

    def create_widgets(self):
        # Label to display the total
        total_label = tk.Label(self, text="Total: 0", font=('Arial', 14))
        total_label.grid(row=0, column=0, columnspan=3, sticky='nsew')

        # Entry field for user input
        entry = tk.Entry(self, textvariable=self.entry_var,
                         font=('Arial', 14), justify='right')
        entry.grid(row=1, column=0, columnspan=3, sticky='nsew')
        entry.insert(0, "0")
        entry.bind("<FocusIn>", self.clear_placeholder)

        # Define addition and subtraction event handlers
        def add():
            try:
                value = int(self.entry_var.get())
                self.total += value
                self.current_number = ""
                self.entry_var.set("0")
                update_total(total_label, self.total)
            except ValueError:
                self.entry_var.set("Invalid Input")

        def subtract():
            try:
                value = int(self.entry_var.get())
                self.total -= value
                self.current_number = ""
                self.entry_var.set("0")
                update_total(total_label, self.total)
            except ValueError:
                self.entry_var.set("Invalid Input")

        def reset():
            self.total = 0
            self.current_number = ""
            self.entry_var.set("0")
            update_total(total_label, self.total)

        # Add buttons to the grid
        button_add = tk.Button(self, text='+', padx=20, pady=20, command=add)
        button_add.grid(row=2, column=0, sticky='nsew')

        button_subtract = tk.Button(
            self, text='-', padx=20, pady=20, command=subtract)
        button_subtract.grid(row=2, column=1, sticky='nsew')

        # Reset button
        reset_button = tk.Button(
            self, text='Reset', padx=20, pady=20, command=reset)
        reset_button.grid(row=2, column=2, sticky='nsew')

        # Configure grid layout to expand properly
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

        # Adjust column weights to make functional part take 2/3rd of the width
        self.grid_columnconfigure(3, weight=2)

    def clear_placeholder(self, event):
        if self.entry_var.get() == "0":
            self.entry_var.set("")


if __name__ == "__main__":
    app = Calculator()
    app.title("Simple Calculator")
    app.geometry("400x200")  # Set initial window size
    app.mainloop()
