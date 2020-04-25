import random

game_list = [ "Snake", "Water", "Gun" ]

game_NO = 1
total_Games = 10
score_of_user = 0
score_of_robot = 0
no_of_tie_games = 0
no_of_invalid_attempt = 0

print ( "WELCOME TO THE 'SNAKE WATER GUN' GAME'\nYou will get 10 lifes to play the game" )

while game_NO <= total_Games:

    print ( f"\nGame No: {game_NO}\nPlease choose your character.\n's' "
            f"for snake, 'w' for water and 'g' for gun." )

    system_choise = random.choice ( game_list )

    user_choise = input ( "\n>>> " )

    if user_choise != 's' and user_choise != 'w' and user_choise != 'g':
        print ( "Invalid input. Please choose correctly" )
        game_NO += 1
        no_of_invalid_attempt += 1
        continue

    elif user_choise == 's' and system_choise == 'Snake' \
            or user_choise == 'w' and system_choise == 'Water' \
            or user_choise == 'g' and system_choise == 'Gun':
        print ( "Game Tied..!!!" )
        no_of_tie_games += 1
        game_NO += 1

    elif user_choise == 's' and system_choise == 'Gun' \
            or user_choise == 'g' and system_choise == 'Water' \
            or user_choise == 'w' and system_choise == 'Snake':
        print ( "System Won the game" )
        score_of_robot += 1
        game_NO += 1

    elif user_choise == 's' and system_choise == 'Water' \
            or user_choise == 'g' and system_choise == 'Snake' \
            or user_choise == 'w' and system_choise == 'Gun':
        print ( "Congratulations!! You Won the game" )
        score_of_user += 1
        game_NO += 1

print ( f"\n\n{'*' * 30}\nThank for playing game with us\n{'*' * 30}\n"
        f"Check your result below:\nSystem Won: {score_of_robot}\n"
        f"You Won: {score_of_user}\nTotal Tie: {no_of_tie_games}\n"
        f"Invalid Games: {no_of_invalid_attempt}\n{'*' * 30}" )
