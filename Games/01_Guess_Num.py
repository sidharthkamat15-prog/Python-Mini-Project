                                      # 03_Guess_Num.py

import random
import time

# 🎬 Game Introduction
def show_intro():
    intro = '''
🎉 Welcome to the Number Guessing Challenge!

           FROM [ 1 to 100 ] 

🎯 Your goal: Guess the secret number chosen by the computer.

📊 There are 3 levels:
- 🟢 Easy: Number is between 1 and 20
- 🟡 Medium: Number is between 20 and 50
- 🔴 Hard: Number is between 50 and 100

🎲 You get 5 chances to guess 5 different numbers:
- 🟢 2 Easy level guesses
- 🟡 2 Medium level guesses
- 🔴 1 Hard level guess

🏆 If you guess it exactly, you win!
📉 If not, your score depends on how close your guesses were.

💡 The closer your guess is to the secret number, the higher your score.

Ready to play?
'''
    for line in intro.strip().split('\n'):
        print(line)
        time.sleep(0.4)

# 🚀 Start Game 
def start_game():
    while True:
        user_input = input("\n👉 Type 'start' to begin the game or 'quit' to exit: ").strip().lower()
        if user_input == "start":
            print("\n🎮 Great! Let's begin your challenge...")
            time.sleep(0.8)
            run_game()
            break
        elif user_input == "quit":
            print("\n👋 No worries! Come back anytime for a challenge.")
            break
        else:
            print("⚠️ Invalid input. Please type 'start' or 'quit'.")

# 🎯 Play a Level
def play_level(level_name, num_guesses, low, high):
    guesses = []
    secrets = []
    gaps = []

    print(f"\n🔹 {level_name} Level: Guess {num_guesses} number(s) between {low} and {high}")
    time.sleep(1)

    for i in range(num_guesses):
        while True:
            try:
                guess = int(input(f"👉 {level_name} Guess {i+1}: "))
                if low <= guess <= high:
                    break
                else:
                    print(f"⚠️ Please enter a number between {low} and {high}.")
            except ValueError:
                print("❌ Invalid input. Please enter a number.")

        secret = random.randint(low, high)
        gap = abs(secret - guess)

        guesses.append(guess)
        secrets.append(secret)
        gaps.append(gap)

        print(f"🤖 Computer's number: {secret}")
        print(f"📏 Gap: {gap}")
        time.sleep(1)

        if gap == 0:
            print("\n🏆🌟🌟🌟 LEGENDARY! 🌟🌟🌟🏆")
            print("🎉 You guessed the number perfectly!")
            print("🧠 You're a mind reader! A true champion!")
            print("🎮 The game bows to your greatness.")
            print("🚀 No need to continue — you've already won!")
            return guesses, secrets, gaps, True

    return guesses, secrets, gaps, False

# 📊 Show Summary
def show_summary(level_name, guesses, secrets, gaps):
    print(f"\n📊 {level_name} Level Summary")
    print(f"🧠 Your guesses: {guesses}")
    print(f"🤖 Computer's numbers: {secrets}")
    print(f"📏 Gaps: {gaps}")
    closest = min(gaps) if gaps else 0
    print(f"🎯 Closest guess gap: {closest}")
    return closest

# 🎖️ Final Score Rating (1–10 scale)
def game_rating(score):
    if score == 0:
        rating = 10
        title = "🏆 LEGENDARY"
        message = "🎯 Perfect guesses! You're a mind reader!"
    elif score <= 10:
        rating = 9
        title = "🌟 Master Guesser"
        message = "💫 Incredible accuracy! You're almost legendary!"
    elif score <= 15:
        rating = 8
        title = "🔥 Sharp Shooter"
        message = "🎯 Great instincts! You’re on fire!"
    elif score <= 20:
        rating = 7
        title = "👍 Skilled Player"
        message = "👏 Solid performance! Keep it up!"
    elif score <= 25:
        rating = 6
        title = "✅ Getting There"
        message = "🙂 You're improving fast. Stay sharp!"
    elif score <= 30:
        rating = 5
        title = "🙂 Not Bad"
        message = "😊 You're learning. Keep practicing!"
    elif score <= 35:
        rating = 4
        title = "🔁 Try Again"
        message = "🔄 You're getting closer. Don't give up!"
    elif score <= 40:
        rating = 3
        title = "📚 Keep Practicing"
        message = "📖 Every guess teaches you something new!"
    elif score <= 45:
        rating = 2
        title = "🌀 Warming Up"
        message = "🧠 You're just getting started. Try again!"
    else:
        rating = 1
        title = "💤 Needs More Focus"
        message = "😴 That was a tough round. Come back stronger!"

    print(f"\n🎖️ Final Score Rating: {rating}/10")
    print(f"{title} — {message}")

# 📝 Ask for Player Feedback
def ask_for_feedback():
    print("\n📝 We'd love to hear what you think about the game!")
    print("👉 On a scale of 1 to 10, how much did you enjoy it?")
    
    while True:
        try:
            rating = int(input("⭐ Your rating (1 = not fun, 10 = amazing): "))
            if 1 <= rating <= 10:
                break
            else:
                print("⚠️ Please enter a number between 1 and 10.")
        except ValueError:
            print("❌ That's not a number. Try again!")

    if rating == 10:
        print("🎉 Wow! We're thrilled you loved it! You're awesome!")
    elif rating >= 8:
        print("😊 So glad you had fun! Thanks for playing!")
    elif rating >= 5:
        print("👍 Thanks! We’ll keep improving to make it even better.")
    elif rating >= 3:
        print("😅 Sorry it wasn’t perfect. We’d love to hear how we can improve.")
    else:
        print("😔 Oh no! We’ll work harder to make it more fun next time.")

    print("\n💬 If you have any ideas or suggestions, feel free to share them!")

# 🧠 Main Game Logic
def run_game():
    legendary = False
    easy_closest = medium_closest = hard_closest = 0

    for level in [("🟢 Easy", 2, 1, 20), ("🟡 Medium", 2, 20, 50), ("🔴 Hard", 1, 50, 100)]:
        name, count, low, high = level
        guesses, secrets, gaps, legendary = play_level(name, count, low, high)
        if legendary:
            game_rating(0)
            ask_for_feedback()
            return
        if name == "🟢 Easy":
            easy_closest = show_summary(name, guesses, secrets, gaps)
        elif name == "🟡 Medium":
            medium_closest = show_summary(name, guesses, secrets, gaps)
        elif name == "🔴 Hard":
            hard_closest = show_summary(name, guesses, secrets, gaps)

    total_closest = easy_closest + medium_closest + hard_closest
    print(f"\n📈 Total of closest gaps: {total_closest}")
    time.sleep(1)
    game_rating(total_closest)
    ask_for_feedback()

# Explain in simple way

# 🟢 Running the all the function
show_intro()
start_game()

