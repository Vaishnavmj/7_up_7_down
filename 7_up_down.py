import time
from random import randint 

money = int(input("Welcome! 7 Up 7 Down is a dice game where you bet on numbers greater than, less than, or equal to 7.\nTwo dice are rolled, and if the sum matches your bet, you win!\n\nHow much money do you want to withdraw from your bank? "))

play = input("Do you want to play a game of 7 Up 7 Down? Y or N? ")
while play.lower().startswith('y'):
    number = randint(2, 12)  # Dice sum should be between 2 and 12
    bet = int(input("How much money do you want to bet? "))
    if bet > money:
        print("Insufficient funds! You need an additional", bet - money, "rupees to place the bet. Withdraw more money next time.")
        break

    guess = input("Place your bet:\nA. 7 Up (sum > 7)\nB. 7 Down (sum < 7)\nC. Lucky 7 (sum == 7)\nPress A, B, or C: ")

    print("Rolling dice...")
    time.sleep(3)
    
    # Check guesses
    if guess.lower().startswith('a'):
        if number > 7:
            print("Correct! The dice sum was", number)
            money += bet
        else:
            print("Wrong! The dice sum was", number)
            money -= bet
    elif guess.lower().startswith('b'):
        if number < 7:
            print("Correct! The dice sum was", number)
            money += bet
        else:
            print("Wrong! The dice sum was", number)
            money -= bet
    elif guess.lower().startswith('c'):
        if number == 7:
            print("Correct! The dice sum was", number)
            money += bet * 2
        else:
            print("Wrong! The dice sum was", number)
            money -= bet * 2
    else:
        print("Invalid choice. Please select A, B, or C.")
        continue

    print("You now have", money, "rupees.")
    if money <= 0:
        print("You ran out of money! Time to go to the ATM.")
        money = int(input("How much money do you want to withdraw from your bank? "))
    play = input("Play again? Y or N: ")

print("\nThe game is over.")
print("You finished with", money, "rupees.")
