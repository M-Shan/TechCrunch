"""
    Script for making hangman game
    :file: hangman.py
    :platform: Windows 10
    :synopsis:
        This script is the parent file of hangman game.
        All the functions that make up the whole code
        are called here sequence wise. At the end, there
        is built-in choice for user to either again
        play the game or quit it.

    :author:
        Muhammad Faheem-ur-Rehman
        email: faheemlasani1034@gmail.com
"""

import hangman_functions


def main():
    flag = True
    key = True

    #saving the game data in a separate dictionary
    words_dict = {'COUNTRIES': ['GERMANY', 'UGANDA', 'FIJI', 'FINLAND', 'ARGENTINA', 'QATAR', 'EGYPT', 'AUSTRALIA'],
                  'SCIENCE': ['VELOCITY', 'INERTIA', 'REACTION', 'FUSION', 'GRAVITY', 'FORCE', 'ELECTRONS',
                              'RADIATION'],
                  'FRUITS': ['MANGO', 'GUAVA', 'PEAR', 'APRICOT', 'MELON', 'GRAPES', 'ORANGE', 'FIG'],
                  'PROFESSIONS': ['PHYSICIST', 'ASTRONOMER', 'BARTENDER', 'LIBRARIAN', 'GAMER', 'ACCOUNTANT', 'BUTLER',
                                  'BIOLOGIST']}

    #calling all basic functions
    hangman_functions.greeting_function()
    while flag:

        hangman_functions.display_categories()
        category = hangman_functions.user_input()
        guess_word, guess_list, memory_list = hangman_functions.generate_guess_word(words_dict, category)
        result = hangman_functions.game_starts(guess_list, memory_list)

        while key:
            again_play = input('DO YOU WANT TO PLAY AGAIN? (Y/N)')
            if again_play in ['Y', 'y']:
                break
            elif again_play in ['N', 'n']:
                flag = False
                break
            else:
                print('OOPS! WRONG INPUT. TRY AGAIN!')


if __name__ == '__main__':
    main()
