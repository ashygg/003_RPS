import random

rps_choices = ("rock", "paper", "scissors")
selection = (random.choice(rps_choices))

intro = """Welcome to a simple game of Rock, Paper, Scissors!
I assume you know the rules, so let's play!
"""
print(intro)

total_score = 0
print("""What is your choice?
Rock... 
Paper... 
Scissors... 
Shoot!""")

ans = input("I choose: ")

results = (f"I chose {selection} and you chose {ans}!")
print(results)

if ans == "rock":
    if selection == "scissors":
        total_score += 1
elif ans == "rock":
    if selection == "paper":
        total_score += 0
elif ans == "paper":
    if selection == "rock":
        total_score += 1
elif ans == "paper":
    if selection == "scissors":
        total_score += 0
elif ans == "scissors":
    if selection == "paper":
        total_score += 1
elif ans == "scissors":
    if selection == "rock":
        total_score += 0

if total_score == 1:
    print("You won! Congrats!")
elif total_score == 0:
    print("I win! Better luck next time!")


