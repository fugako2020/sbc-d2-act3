from random import randint
fold=1
unfold=2

p1 = input("fold unfold")

c1 = randint(1, 2)
c2 = randint(1, 2)
c3 = randint(1, 2)

print()


def game_result(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif player_choice == "fold" and computer_choice == "unfold":
        return "Player wins!"
    elif player_choice == "unfold" and computer_choice == "fold":
        return "Computer wins!"


player_choice = input("Enter 'fold' or 'unfold': ").strip().lower()


while player_choice not in ["fold", "unfold"]:
    print("Invalid choice. Please enter 'fold' or 'unfold'.")
    player_choice = input("Enter 'fold' or 'unfold': ").strip().lower()


computer_choice = "fold" if randint(1, 2) == 1 else "unfold"

result = game_result(player_choice, computer_choice)
print(f"Player chose: {player_choice}")
print(f"Computer chose: {computer_choice}")
print(result)