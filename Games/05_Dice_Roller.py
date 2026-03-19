                                 # DICE ROLLER
import random
import keyboard   # pip install keyboard

print("🎲 Welcome to the Dice Roller Simulator!")
print("Press SPACE to roll the dice, or ESC to quit.")

while True:
    # If SPACE is pressed → roll dice
    if keyboard.is_pressed("space"):
        num_dice = int(input("\nHow many dice do you want to roll? "))
        results = [random.randint(1, 6) for _ in range(num_dice)]
        print("You rolled:", results)

        # Small pause so it doesn’t auto‑trigger multiple times
        keyboard.wait("space", suppress=True)
        

    # If ESC is pressed → exit
    elif keyboard.is_pressed("esc"):
        print("Goodbye! Thanks for playing 🎲")
        