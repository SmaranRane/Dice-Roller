import random
import time
import math

class Dice:
    def __init__(self, sides):
        self.sides = sides
        self.last_roll = 1

    def roll(self):
        #start_num = self.last_roll % self.sides + 1
        aggression = random.random()
        if aggression <= 0.001:
            aggression = 0.001
        max_bounce = int(30.45936 * math.log(self.sides) * aggression)
        if max_bounce < 1:
            max_bounce = 1
        bounce = random.randint(1, max_bounce)
        for _ in range(bounce):
            rolled_num = random.randint(1, self.sides)
        return rolled_num


def suspense():
    print("Rolling the dice", end="", flush=True)
    for _ in range(3):
        print(".", end="", flush=True)
        time.sleep(1)
    print()

if __name__ == "__main__":
    suspense_mode = False
    last_roll = 0
    if input("Enable suspense mode? (y/n): ").lower() == 'y':
        print("Suspense mode enabled. Prepare to be in suspense 😱")
        suspense_mode = True
    elif input("Enable suspense mode? (y/n): ").lower() == 'n':
        print("Suspense mode disabled. Boring 🙄")
    else:
        print("Invalid input 🤨. Suspense mode disabled by default.")
    while True:
        try:
            command = input("Enter a command: ")
            if command == "help":
                print("Available commands:")
                print("  help - Show this help message")
                print("  suspense - Toggle suspense mode on/off")
                print("  <num>d<sides> [+<modifier> / +<num>d<sides>] - Roll a specified number of dice with the specified number of sides. You can also add modifiers or roll multiple types of dice (e.g. 2d6+3 or d20+d8).")
                print("  quit - Exit the program")
            elif command == "suspense":
                suspense_mode = not suspense_mode
                print(f"Suspense mode is now {'enabled' if suspense_mode else 'disabled'}")
            elif command.__contains__("d"):
                dice_parts = command.split("+")
                sum_total = 0
                for dice_part in dice_parts:
                    if "d" in dice_part:
                        try:
                            amount, sides = dice_part.split("d")
                            amount = int(amount) if amount else 1
                            sides = int(sides)
                            dice = Dice(sides)
                            rolls = []
                            for _ in range(amount):
                                if suspense_mode:
                                    suspense()
                                rolls.append(dice.roll())
                            sum_total += sum(rolls)
                            print(f"Rolling {amount}d{sides}: {rolls} (Total: {sum(rolls)})")
                        except ValueError:
                            print(f"Invalid dice format: {dice_part}")
                    else:
                        try:
                            modifier = int(dice_part)
                            sum_total += modifier
                            print(f"Modifier: {modifier}")
                        except ValueError:
                            print(f"Invalid modifier format: {dice_part}")
                print(f"Final Total of {command}: {sum_total}")
            elif command == "quit":
                print("Exiting the dice roller. Goodbye!")
                break
            else:
                print("Unknown command (type 'help' for list of commands)")
        except ValueError:
            print("Please enter valid integers for the number of dice and sides.")
        except KeyboardInterrupt:
            print("\nExiting the dice roller. Goodbye!")
            break