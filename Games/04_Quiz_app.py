                                    # Quiz Application

import random
import os

def load_questions(num_questions=15):
    questions = []
    try:
        base_dir = os.path.dirname(__file__)
        file_path = os.path.join(base_dir, "questions.txt")

        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split("|")

                # Skip invalid lines
                if len(parts) != 6:
                    continue

                questions.append({
                    "question": parts[0].strip(),
                    "options": [p.strip() for p in parts[1:5]],
                    "answer": parts[5].strip().upper()
                })

        # Randomly select questions
        if len(questions) > num_questions:
            questions = random.sample(questions, num_questions)

    except FileNotFoundError:
        print("questions.txt not found!")

    return questions


def run_quiz(questions):
    score = 0

    for i, q in enumerate(questions, start=1):
        print(f"\nQ{i}. {q['question']}")
        print(f"A. {q['options'][0]}")
        print(f"B. {q['options'][1]}")
        print(f"C. {q['options'][2]}")
        print(f"D. {q['options'][3]}")

        answer = input("Your answer (A/B/C/D): ").upper()

        if answer == q["answer"]:
            print("Correct ✅")
            score += 1
        else:
            print(f"Wrong ❌ | Correct Answer: {q['answer']}")

    return score


def show_result(score, total):
    print("\n--- QUIZ RESULT ---")
    print(f"Score: {score}/{total}")

    percent = (score / total) * 100
    print(f"Percentage: {percent:.2f}%")

    if percent >= 80:
        print("Excellent! 🎉")
    elif percent >= 50:
        print("Good 👍")
    else:
        print("Needs Practice 💪")


# -------- MAIN PROGRAM --------
questions = load_questions()

if questions:
    score = run_quiz(questions)
    show_result(score, len(questions))
else:
    print("No questions available.")
