import random
import time
import math

# add multi amount roll (e.g. 3d6), multi type roll (e.g. d20 d8), and modifiers (e.g. 2d8+3) support

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

if __name__ != "__main__":
    suspense_mode = False
    last_roll = 0
    if input("Enable suspense mode? (y/n): ").lower() == 'y':
        print("Suspense mode enabled. Prepare to be in suspense >:3")
        suspense_mode = True
    else:
        print("Suspense mode disabled. Boring (¬_¬)")
    while True:
        try:
            command = input("Enter a command (type 'help' for list of commands): ")
            if command == "help":
                print("Available commands:")
                print("  help - Show this help message")
                print("  suspense - Toggle suspense mode on/off")
                print("  d<sides> - Roll a die with the specified number of sides")
                print("  quit - Exit the program")
            elif command == "suspense":
                suspense_mode = not suspense_mode
                print(f"Suspense mode is now {'enabled' if suspense_mode else 'disabled'}")
            elif command.startswith("d"):
                sides_n = int(command[1:])
                dice = Dice(sides_n)
                if suspense_mode:
                    suspense()
                last_roll = dice.roll()
                print(f"Rolling a d{sides_n}: {last_roll}")
            elif command == "quit":
                print("Exiting the dice roller. Goodbye!")
                break
        except ValueError:
            print("Please enter valid integers for the number of dice and sides.")
        except KeyboardInterrupt:
            print("\nExiting the dice roller. Goodbye!")
            break