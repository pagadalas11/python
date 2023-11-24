import random

def roll():
    min_value= 1
    max_value= 6
    roll = random.randint(min_value, max_value)

    return roll
    

while True:    
        players = input("Enter the number of players (2-4):  ")
        if players.isdigit():
            players=int(players)
            if 2 <= players <= 4:
                break
            else:
                print("players should be between 2 to 4 players.")
        else:
            print("Invalid, try again.")
max_score = 50 
player_scores = [0 for _ in range(players)]

while max(player_scores) < max_score:
     for player_index in range(players):
          print("player", player_index + 1, " has just started!")
          current_score = 0
    whi∏le True:
        should_rool = input("would you lke to roll (y)?  ")
            if should_roll != "y":
             break
            value=roll()
               if value == 1:
                  print("your truen is done! cuze your roll 1")
    else: 
     current_score += value
     print("you rolled a", value)

    print("your score is:", current_score)

player_score[player_index] += current_score
print("your total score is:" player_score[player_index])