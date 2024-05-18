# game_module.py

import random

# Liste de mots
word_database = ["letter", "puzzle", "definition", "advantage", "textbook"]

# Fonction pour choisir un mot aléatoirement
def choose_word():
    return random.choice(word_database)

# Fonction pour afficher le mot avec les lettres devinées
def display_word(word, guessed_letters):
    displayed_word = ''.join([letter if letter in guessed_letters else '_' for letter in word])
    return displayed_word

# Fonction pour afficher le dessin du pendu
def display_hangman(tries):
    stages = [
        """
           +---+
           |   |
               |
               |
               |
               |
        =========""",
        """
           +---+
           |   |
           O   |
               |
               |
               |
        =========""",
        """
           +---+
           |   |
           O   |
           |   |
               |
               |
        =========""",
        """
           +---+
           |   |
           O   |
          /|   |
               |
               |
        =========""",
        """
           +---+
           |   |
           O   |
          /|\\  |
               |
               |
        =========""",
        """
           +---+
           |   |
           O   |
          /|\\  |
          /    |
               |
        =========""",
        """
           +---+
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        ========="""
    ]
    return stages[tries]
