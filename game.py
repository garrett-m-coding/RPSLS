from human import Human
from ai import Artificial

class Game:
    def __init__(self):
        self.contestants = []
        pass

    def welcome_rules(self):
        print("Welcome to Rock, Paper, Scissors, Lizard, Spock (RPSLS)!\n"
        "\n"
        "The rules of RPSLS is:\n"
        "\n"
        "Rock crushes Scissors\n"
        "Scissors cuts Paper\n"
        "Paper covers Rock\n"
        "Rock crushes Lizard\n"
        "Lizard poisons Spock\n"
        "Spock smashes Scissors\n"
        "Scissors decapitates Lizard\n"
        "Lizard eats Paper\n"
        "Paper disproves Spock\n"
        "Spock vaporizes Rock\n"
        "\n"
        "Let's play!")
    
    def game_mode(self):
        game_choice = (input("How will you be playing?\n"
        "Type (1) for single player\n"
        "Type (2) for multiplayer  "))
        if game_choice == "1":
            ai_player = Artificial()
            self.contestants.append(ai_player)
            human_player1 = Human()
            self.contestants.append(human_player1)
            print("\n")
            self.ai_game()
        elif game_choice == "2":
            human_player1 = Human()
            self.contestants.append(human_player1)
            human_player2 = Human()
            self.contestants.append(human_player2)
            self.human_game()
        else:
            print("\n")
            self.game_mode()
        pass

    def ai_game(self):
        human_winner_counter = 0
        ai_winner_counter = 0

        human_round1 = self.human_turn(1)
        ai_round1 = self.ai_turn()
        round_one_winner = self.find_round_winner(human_round1, ai_round1)
        print("\n")
        print(f'{self.contestants[1].name} chose {human_round1} and\n{self.contestants[0].name} chose {ai_round1}')
        print(f'{round_one_winner} wins round 1')
        print("\n")
        if round_one_winner == self.contestants[1].name:
            human_winner_counter += 1
        elif round_one_winner == self.contestants[0].name:
            ai_winner_counter += 1
        
        human_round2 = self.human_turn(1)
        ai_round2 = self.ai_turn()
        round_two_winner = self.find_round_winner(human_round2, ai_round2)
        print("\n")
        print(f'{self.contestants[1].name} chose {human_round2} and\n{self.contestants[0].name} chose {ai_round2}')
        print(f'{round_two_winner} wins round 2')
        print("\n")
        if round_two_winner == self.contestants[1].name:
            human_winner_counter += 1
        elif round_two_winner == self.contestants[0].name:
            ai_winner_counter += 1
        if human_winner_counter == 2:
            print(f'{self.contestants[1].name} wins the game!!!\n')
            self.ask_new_game()
        elif ai_winner_counter == 2:
            print(f'{self.contestants[0].name} wins the game!!!\n''Better luck next time! ¯\_(ツ)_/¯\n')
            self.ask_new_game()
        elif human_winner_counter < 2 and ai_winner_counter < 2:
            human_round3 = self.human_turn(1)
            ai_round3 = self.ai_turn()
            round_three_winner = self.find_round_winner(human_round3, ai_round3)
            print("\n")
            print(f'{self.contestants[1].name} chose {human_round3} and\n{self.contestants[0].name} chose {ai_round3}')
            print(f'{round_three_winner} wins round 3')
            print("\n")
            if round_three_winner == self.contestants[1].name:
                human_winner_counter += 1
            elif round_three_winner == self.contestants[0].name:
                ai_winner_counter += 1
            
            if human_winner_counter >= 2:
                print(f'{self.contestants[1].name} wins the game!!!\n')
                self.ask_new_game()
            elif ai_winner_counter >= 2:
                print(f'{self.contestants[0].name} wins the game!!!\n''Better luck next time! ¯\_(ツ)_/¯\n')
                self.ask_new_game()
            elif human_winner_counter == 1 and ai_winner_counter == 0:
                print(f'{self.contestants[1].name} wins the game!!!\n')
                self.ask_new_game() 
            elif ai_winner_counter == 1 and human_winner_counter == 0:
                print(f'{self.contestants[0].name} wins the game!!!\n''Better luck next time! ¯\_(ツ)_/¯\n')
                self.ask_new_game()
            elif human_winner_counter == ai_winner_counter:
                print("How does it feel to tie and win nothing?! Sucks right?\n""Play again because if you ain't first, you're last!\n")
                self.ask_new_game()

    def ai_turn(self):
        ai_player_choice = self.contestants[0].choose_gesture()
        return ai_player_choice

    def human_turn(self, index_number):
        self.contestants[index_number].choose_gesture()
        human1_choice = self.valid_answer()
        return human1_choice

    def human_game(self):
        human1_winner_counter = 0
        human2_winner_counter = 0

        human1_round1 = self.human_turn(1)
        human2_round1 = self.human_turn(0)
        round_one_winner = self.find_round_winner(human1_round1, human2_round1)
        print("\n")
        print(f'{self.contestants[1].name} chose {human1_round1} and\n{self.contestants[0].name} chose {human2_round1}')
        print(f'{round_one_winner} wins round 1!')
        print("\n")
        if round_one_winner == self.contestants[1].name:
            human1_winner_counter += 1
        elif round_one_winner == self.contestants[0].name:
            human2_winner_counter += 1
        
        human1_round2 = self.human_turn(1)
        human2_round2 = self.human_turn(0)
        round_two_winner = self.find_round_winner(human1_round2, human2_round2)
        print("\n")
        print(f'{self.contestants[1].name} chose {human1_round2} and\n{self.contestants[0].name} chose {human2_round2}')
        print(f'{round_two_winner} wins round 2!')
        print("\n")
        if round_two_winner == self.contestants[1].name:
            human1_winner_counter += 1
        elif round_two_winner == self.contestants[0].name:
            human2_winner_counter += 1
        if human1_winner_counter == 2:
            print(f'{self.contestants[1].name} wins the game!!!\n')
            self.ask_new_game()
        elif human2_winner_counter == 2:
            print(f'{self.contestants[0].name} wins the game!!!\n')
            self.ask_new_game()
        elif human1_winner_counter < 2 and human2_winner_counter < 2:
            human1_round3 = self.human_turn(1)
            human2_round3 = self.human_turn(0)
            round_three_winner = self.find_round_winner(human1_round3, human2_round3)
            print("\n")
            print(f'{self.contestants[1].name} chose {human1_round3} and\n{self.contestants[0].name} chose {human2_round3}')
            print(f'{round_three_winner} wins round 3!')
            print("\n")
            if round_three_winner == self.contestants[1].name:
                human1_winner_counter += 1
            elif round_three_winner == self.contestants[0].name:
                human2_winner_counter += 1
            
            if human1_winner_counter >= 2:
                print(f'{self.contestants[1].name} wins the game!!!\n')
                self.ask_new_game()
            elif human2_winner_counter >= 2:
                print(f'{self.contestants[0].name} wins the game!!!\n')
                self.ask_new_game()
            elif human1_winner_counter == 1 and human2_winner_counter == 0:
                print(f'{self.contestants[1].name} wins the game!!!\n')
                self.ask_new_game() 
            elif human2_winner_counter == 1 and human1_winner_counter == 0:
                print(f'{self.contestants[0].name} wins the game!!!\n')
                self.ask_new_game()
            elif human1_winner_counter == human2_winner_counter:
                print("How does it feel to tie and win nothing?! Sucks right?\n""Play again because if you ain't first, you're last!\n")
                self.ask_new_game()
        pass        

    def run_game(self):
        self.contestants = []
        self.welcome_rules()
        self.game_mode()

    def valid_answer(self):
        while True:
            choice = input("Please type your RPSLS gesture choice here: ").casefold()
            if choice.lower() not in ("rock", "paper", "scissors", "lizard", "spock"):
                print("Please re-type your gesture choice.""\n")
            else:
                break
        return choice

    def find_round_winner(self, human1_choice, ai_player_choice):
        if human1_choice == ai_player_choice:
            return"Nobody"

        elif human1_choice == "rock":   
            if ai_player_choice == "scissors" or ai_player_choice ==  "lizard":
                return self.contestants[1].name
            elif ai_player_choice == "spock" or ai_player_choice == "paper":
                return self.contestants[0].name

        elif human1_choice == "paper":
            if ai_player_choice == "spock" or ai_player_choice == "rock":   
                return self.contestants[1].name
            elif ai_player_choice == "lizard" or ai_player_choice == "scissors":
                return self.contestants[0].name

        elif human1_choice == "scissors":
            if ai_player_choice == "paper" or ai_player_choice == "lizard":
                return self.contestants[1].name
            elif ai_player_choice == "rock" or ai_player_choice == "spock":
                return self.contestants[0].name

        elif human1_choice == "lizard":
            if ai_player_choice == "spock" or ai_player_choice == "paper":
                return self.contestants[1].name
            elif ai_player_choice == "rock" or ai_player_choice == "scissors":
                return self.contestants[0].name

        elif human1_choice == "spock":
            if ai_player_choice == "rock" or ai_player_choice == "scissors":
                return self.contestants[1].name
            elif ai_player_choice == "paper" or ai_player_choice == "lizard":
                return self.contestants[0].name

    def ask_new_game(self):
        new_game = input("Do you want to play again?\n"
        "Type (y)\n"
        "Type (n)  ")
        if new_game == "y":
            self.run_game()
        elif new_game == "n":
            print("See you next time.")
        else:
            self.ask_new_game()
