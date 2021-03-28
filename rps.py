#!/usr/bin/env python3
import random
import os
from colorama import Fore

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    # Master class for Every Player
    # To create a move of every player
    def move(self):
        return 'rock'

    # Learn the opponent moves
    def learn(self, my_move, their_move):
        self.their_move = their_move


def beats(one, two):
    # Check to see game conditions based on rules
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


def clear_screen():
    # To clear the screen after every game
    os.system('cls' if os.name == 'nt' else 'clear')


class ReflectPlayer(Player):
    # Computer player reflects the Human player moves after each move
    def __init__(self):
        super().__init__()
        self.their_move = None

    def learn(self, my_move, their_move):
        self.their_move = their_move

    def move(self):
        # if it's first move select a random move else reflect HumanPlayer move
        if self.their_move is None:
            return random.choice(moves)
        return self.their_move


class CyclePlayer(Player):
    # CyclePlayer class cycles through moves by making
    # everytime a different move
    def __init__(self):
        super().__init__()
        self.my_move = None

    def learn(self, my_move, their_move):
        self.my_move = my_move

    def move(self):
        # Cycle through every move
        if self.my_move is None:
            return random.choice(moves)
        elif self.my_move == 'rock':
            return 'paper'
        elif self.my_move == 'paper':
            return 'scissors'
        elif self.my_move == 'scissors':
            return 'rock'


class RandomPlayer(Player):
    # RandomPlayer used to generate the moves randomly
    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):
    # HumanPlayer to get the user's move
    def move(self):
        while True:
            try:
                # Foreground colors are used to color the Fonts
                move = input(f"{Fore.RED}Rock, \
{Fore.BLUE}Paper, \
{Fore.YELLOW}Scissors?{Fore.RESET} > ").lower()
                if move in moves:
                    return move
            except ValueError:
                pass


class Game:
    def __init__(self, p1, p2):
        # Initialize the Human Player and Computer Player
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        # play_round is a method to play rounds
        # Get the moves for Human and Computer Players
        move1 = self.p1.move()
        move2 = self.p2.move()

        print(f"Player 1: {move1}  Player 2: {move2}")

        if beats(move1, move2):
            # beats function is used to find out who 'WINS'
            print(f"{Fore.GREEN}** PLAYER ONE WINS **{Fore.RESET}")
            self.p1_score += 1
            print(f"Score: Player One - {self.p1_score}, \
Player Two - {self.p2_score}")
        elif beats(move2, move1):
            print(f"{Fore.LIGHTCYAN_EX}** PLAYER TWO WINS **{Fore.RESET}")
            self.p2_score += 1
            print(f"Score: Player One - {self.p1_score}, \
Player Two - {self.p2_score}")
        else:
            print(f"{Fore.LIGHTMAGENTA_EX}** TIE **{Fore.RESET}")
            print(f"Score: Player One - {self.p1_score}, \
Player Two - {self.p2_score}")

        # learn method is used to learn the Human Player moves
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        # play_game is used to initiate the game
        print(f"{Fore.RED}Rock{Fore.RESET} \
{Fore.BLUE}Paper{Fore.RESET} \
{Fore.YELLOW}Scissors,{Fore.RESET} \
{Fore.RESET}Go!\n")

        while True:
            try:
                # Get the play best of
                rounds = int(input("You want to play best of? \n> "))
                self.p1_score = 0
                self.p2_score = 0

                for round in range(rounds):
                    print(f"\nRound {round+1} --")
                    self.play_round()

                # Display Final Scores
                print(f"\n{Fore.LIGHTMAGENTA_EX}Final Scores are: \
{Fore.LIGHTBLUE_EX}Player one - \
{self.p1_score}{Fore.RESET} and \
{Fore.LIGHTYELLOW_EX}Player two - \
{self.p2_score}{Fore.RESET}")

                # Display who WINS, LOSE or TIE
                if self.p1_score > self.p2_score:
                    print(f"{Fore.GREEN}You Wins!{Fore.RESET}")
                elif self.p1_score < self.p2_score:
                    print(f"{Fore.LIGHTCYAN_EX}You lose!{Fore.RESET}")
                else:
                    print(f"{Fore.LIGHTMAGENTA_EX}Match is TIE!{Fore.RESET}")
                break
            except ValueError:
                print("Please enter number.")


def intro():
    # Display's introduction and rules of the game
    print(f"""
******************************************
*        {Fore.GREEN}Welcome to the world of{Fore.RESET}         *
*         {Fore.RED}Rock,{Fore.RESET}                          *
*         {Fore.BLUE}Paper,{Fore.RESET}                         *
*         {Fore.YELLOW}Scissors!{Fore.RESET}                      *
*  {Fore.GREEN}Rules:{Fore.RESET}                                *
*      {Fore.RED}1. Paper beats Rock;{Fore.RESET}              *
*      {Fore.BLUE}2. Rock beats Scissors;{Fore.RESET}           *
*      {Fore.YELLOW}3. Scissors beat Paper.{Fore.RESET}           *
******************************************
""")


if __name__ == '__main__':
    game = Game(HumanPlayer(), random.choice(
        [ReflectPlayer(), CyclePlayer()]))

    while True:
        clear_screen()
        intro()
        game.play_game()
        play_again = input("\nWant to play again y/n? ").lower()
        if play_again == 'n':
            print("Bye!")
            break
