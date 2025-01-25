# Write your solution here
import random

class WordGame():
    def __init__(self, rounds: int):
        self.wins1 = 0
        self.wins2 = 0
        self.rounds = rounds

    def round_winner(self, player1_word: str, player2_word: str):
        # determine a random winner
        return random.randint(1, 2)

    def play(self):
        print("Word game:")
        for i in range(1, self.rounds+1):
            print(f"round {i}")
            answer1 = input("player1: ")
            answer2 = input("player2: ")

            if self.round_winner(answer1, answer2) == 1:
                self.wins1 += 1
                print("player 1 won")
            elif self.round_winner(answer1, answer2) == 2:
                self.wins2 += 1
                print("player 2 won")
            else:
                pass # it's a tie

        print("game over, wins:")
        print(f"player 1: {self.wins1}")
        print(f"player 2: {self.wins2}")

class LongestWord(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):
        # your code for determining the winner goes here

        length1 = len(player1_word)
        length2 = len(player2_word)

        if length1 == length2:
            return 0
        return 1 if length1 > length2 else 2


class MostVowels(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def _count_vowels(self, string):
        return sum([1 for char in string if char.lower() in "aeiou"])

    def round_winner(self, player1_word: str, player2_word: str):

        vowels1 = self._count_vowels(player1_word)
        vowels2 = self._count_vowels(player2_word)

        if vowels1 == vowels2:
            return 0
        return 1 if vowels1 > vowels2 else 2


class RockPaperScissors(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):

        rules = {"paper": "rock", "rock": "scissors", "scissors": "paper"}
        words = ["paper", "rock", "scissors"]

        if player1_word == player2_word: 
            return 0 
        
        if player1_word not in words and player2_word not in words:
            return 0
        
        if player1_word in words and player2_word not in words:
            return 1
        
        if player1_word not in words and player2_word in words:
            return 2

        if rules.get(player1_word) == player2_word:
            return 1 
        return 2
        
            
        
    
