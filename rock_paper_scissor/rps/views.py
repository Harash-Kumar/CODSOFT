import random
from django.shortcuts import render

def rps_game(request):
    user_choice = ""
    computer_choice = ""
    result = ""

    if request.method == "POST":
        user_choice = request.POST.get("choice")

        choices = ["rock", "paper", "scissors"]
        computer_choice = random.choice(choices)

        # Game logic
        if user_choice == computer_choice:
            result = "It's a Tie!"
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            result = "🎉 You Win!"
        else:
            result = "😢 Computer Wins!"

    return render(request, "rps/game.html", {
        "user_choice": user_choice,
        "computer_choice": computer_choice,
        "result": result
    })
