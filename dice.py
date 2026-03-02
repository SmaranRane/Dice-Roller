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

# Add modifier

if __name__ == "__main__":
    suspense_mode = False
    if input("Enable suspense mode? (y/n): ").lower() == 'y':
        suspense_mode = True
    while True:
        try:
            sides_n = int(input("Enter the number of sides on each die: "))
            
            dice = Dice(sides_n)
            if suspense_mode:
                suspense()
            print(f"Rolling a d{sides_n}: {dice.roll()}")
        except ValueError:
            print("Please enter valid integers for the number of dice and sides.")
        except KeyboardInterrupt:
            print("\nExiting the dice roller. Goodbye!")
            break

