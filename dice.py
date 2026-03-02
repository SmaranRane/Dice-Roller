import random
import time

class Dice:
    def __init__(self, sides):
        self.sides = sides

    def roll(self):
        self.randomize(self.sides)
        return random.randint(1, self.sides)
    
    def randomize(self, sides):
        start_num = random.randint(1, sides)
        aggression = random.randint(1, 100)
        bounce = random.randint(1, 10)
        low = sides+start_num
        high = sides*start_num*aggression*bounce
        random.seed(random.randint(low, high))
    
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
        print("Suspense mode enabled. Prepare to be in suspense :3")
        suspense_mode = True
    else:
        print("Suspense mode disabled. Boring ahh (¬_¬)")
    while True:
        try:
            command = input("Enter a command (type 'help' for list of commands): ")
            if command == "help":
                print("Available commands:")
                print("  help - Show this help message")
                print("  suspense - Toggle suspense mode on/off")
                print("  d<sides> - Roll a die with the specified number of sides")
                print("  +/-<number> - Add or subtract a modifier to the last roll (e.g., +2 or -1)")
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
            elif command.startswith("+") or command.startswith("-"):
                modifier = int(command)
                new_roll = last_roll + modifier
                print(f"Adding {modifier} to {last_roll}: {new_roll}")
            elif command == "quit":
                print("Exiting the dice roller. Goodbye!")
                break
        except ValueError:
            print("Please enter valid integers for the number of dice and sides.")
        except KeyboardInterrupt:
            print("\nExiting the dice roller. Goodbye!")
            break