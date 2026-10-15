import time
import tkinter as tk
from tkinter import messagebox, ttk

# Import the original Dice class from dice.py
import dice


class DiceRollerGUI:

    def __init__(self, root):
        self.root = root
        self.root.title("Dice Roller")
        self.root.geometry("400x520")

        self.suspense_mode = tk.BooleanVar(value=False)
        self.advanced_mode = tk.BooleanVar(value=False)

        self.dice_rows = []
        self.modifier_rows = []

        self._create_menu()
        self._create_widgets()

    def _create_menu(self):
        menubar = tk.Menu(self.root)

        # File Menu
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_checkbutton(
            label="Suspense Mode",
            variable=self.suspense_mode,
            command=self.toggle_suspense,
        )
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)
        menubar.add_cascade(label="File", menu=file_menu)

        # Help Menu
        help_menu = tk.Menu(menubar, tearoff=0)
        help_menu.add_command(
            label="Commands Help", command=self.show_help_dialog
        )
        menubar.add_cascade(label="Help", menu=help_menu)

        self.root.config(menu=menubar)

    def _create_widgets(self):
        # Top Frame: Split into DICE (left) and MODIFIER (right)
        top_frame = tk.Frame(self.root, bd=2, relief=tk.SOLID)
        top_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        # Left Column: DICE
        self.dice_frame = tk.Frame(top_frame, bd=1, relief=tk.SOLID)
        self.dice_frame.pack(
            side=tk.LEFT, fill=tk.BOTH, expand=True, padx=2, pady=2
        )

        tk.Label(
            self.dice_frame, text="DICE", font=("Arial", 16, "bold")
        ).pack(pady=5)
        self.dice_container = tk.Frame(self.dice_frame)
        self.dice_container.pack(fill=tk.BOTH, expand=True)

        # Right Column: MODIFIER
        self.modifier_frame = tk.Frame(top_frame, bd=1, relief=tk.SOLID)
        self.modifier_frame.pack(
            side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=2, pady=2
        )

        tk.Label(
            self.modifier_frame, text="MODIFIER", font=("Arial", 16, "bold")
        ).pack(pady=5)
        self.mod_container = tk.Frame(self.modifier_frame)
        self.mod_container.pack(fill=tk.BOTH, expand=True)

        # Default setup matching the design diagram
        self.add_dice_row(default_qty=2, default_sides=6, is_first=True)
        self.add_dice_row(default_qty=3, default_sides=8, is_first=False)

        self.add_mod_row(default_val=6, is_first=True)
        self.add_mod_row(default_val=-3, is_first=False)

        # Bottom Frame: Controls and Output area
        bottom_frame = tk.Frame(self.root, bd=2, relief=tk.SOLID)
        bottom_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        ctrl_frame = tk.Frame(bottom_frame)
        ctrl_frame.pack(fill=tk.X, padx=5, pady=2)

        adv_chk = tk.Checkbutton(
            ctrl_frame, text="Advanced Mode", variable=self.advanced_mode
        )
        adv_chk.pack(side=tk.LEFT)

        roll_btn = tk.Button(
            ctrl_frame,
            text="ROLL DICE",
            command=self.roll_all,
            font=("Arial", 10, "bold"),
            bg="#e1e1e1",
        )
        roll_btn.pack(side=tk.RIGHT, padx=5)

        tk.Label(
            bottom_frame, text="Output", font=("Arial", 10, "bold")
        ).pack(anchor="w", padx=5)

        self.output_text = tk.Text(bottom_frame, height=8, wrap=tk.WORD)
        self.output_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

    def add_dice_row(self, default_qty=1, default_sides=6, is_first=False):
        row_frame = tk.Frame(self.dice_container)
        row_frame.pack(fill=tk.X, pady=4, padx=5)

        if not is_first:
            btn_frame = tk.Frame(row_frame)
            btn_frame.pack(side=tk.LEFT, padx=2)
            tk.Button(
                btn_frame,
                text="+",
                width=1,
                height=1,
                command=lambda: self.add_dice_row(),
            ).pack(side=tk.TOP)
            tk.Button(
                btn_frame,
                text="-",
                width=1,
                height=1,
                command=lambda: self.remove_dice_row(row_info),
            ).pack(side=tk.BOTTOM)
        else:
            tk.Frame(row_frame, width=20).pack(side=tk.LEFT)

        qty_spin = tk.Spinbox(
            row_frame, from_=1, to=100, width=4, font=("Arial", 11)
        )
        qty_spin.delete(0, tk.END)
        qty_spin.insert(0, str(default_qty))
        qty_spin.pack(side=tk.LEFT, padx=2)

        tk.Label(row_frame, text="dice with").pack(side=tk.LEFT, padx=2)

        sides_spin = tk.Spinbox(
            row_frame, from_=1, to=1000, width=4, font=("Arial", 11)
        )
        sides_spin.delete(0, tk.END)
        sides_spin.insert(0, str(default_sides))
        sides_spin.pack(side=tk.LEFT, padx=2)

        tk.Label(row_frame, text="sides").pack(side=tk.LEFT, padx=2)

        row_info = {
            "frame": row_frame,
            "qty": qty_spin,
            "sides": sides_spin,
            "is_first": is_first,
        }
        self.dice_rows.append(row_info)

    def remove_dice_row(self, row_info):
        if len(self.dice_rows) > 1:
            row_info["frame"].destroy()
            self.dice_rows.remove(row_info)

    def add_mod_row(self, default_val=0, is_first=False):
        row_frame = tk.Frame(self.mod_container)
        row_frame.pack(fill=tk.X, pady=4, padx=5)

        if not is_first:
            btn_frame = tk.Frame(row_frame)
            btn_frame.pack(side=tk.LEFT, padx=2)
            tk.Button(
                btn_frame,
                text="+",
                width=1,
                height=1,
                command=lambda: self.add_mod_row(),
            ).pack(side=tk.TOP)
            tk.Button(
                btn_frame,
                text="-",
                width=1,
                height=1,
                command=lambda: self.remove_mod_row(row_info),
            ).pack(side=tk.BOTTOM)
        else:
            tk.Frame(row_frame, width=20).pack(side=tk.LEFT)

        tk.Label(row_frame, text="+").pack(side=tk.LEFT, padx=2)

        mod_spin = tk.Spinbox(
            row_frame, from_=-100, to=100, width=4, font=("Arial", 11)
        )
        mod_spin.delete(0, tk.END)
        mod_spin.insert(0, str(default_val))
        mod_spin.pack(side=tk.LEFT, padx=2)

        tk.Label(row_frame, text="modifier").pack(side=tk.LEFT, padx=2)

        row_info = {"frame": row_frame, "val": mod_spin, "is_first": is_first}
        self.modifier_rows.append(row_info)

    def remove_mod_row(self, row_info):
        if len(self.modifier_rows) > 1:
            row_info["frame"].destroy()
            self.modifier_rows.remove(row_info)

    def toggle_suspense(self):
        msg = (
            "Suspense mode enabled. Prepare to be in suspense ꉂ૮(°□°'˶)ა"
            if self.suspense_mode.get()
            else "Suspense mode disabled. Boring ¬_¬"
        )
        self.log_output(msg + "\n")

    def show_help_dialog(self):
        help_text = (
            "Available commands/features:\n"
            "  • Use '+' / '-' buttons to add or remove dice/modifier inputs.\n"
            "  • Check 'Advanced Mode' for extended details.\n"
            "  • Toggle 'Suspense Mode' in File menu for animated delays.\n"
            "  • Click 'ROLL DICE' to calculate totals."
        )
        messagebox.showinfo("Help", help_text)

    def log_output(self, text):
        self.output_text.insert(tk.END, text)
        self.output_text.see(tk.END)
        self.root.update()

    def play_suspense_animation(self):
        self.log_output("Rolling the dice")
        for _ in range(3):
            time.sleep(0.5)
            self.log_output(".")
        self.log_output("\n")

    def roll_all(self):
        sum_total = 0
        command_parts = []

        try:
            # Process all configured dice sets
            for d in self.dice_rows:
                amount = int(d["qty"].get())
                sides = int(d["sides"].get())

                if amount <= 0 or sides <= 0:
                    continue

                command_parts.append(f"{amount}d{sides}")
                dice = dice.Dice(sides)
                rolls = []

                for _ in range(amount):
                    if self.suspense_mode.get():
                        self.play_suspense_animation()
                    rolls.append(dice.roll())

                subtotal = sum(rolls)
                sum_total += subtotal
                self.log_output(
                    f"Rolling {amount}d{sides}: {rolls} (Total: {subtotal})\n"
                )

            # Process all configured modifiers
            for m in self.modifier_rows:
                mod_val = int(m["val"].get())
                if mod_val != 0:
                    sum_total += mod_val
                    command_parts.append(f"{mod_val:+d}")
                    self.log_output(f"Modifier: {mod_val}\n")

            full_cmd = "+".join(command_parts)
            self.log_output(
                f"Final Total of {full_cmd}: {sum_total}\n" + "-" * 30 + "\n"
            )

        except ValueError:
            self.log_output(
                "Error: Please enter valid integers in all input fields.\n"
            )


if __name__ == "__main__":
    root = tk.Tk()
    app = DiceRollerGUI(root)
    root.mainloop()