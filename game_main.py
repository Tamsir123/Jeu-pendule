# game_main.py

import game_module

def main():
    print(">> Bienvenue dans le jeu du pendu <<")
    word = game_module.choose_word()
    guessed_letters = set()
    tries = 0
    max_tries = 6
    word_guessed = False
    
    print("\nMot à deviner : " + game_module.display_word(word, guessed_letters))
    
    while tries < max_tries and not word_guessed:
        guess = input("\nProposez une lettre : ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Veuillez entrer une seule lettre valide.")
            continue
        
        if guess in guessed_letters:
            print("Vous avez déjà essayé cette lettre.")
            continue
        
        guessed_letters.add(guess)
        
        if guess in word:
            print("\nBonne lettre !")
        else:
            print("\nMauvaise lettre !")
            tries += 1
        
        print(game_module.display_hangman(tries))
        print("\nMot à deviner : " + game_module.display_word(word, guessed_letters))
        
        if '_' not in game_module.display_word(word, guessed_letters):
            word_guessed = True
    
    if word_guessed:
        print("\nFélicitations ! Vous avez deviné le mot :", word)
    else:
        print("\nDésolé, vous avez perdu. Le mot était :", word)

if __name__ == "__main__":
    main()
