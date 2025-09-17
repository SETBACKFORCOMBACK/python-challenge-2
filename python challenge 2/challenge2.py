import random

print("🎲 Welcome to the Number Guessing Game!")
print("I have picked a number between 1 and 10.")
print("You have only 5 chances to guess it correctly.\n")

# computer picks random number
secret_number = random.randint(1, 10)
max_chances = 5

# loop for 5 chances
for attempt in range(1, max_chances + 1):
    try:
        guess = int(input(f"Attempt {attempt}/{max_chances} - Enter your guess: "))
        
        if guess == secret_number:
            print(f"🎉 Correct! You guessed it in {attempt} tries!")
            break
        elif guess < secret_number:
            print("📉 Too low! Try again.\n")
        else:
            print("📈 Too high! Try again.\n")
    
    except ValueError:
        print("❌ Invalid input! Please enter a number.\n")

else:
    print(f"❌ Out of chances! The correct number was {secret_number}.")
