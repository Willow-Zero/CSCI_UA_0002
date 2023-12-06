from dice_games import *

def main():
    print('Let\'s play a dice game.')
    print('Boom')
    my_game = boomDiceGame('Boom')
    my_game.play_game()
    an = input('Would you like to play again? And weight your dice this time this time?(Y/N) ')
    if an == "Y" or an == "y":
        my_game2 = boomDiceGame("Boom (Weighted)",True)
        my_game2.play_game()
main()

