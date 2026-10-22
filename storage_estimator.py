# Added Extreme difficulty mode feature
import random


def get_max_number():
    print(
        "Select Difficulty: 1. Easy (1-20)  2. Medium (1-50)  3. Hard (1-100)  4. Extreme (1-500)"
    )
    choice = input("Enter choice (1-4): ").strip()
    if choice == "1":
        return 20
    elif choice == "3":
        return 100
    elif choice == "4":
        return 500
    return 50


def play_round(best_score):
    max_num = get_max_number()
    secret = random.randint(1, max_num)
    attempts = 0
    print(f"\nI am thinking of a number between 1 and {max_num}. Guess it!")

    while True:
        try:
            guess = int(input("Your guess: "))
            attempts += 1
            if guess < secret:
                print("Too low! Try higher.")
            elif guess > secret:
                print("Too high! Try lower.")
            else:
                print(f"Correct! You got it in {attempts} attempts.")
                if best_score is None or attempts < best_score:
                    print(" New High Score!")
                    return attempts
                return best_score
        except ValueError:
            print("Please enter a valid integer.")


def main():
    best_score = None
    print("=== WELCOME TO THE NUMBER GUESSING GAME ===")

    while True:
        best_score = play_round(best_score)
        print(f"Best Score so far: {best_score} attempts")
        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing! Goodbye.")
            break


if __name__ == "__main__":
    main()
